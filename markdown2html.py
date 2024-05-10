#!/usr/bin/python3

import sys
import os

# Check if the correct number of arguments are provided
if len(sys.argv) < 3:
    print("Usage: ./markdown2html.py README.md README.html", file=sys.stderr)
    sys.exit(1)

# Assign command line arguments to variables
markdown_file = sys.argv[1]
output_file = sys.argv[2]

# Check if Markdown file exists
if not os.path.exists(markdown_file):
    print(f"Missing {markdown_file}", file=sys.stderr)
    sys.exit(1)

# Exit successfully
sys.exit(0)
