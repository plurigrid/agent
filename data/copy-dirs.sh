#!/bin/bash

# The directory to process
top_level_dir=$1

# Function to copy files from a subdirectory and delete the subdirectory
copy_and_delete() {
    local subdir=$1

    # Copy all files from the subdirectory to the top level directory
    find "$subdir" -type f -exec cp {} "$top_level_dir" \;
    # echo "$subdir"

    # Delete the subdirectory
    # rm -rf "$subdir"
}

# Iterate through all subdirectories in the directory
find "$top_level_dir" -mindepth 1 -type d | while read -r subdir
do
    copy_and_delete "$subdir"
done
