from PIL import Image,ImageFilter
import cv2
from matplotlib import pyplot as plt
import numpy as np

#width
basewidth = 550
img = Image.open("ist.jpeg")
wpercent = (basewidth/float(img.size[0]))
hsize = int((float(img.size[1])*float(wpercent)))
img = img.resize((basewidth,hsize),Image.ANTIALIAS)
img.save("reserved_image.jpeg")

#height
baseheight = 366
img = Image.open("ist.jpeg")
hpercent = (baseheight/float(img.size[1]))
wsize = int((float(img.size[0])*float(hpercent)))
img = img.resize((wsize,baseheight),Image.ANTIALIAS)
img.save("reserved_image.jpeg")

from tkinter import Tk, Canvas

from PIL import ImageTk, Image

from tkinter import *

import tkinter.font as tkFont
import PIL.Image

master = Tk()

master.title('Image Resize')

frame_govde = Frame(master,width=basewidth,height=baseheight)
frame_govde.grid(row=1,column=0,rowspan=2)

def message():
    print("basarili")

img = PIL.Image.open('/Users/zerry/Desktop/SystemPro/reserved_image.jpeg')
photo = ImageTk.PhotoImage(img)

a=Button(frame_govde,image=photo,text="All stones preview",command=message,height=290,width=335,font=tkFont.Font(weight="bold",size=15))
a.grid(row=1, column=1)

master.mainloop()