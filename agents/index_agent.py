import sys
from base_agent import BaseAgent

# from models import data_reader
import config


class IndexAgent(BaseAgent):
    def __init__(self):
        # self.data_reader = data_reader.DataReader()
        self.data_reader.load(config.DATA_DIR, config.INDEX_PATH)

    def handle_message(self, message):
        res = self.data_reader.index.query(message["content"])
        return res.response


if __name__ == "__main__":
    agent = IndexAgent()
