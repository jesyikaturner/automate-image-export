# Automate exporting files using tablet as bottom screen - Affinity Designer
# Has to be run from the folder where Affinity Designer saves the pictures

from ast import parse
import pyautogui as pag
import time
import os
import argparse
from dataclasses import dataclass  # Python 3.7


@dataclass
class Coord:
    x: int
    y: int


# Coord - (x, y)
# fileButton - File dropdown menu location
fileButton = Coord(2993, 24)
# exportButton - File -> Export...
exportButton = Coord(3027, 548)
# sizeField - The first box next to 'Size:' under Export Settings
sizeField = Coord(4154, 666)
# exportSettingsButtton - The Export button under Export Settings
exportSettingsButton = Coord(4553, 960)
# saveButton -
saveButton = Coord(3972, 1014)

filetype = ".png"


def save_and_move(filename, filesizes, filepath):
    for i in range(len(filesizes)):
        # click on File
        pag.click(fileButton.x, fileButton.y)

        # click on export
        pag.click(exportButton.x, exportButton.y)

        # click on size
        pag.click(sizeField.x, sizeField.y)

        # delay to make sure size is entered
        time.sleep(1.0)

        # enter a size
        pag.typewrite(filesizes[i])

        # click on export
        pag.click(exportSettingsButton.x, exportSettingsButton.y)

        # type in save filename
        savename = "{0}_{1}{2}".format(
            filename, filesizes[i], filetype)
        pag.typewrite(savename)
        print("[{0}/{1}] Saving file: {2} in './'.".format(i +
              1, len(filesizes), savename))

        # click on save
        pag.click(saveButton.x, saveButton.y)

        # another delay to make sure the save box is closed - and that the save file exists
        time.sleep(1.0)

        # should move file to directory
        os.rename("./{}".format(savename),
                  "{0}/{1}".format(filepath, savename))
        print("[{0}/{1}] Moving file from './{2}' to '{3}/{2}'.".format(i +
              1, len(filesizes), savename, filepath))


def main(*args):
    parser = argparse.ArgumentParser()
    parser.add_argument("FILENAME", metavar="filename",
                        type=str, help="name of the file")
    parser.add_argument("--list", dest="FILESIZES",
                        nargs="+", help="--list 1234 5678")
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

    save_and_move(args.FILENAME, args.FILESIZES)

    print("Program finished!")


if __name__ == '__main__':
    main()
