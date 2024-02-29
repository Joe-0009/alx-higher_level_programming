#!/bin/bash

# Send a request to the specified URL and display the size of the response body in bytes

# Usage: ./0-body_size.sh <URL>

# Make sure the URL is provided as an argument
if [ $# -ne 1 ]; then
    echo "Usage: $0 <URL>"
    exit 1
fi

# Extract the size of the response body using curl
SIZE=$(curl -sI "$1" | grep -i 'content-length' | awk '{print $2}')

# Check if the size is present
if [ -z "$SIZE" ]; then
    echo "Could not determine the size of the response body."
else
    echo "$SIZE"
fi
