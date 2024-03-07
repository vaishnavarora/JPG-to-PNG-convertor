from PIL import Image
from tkinter import filedialog as file
import ntpath
import os as vaishnav

def IMG_conversion():
    filenames = []
    names = []
    print("choose file you want to convert from the box that appears.")
    get_img = file.askopenfilename()
    if get_img.endswith(".jpg"):
        img = Image.open(get_img)
        print("...converting...")
        filenames.append(ntpath.basename(get_img))
        for name in filenames:
            k = name.rfind(".jpg")
            names = name[:k]
        width, height = img.size
        sizes = width, height
        img.load()
        img.save(f"./{names}_converted.png","PNG")
        print("image converted successfully. Check your device to see the converted image")
    else:
        file_ext = vaishnav.path.splitext(get_img)
        ext_name = file_ext[1]
        print("Cannot convert your file as file is in", ext_name,"format. Give command again and choose a file that is in .jpg format")


IMG_conversion()
