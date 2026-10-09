# CodeAlpha Project 3: JPG File Organizer

A Python automation script that moves `.jpg` and `.jpeg` files from a chosen folder into a `JPG_Images` subfolder.

## Features
- Asks the user for a folder path.
- Checks that the folder exists.
- Asks for confirmation before moving files.
- Recognizes `.jpg` and `.jpeg` extensions regardless of capitalization.
- Avoids overwriting files by creating a numbered alternative filename.
- Prints a summary of moved and skipped files.

## Requirements
- Python 3.8 or later
- No third-party packages required

## Run
```bash
python organize_jpgs.py
```

Enter a test folder path when prompted. Try this on a folder containing copies of images first.

## Concepts used
`pathlib`, `os`-style filesystem paths, `shutil`, functions, loops, conditions, exceptions, and file handling.

## Safety note
This script moves files. Test it with sample images in a temporary folder before using it on important files.
