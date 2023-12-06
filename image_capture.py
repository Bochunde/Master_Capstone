import cv2
import tkinter as tk
from tkinter import ttk
from ultralytics import YOLO
import matplotlib.pyplot as plt
import tkinter
import PIL.Image, PIL.ImageTk

class image_capture:
    def __init__(self, window, window_title, model,source):
        self.window = window
        self.model = model
        self.source = source
        self.window_title = window_title
        
        self.predicted_img = self.model(source)[0].plot()
        self.predicted_img = cv2.cvtColor(self.predicted_img,cv2.COLOR_BGR2RGB)
        self.predicted_img = self.image_resize()
        self.photo = PIL.ImageTk.PhotoImage(image = PIL.Image.fromarray(self.predicted_img))

        self.canvas = tkinter.Canvas(window, width = self.predicted_img.shape[1], height = self.predicted_img.shape[0])
        self.canvas.create_image(0, 0, image = self.photo, anchor = tkinter.NW)
        self.canvas.pack()
        self.window.mainloop()
    
    def image_resize(self,maxwidth=1920,maxheight=1080):
        if self.predicted_img.shape[0]>1080 or self.predicted_img.shape[1]>1920:
            f1 = maxwidth / self.predicted_img.shape[1]
            f2 = maxheight / self.predicted_img.shape[0]
            f = min(f1, f2)  # resizing factor
            dim = (int(self.predicted_img.shape[1] * f), int(self.predicted_img.shape[0] * f))
            resized = cv2.resize(self.predicted_img, dim)
            return resized
        else:
            return self.predicted_img
