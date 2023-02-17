from gpt_index import GPTSimpleVectorIndex, SimpleDirectoryReader

import os


class DataReader:
    def load(self, data_dir: str, index_path: str):
        self.index_path = index_path
        self.data_dir = data_dir
        if os.path.exists(index_path):
            print("loading index from disk...")
            self.index = GPTSimpleVectorIndex.load_from_disk(index_path)
        else:
            print("initializing index, this may take a moment...")
            documents = SimpleDirectoryReader(data_dir).load_data()
            index = GPTSimpleVectorIndex(documents)
            index.save_to_disk(index_path)
            self.index = index
