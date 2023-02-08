from gpt_index import ObsidianReader, GPTSimpleVectorIndex, SimpleDirectoryReader
import os

# Set OBSIDIAN_VAULT_PATH to the path of your Obsidian vault
obsidian_path = os.getenv('OBSIDIAN_VAULT_PATH')
if obsidian_path is None:
    raise Exception('OBSIDIAN_VAULT_PATH environment variable not set')

openai_api_key = os.getenv('OPENAI_API_KEY')
if openai_api_key is None:
    raise Exception('OPENAI_API_KEY environment variable not set')

if os.path.exists('index.json'):
    index = GPTSimpleVectorIndex.load_from_disk('index.json')
else:
    documents = ObsidianReader(obsidian_path).load_data()
    print('initializing index, this may take several minutes...')
    index = GPTSimpleVectorIndex(documents) # Initialize index with documents
    index.save_to_disk('index.json')

print('ask any questions to the index, press CTRL+C to quit...')
while True:
    question = input(">>> ")
    print('querying response...')
    res = index.query(question)
    print(res.response)