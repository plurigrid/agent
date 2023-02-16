# Zero-shot learning for expert systems
# Attempt 0
import os
import fnmatch
from langchain.document_loaders import UnstructuredPDFLoader

pdf_files = []

# Set the root directory to start searching for PDFs
root = "/Users/barton/Plurigrid/agent/unhack/Library"

# Traverse through all directories and subdirectories in the root directory
for path, subdirs, files in os.walk(root):
    for name in files:
        # Check if the file has a .pdf extension
        if fnmatch.fnmatch(name, '*.pdf'):
            # If it does, add its path to the list of PDF files
            pdf_files.append(os.path.join(path, name))

print(pdf_files)
