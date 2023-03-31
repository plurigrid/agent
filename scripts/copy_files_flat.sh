#!/bin/bash

# Usage: ./copy_files_flat.sh [source_directory] [destination_directory]

source_directory="$1"
destination_directory="$2"

# Check if the required arguments are provided
if [ -z "$source_directory" ] || [ -z "$destination_directory" ]; then
    echo "Usage: $0 [source_directory] [destination_directory]"
    exit 1
fi

# Create the destination directory if it doesn't exist
mkdir -p "$destination_directory"

# Use find to search for files in the source directory and its nested directories
# Use xargs and cp to copy the files to the destination directory
find "$source_directory" -type f -exec cp -- {} "$destination_directory" \;

echo "Files copied successfully from $source_directory to $destination_directory."
