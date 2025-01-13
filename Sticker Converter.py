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
    remove_background=False
    file_extensions=[".png",".jpg",".jpeg",".gif",".jfif",".webp",".bmp"]
    for filename in os.listdir(directory):
        for extension in file_extensions:
            if filename.endswith(extension):
                process_file(filename, extension, remove_background)   
                break
