# automate_image_export

Python script that automates saving images at different resolutions in Affinity Designer and moving them into a folder

## Pre-requisites 

- Python 3.7
- PyAutoGUI

## Setup

1. Install python3

2. Install PyAutoGUI:
```bash
    python3 -m pip install pyautogui
```

## Run

**NOTE:** Has to be run from the folder where Affinity Designer saves the pictures
```bash
    python3 automate_export.py "helloworld" --list 128 512
```

