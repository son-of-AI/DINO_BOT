# -*- coding: utf-8 -*-
"""
Created on Sat Dec  8 17:34:27 2018

@author: veron
"""

from PIL import ImageGrab, ImageOps
import pyautogui
import time
from numpy import *

class Cordinates():
    replaybtn=(305, 370)
    dinosaur=(69, 375)
    #y=386
    #x=86
    
def restartGame():
    pyautogui.click(Cordinates.replaybtn)
    
def pressSpace():
    pyautogui.keyDown('up')   
    time.sleep(0.1) 
    print("jump")
    
    pyautogui.keyUp('up')
    
    
    
    

    
   
def imageGrab():
    box=(105,360,135,390)
    image = ImageGrab.grab(box)
    grayImage = ImageOps.grayscale(image)
    a = array(grayImage.getcolors())
    if a.sum()!=1147:
        print(a.sum())
    return(a.sum())    

    

def main():
    restartGame()
    
    while True:
        b=imageGrab()
        if b!=1147:        
            pressSpace()
            time.sleep(0.1)
    
    
main()


   