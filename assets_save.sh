#!/bin/bash

# Directory to save the downloaded assets
OUTPUT_DIR="./assets"
# File containing the list of URLs
URL_FILE="assets.txt"

# Create the output directory if it doesn't exist
mkdir -p "$OUTPUT_DIR"

# Check if the URL file exists
if [ ! -f "$URL_FILE" ]; then
    echo "Error: URL file '$URL_FILE' does not exist."
    exit 1
fi

# Download each URL in the file
while IFS= read -r url; do
    # Skip empty lines or lines starting with #
    if [[ -z "$url" || "$url" =~ ^# ]]; then
        continue
    fi

    # Extract the filename from the URL
    filename=$(basename "$url")

    # Check if the file already exists in the output directory
    if [ -f "$OUTPUT_DIR/$filename" ]; then
        echo "File already exists, skipping: $filename"
        continue
    fi

    # Download the file
    echo "Downloading: $url"
    wget -q --show-progress -P "$OUTPUT_DIR" "$url"
    if [ $? -ne 0 ]; then
        echo "Failed to download: $url"
    fi
done < "$URL_FILE"

echo "All downloads are complete. Files saved in '$OUTPUT_DIR'."