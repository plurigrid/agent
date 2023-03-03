from llama_index import SimpleDirectoryReader, GPTChromaIndex, GPTSimpleVectorIndex
from langchain.chains.conversation.memory import ConversationBufferMemory, ConversationSummaryMemory
from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.vectorstores import Chroma
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain import OpenAI, VectorDBQA, ConversationChain
from langchain.chains import ChatVectorDBChain
from langchain.chains.chat_vector_db.prompts import CONDENSE_QUESTION_PROMPT
from langchain.agents import initialize_agent

from llama_index import GPTSimpleVectorIndex
import json


from langchain.document_loaders import PagedPDFSplitter
from langchain.docstore.document import Document

import gradio as gr



# documents = PagedPDFSplitter("/Users/barton/Lab/poet/agent/vdf.pdf").load_data()

# index = GPTSimpleVectorIndex(documents)
# index.save_to_disk('index.json') # TODO: use Zulip UUID here!


# pages = loader.load_and_split()



# import gradio as gr

# # import wandb # Catcth me if you can

# documents = SimpleDirectoryReader('/Users/barton/Lab/poet/')
# #index = GPTChromaIndex(documents, chroma_collection="iea")

embeddings = OpenAIEmbeddings()

tools = []
llm = OpenAI(temperature=0.42, model="text-davinci-003")
memory = ConversationSummaryMemory(memory_key="chat_history", llm=llm)

notagent = initialize_agent(tools,
    llm=llm,
    agent="conversational-react-description",
    verbose=True,
    memory=memory)




conversation_with_summary = ConversationChain(
    llm=llm,
    memory=ConversationSummaryMemory(llm=OpenAI()),
    verbose=True
)

def langchain_chat(input_text):
    #response = notagent.run(input = input_text)
    response = conversation_with_summary.predict(input=input_text)
    return response


for page in pages[:10]:
    langchain_chat(json.loads(page.json())['page_content'])

# qa = ChatVectorDBChain.from_llm(llm, vectorstore)


iface = gr.Interface(fn=langchain_chat, 
                     inputs=gr.inputs.Textbox(label="gm gm ☀️"), 
                     outputs="text",
                     title="Lucas Personal Agent",
                     description="Talk to ️his thing!")
iface.launch(share = True)


# #text_splitter = CharacterTextSplitter(chunk_size=1000, chunk_overlap=16)
# #texts = text_splitter.split_documents(documents)



# # qa = VectorDBQA.from_chain_type(llm=OpenAI(), chain_type="map_reduce", vectorstore=docsearch)




# # print(index.query("What is the future of Ukraine?"))


# # llm = OpenAI(temperature=0)
# # conversation = ConversationChain(
# #     llm=llm, 
# #     verbose=True, 
# #     memory=ConversationBufferMemory()
# # )





# # print(conversation.predict(input="What does the second law of thermodynamics state?"))

# # # llm_predictor = LLMPredictor(llm=OpenAI(temperature=0, model_name="text-davinci-003"))
# # # index = GPTKeywordTableIndex(documents, llm_predictor=llm_predictor)

# # # response = index.query("How would you use diagrams to illustrate Seeing Like a State?")
# # # print(response)