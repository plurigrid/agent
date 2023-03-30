import logging
from pathlib import Path
from typing import Optional

from fastapi import FastAPI, Request, WebSocket, WebSocketDisconnect
from fastapi.templating import Jinja2Templates
from langchain.vectorstores import VectorStore

from agent.utils.callback import (
    QuestionGenCallbackHandler,
    StreamingLLMCallbackHandler,
)
from agent.utils.schemas import ChatResponse
import uvicorn


class AppState:
    def __init__(self, get_chain):
        self.vector_store: Optional[VectorStore] = None
        self.get_chain


templates = Jinja2Templates(directory="templates")
app = FastAPI()


class App:
    def __init__(self, get_chain):
        self.get_chain = get_chain

    def run(self):
        uvicorn.run(self.app, host="0.0.0.0", port=9000)

    def setup_routes(self):
        self.app.get("/")(self.get)

    # @self.app.on_event("startup")
    # async def startup_event():
    #     logging.info("starting up")

    async def get(self, request: Request):
        return self.templates.TemplateResponse("index.html", {"request": request})

    # @app.websocket("/chat")
    # async def websocket_endpoint(self, websocket: WebSocket):
    #     await websocket.accept()
    #     # question_handler = QuestionGenCallbackHandler(websocket)
    #     stream_handler = StreamingLLMCallbackHandler(websocket)
    #     chat_history = []
    #     qa_chain = self.get_chain(stream_handler)
    #     # Use the below line instead of the above line to enable tracing
    #     # Ensure `langchain-server` is running
    #     # qa_chain = get_chain(vectorstore, question_handler, stream_handler, tracing=True)

    #     while True:
    #         try:
    #             # Receive and send back the client message
    #             question = await websocket.receive_text()
    #             resp = ChatResponse(sender="you", message=question, type="stream")
    #             await websocket.send_json(resp.dict())

    #             # Construct a response
    #             start_resp = ChatResponse(sender="bot", message="", type="start")
    #             await websocket.send_json(start_resp.dict())

    #             result = await qa_chain.acall(
    #                 {"question": question, "chat_history": chat_history}
    #             )
    #             chat_history.append((question, result["answer"]))

    #             end_resp = ChatResponse(sender="agent", message="", type="end")
    #             await websocket.send_json(end_resp.dict())
    #         except WebSocketDisconnect:
    #             logging.info("websocket disconnect")
    #             break
    #         except Exception as e:
    #             logging.error(e)
    #             resp = ChatResponse(
    #                 sender="agent",
    #                 message="Sorry, something went wrong. Try again.",
    #                 type="error",
    #             )
    #             await websocket.send_json(resp.dict())


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=9000)
