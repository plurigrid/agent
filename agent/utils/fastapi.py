import logging
from pathlib import Path
from typing import Callable, Optional

from fastapi import FastAPI, Request, WebSocket, WebSocketDisconnect, Depends
from fastapi.templating import Jinja2Templates
from langchain.vectorstores import VectorStore

from agent.utils.callback import (
    QuestionGenCallbackHandler,
    StreamingLLMCallbackHandler,
)
from agent.utils.schemas import ChatResponse
import uvicorn


class AppState:
    def __init__(self, chain_handler):
        self.chain_handler = chain_handler


templates = Jinja2Templates(directory="agent/utils/templates")
app = FastAPI()
app_state = AppState(None)


def get_chain_handler():
    return app_state.chain_handler


def run():
    uvicorn.run(app, host="0.0.0.0", port=9000)


@app.on_event("startup")
async def startup_event():
    logging.info("starting up")


@app.get("/")
async def get(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})


@app.websocket("/chat")
async def websocket_endpoint(
    websocket: WebSocket, get_chain: Callable = Depends(get_chain_handler)
):
    await websocket.accept()
    # question_handler = QuestionGenCallbackHandler(websocket)
    stream_handler = StreamingLLMCallbackHandler(websocket)
    chat_history = []
    # chain_handler = get_chain()
    qa_chain = get_chain(stream_handler)
    # Use the below line instead of the above line to enable tracing
    # Ensure `langchain-server` is running
    # qa_chain = get_chain(vectorstore, question_handler, stream_handler, tracing=True)

    while True:
        try:
            # Receive and send back the client message
            question = await websocket.receive_text()
            resp = ChatResponse(sender="you", message=question, type="stream")
            await websocket.send_json(resp.dict())

            # Construct a response
            start_resp = ChatResponse(sender="agent", message="", type="start")
            await websocket.send_json(start_resp.dict())

            result = await qa_chain.acall(
                {"input": question, "chat_history": chat_history}
            )
            print(result)
            chat_history.append((question, result["output"]))
            end_resp = ChatResponse(sender="agent", message="", type="end")
            await websocket.send_json(end_resp.dict())
        except WebSocketDisconnect:
            logging.info("websocket disconnect")
            break
        except Exception as e:
            logging.error(e)
            resp = ChatResponse(
                sender="agent",
                message="Sorry, something went wrong. Try again.",
                type="error",
            )
            await websocket.send_json(resp.dict())


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=9000)
