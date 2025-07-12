#!/bin/bash

# Simple script to run brainf*ck programs
# Usage: ./run.sh <filename.bf>

if [ $# -eq 0 ]; then
    echo "Usage: $0 <filename.bf>"
    echo "Available programs:"
    ls -1 *.bf 2>/dev/null || echo "No .bf files found"
    exit 1
fi

if [ ! -f "$1" ]; then
    echo "Error: File '$1' not found"
    exit 1
fi

echo "Running $1..."
python brainfuck_interpreter.py "$1"