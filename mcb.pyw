#! /usr/bin/python3

import pyperclip
import random
import shelve
import sys
import urllib


def download_image(url):
    name = random.randrange(1, 1000)
    real_name = str(name) + ".jpg"
    urllib.urlretrieve(url, real_name)


mcbShelf = shelve.open("mcb")

mcbShelf[pyperclip.paste()] = pyperclip.paste()

if len(sys.argv) == 2 and sys.argv[1] == "download":

    for keys in mcbShelf.keys():
        download_image(mcbShelf.keys())

if len(sys.argv) == 3 and sys.argv[1].lower() == "save":
    mcbShelf[sys.argv[2]] = pyperclip.paste()
elif len(sys.argv) == 2:
    if sys.argv[1].lower() == "list":
        pyperclip.copy(str(list(mcbShelf.keys())))
    elif sys.argv[1] in mcbShelf:
        pyperclip.copy(mcbShelf[sys.argv[1]])
    elif sys.argv[1].lower() == "delete":
        mcbShelf.clear()
elif len(sys.argv) == 3 and sys.argv[1].lower() == "delete":
    del mcbShelf[sys.argv[2]]

mcbShelf.close()
