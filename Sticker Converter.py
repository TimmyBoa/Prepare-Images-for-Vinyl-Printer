# -*- coding: utf-8 -*-
"""
Created on Mon Jan 13 14:24:34 2025

@author: Tim
"""

from PIL import Image 
from rembg import remove
import os 

"""
Convert image to png and removes background
"""
def process_file(filename, extension, remove_background):
    if filename.endswith(extension):
        file_path = os.path.join(directory, filename)
        if os.path.exists(file_path):
            im = Image.open(file_path)
            
            if (extension==".gif"):
                im.seek(0)
            if (remove_background==True):
                im = remove(im)
            new_file_path = os.path.splitext(file_path)[0]+".png"
            im.save(new_file_path)
            if (extension != ".gif" and extension != ".png"):
                os.remove(file_path)
            print(os.path.join(directory, filename))
            
if __name__=="__main__":  
    directory = r'C:\Users\Tim\Pictures\Stickers'
    remove_background=True
    for filename in os.listdir(directory):
        if filename.endswith(".png"):
            process_file(filename, ".png", remove_background)
        elif filename.endswith(".jpg"):
            process_file(filename, ".jpg", remove_background)
        elif filename.endswith(".jpeg"):
            process_file(filename, ".jpeg", remove_background)
        elif filename.endswith(".gif"):
            process_file(filename, ".gif", remove_background)
        elif filename.endswith(".jfif"):
            process_file(filename, ".jfif", remove_background)
        elif filename.endswith(".webp"):
            process_file(filename, ".webp", remove_background)
        elif filename.endswith(".bmp"):
            process_file(filename, ".bmp", remove_background)

    