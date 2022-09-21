#!/bin/python3
# mapIt.py - Launches a map in the browser using an searchString from the
# command line or clipboard.

import webbrowser, sys, pyperclip
if len(sys.argv) > 1:
    # Get searchString from command line.
    searchString = ' '.join(sys.argv[1:])
    print(searchString)
else:
    # Get searchString from clipboard.
    searchString = pyperclip.paste()

webbrowser.open('https://duckduckgo.com/?q=' + searchString)