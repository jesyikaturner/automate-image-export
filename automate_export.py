# Automate exporting files using tablet as bottom screen - Affinity Designer
# Has to be run from the folder where Affinity Designer saves the pictures

import pyautogui as pag
import time
import os
import argparse

filesizes = ["32", "64", "128", "256", "512", "1024"]
#filesizes = ["128", "256", "512", "1024", "1280"]
filetype = ".png"

# Coords - (x, y)
# fileButton - File dropdown menu location
# exportButton - File -> Export...
# sizeField - The first box next to 'Size:' under Export Settings
# exportSettingsButtton - The Export button under Export Settings
# saveButton - 
fileButton = (2993, 24)
exportButton = (3027, 548)
sizeField = (4154, 666)
exportSettingsButton = (4553, 960)
saveButton = (3972, 1014)


def main(*args):
    parser = argparse.ArgumentParser()
    parser.add_argument("FILENAME", metavar="filename", type=str, help="name of the file")
    args = parser.parse_args()

    filepath = "./"+args.FILENAME

    # Create a directory
    if not os.path.isdir(filepath):
        try:
            os.mkdir(filepath)
        except(OSError):
            print("Creation of the directory %s failed." % filepath)
        else:
            print("Successfully created the directory %s " % filepath)

    for i in range(len(filesizes)):
        # click on File
        pag.click(fileButton[0], fileButton[1])

        # click on export
        pag.click(exportButton[0], exportButton[1])

        # click on size
        pag.click(sizeField[0], sizeField[1])

        # delay to make sure size is entered
        time.sleep(1.0)

        # enter a size
        pag.typewrite(filesizes[i])

        # click on export
        pag.click(exportSettingsButton[0], exportSettingsButton[1])

        # type in save filename
        savename = "{0}_{1}{2}".format(args.FILENAME, filesizes[i], filetype)
        pag.typewrite(savename)
        print("[{0}/{1}] Saving file: {2} in './'.".format(i+1, len(filesizes), savename))

        # click on save
        pag.click(saveButton[0], saveButton[1])

        # another delay to make sure the save box is closed - and that the save file exists
        time.sleep(1.0)

        # should move file to directory
        os.rename("./{}".format(savename), "{0}/{1}".format(filepath, savename))
        print("[{0}/{1}] Moving file from './{2}' to '{3}/{2}'.".format(i+1, len(filesizes), savename, filepath))

    print("Program finished!")

if __name__ == '__main__':
    main()