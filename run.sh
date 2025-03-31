#!/bin/bash

if [ -z "$1" ]; then
    echo "Usage: $0 <source-file>"
    exit 1
fi

FILE="$1" 
EXT="${FILE##*.}"
BASENAME="${FILE%.*}"

PROJECT_DIR=$(realpath "$(dirname "$0")/../")

OUTDIR="$PROJECT_DIR/bin/"
OUTPUT="$OUTDIR$BASENAME"
OUTPUT_DIR=$(dirname "$OUTPUT")

mkdir -p "$OUTPUT_DIR"

case "$EXT" in
    cpp)
        OUTPUT="$OUTPUT"
        g++ -o "$OUTPUT" "$FILE"
        if [ $? -eq 0 ]; then
            "$OUTPUT"
        else 
            echo "C Compilation failed."
        fi
        ;;
    java) 
        javac -d "$OUTPUT_DIR" "$FILE"
        if [ $? -eq 0 ]; then
            CLASS_NAME=$(basename "$BASENAME")
            java -cp "$OUTPUT_DIR" "$CLASS_NAME"
        else
            echo "Java Compilation failed."
        fi
        ;;
    hs) 
        ghc --make "$FILE" -outputdir "$OUTPUT_DIR" -o "$OUTPUT"
        if [ $? -eq 0 ]; then
            "$OUTPUT"
        else
            echo "Haskell compilation failed."
        fi
        ;;
    *)
        echo "Unsupported file type: $EXT"
        exit 1
        ;;
esac