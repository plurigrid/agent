from enum import Enum

class IndexAgentType(Enum):
    TOOL = 1
    MEMORY = 2
    
class IndexFileType(Enum):
    MARKDOWN = 1

class Config:
    # Zulip API key
    ZULIP_CONFIG_PATH = "~/zuliprc.txt"
    # Zulip server url
    ZULIP_BASE_URL = "https://plurigrid.zulipchat.com"
    # Zulip stream to listen and send messages on
    ZULIP_STREAM = "unhack"
    # Zulip topic to listen and send messages on
    ZULIP_TOPIC = "gm"
    # Cosmos chain ID
    CHAIN_ID = "juno-1"
    # Cosmos LCD URL
    LCD_URL = "https://lcd-juno.keplr.app"
    # Contract address to send messages to
    CONTRACT_ADDRESS = "juno177zg5chuaxelxhr7qjzgjrvhm75c042xtme564d3mf7g3928pydq3x8lku"
    # Index created by GPTIndex
    INDEX_PATH = "./indices/index.json"
    # Documents fed into GPTIndex
    DATA_DIR = "/Users/janitachalam/code/plurigrid/ontology/journal/janita"
    # Documents to feed into Langchain VectorStore
    DOCUMENT_PATH = "./"
    # Type of index agent to instantiate
    INDEX_AGENT_TYPE = IndexAgentType.TOOL
    # Type of input files that index supports
    INDEX_FILE_TYPE = IndexFileType.MARKDOWN

