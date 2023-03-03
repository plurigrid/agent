from llama_index import GPTSimpleVectorIndex, SimpleDirectoryReader
from llama_index.readers.obsidian import ObsidianReader
from agent.config import config
import gradio as gr

import os


class IndexModel:
    def __init__(self, data_dir: str, index_path: str):
        self.index_path = index_path
        self.data_dir = data_dir
        if os.path.exists(index_path):
            print("loading index from disk...")
            self.index = GPTSimpleVectorIndex.load_from_disk(index_path)
        else:
            print("initializing index, this may take a moment...")
            print(data_dir)
            documents = ObsidianReader(data_dir).load_data()
            index = GPTSimpleVectorIndex(documents)
            index.save_to_disk(index_path)
            self.index = index
            
    def get_index(self):
        return self.index

    def query(self, question):
        print("question received: ", question)
        return self.index.query(question)

    def repl(self):
        while True:
            user_input = input(">>> ")
            print(self.query(user_input))

    def gradio(self, label, title):
        iface = gr.Interface(
            fn=self.query,
            inputs=gr.inputs.Textbox(
                label=label
            ),
            outputs="text",
            title=title,
            description="Ask anything!",
        )

        iface.launch(share=True)


if __name__ == "__main__":
    config = config.Config()
    model = IndexModel(config.DATA_DIR, config.INDEX_PATH)
    # model.repl()
