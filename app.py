#This file is the root file for fruit detection system.
from video_capture import *
from image_capture import *
from real_time_capture import *

import tkinter as tk
from tkinter import ttk
from ultralytics import YOLO

from tkinter import filedialog


#from main import load_model
import os
from tkinter import font

def load_model():
    file_path = filedialog.askopenfilename(
        filetypes=[("PyTorch Model Files", "*.pt")],
        title="Select a PyTorch Model File"
    )

    if file_path != "":
        global model_name_label
        model_name_label.config(text='Current Model is: '+os.path.basename(file_path)) 
        global model 
        model = YOLO(file_path)

def video_capture_onclick():
    file_path = filedialog.askopenfilename(
        filetypes=[("video file", "*.asf *.avi *.gif *.mkv *.mov *.mp4 *.mpeg *.mpg *.ts *.wmv *.webm")],
        title="Select a Video File"
    )
    if file_path != "":
        video_capture(tkinter.Toplevel(), window_title="video detection",video_source=file_path,model=model)

def real_time_capture_onclick():
    real_time_capture(tkinter.Toplevel(), window_title="real-time detection",model=model)

def image_capture_onclick():
    file_path = filedialog.askopenfilename(
        filetypes=[("Image Files", "*.bmp *.dng *.jpeg *.jpg *.mpo *.png *.tif *.tiff *.webp *.pfm")],
        title="Select an Image"
    )
    if file_path != "":    
        image_capture(tkinter.Toplevel(), window_title="image detection",model=model,source=file_path)

    
root = tk.Tk()
root.geometry("500x600")
root.title('Fruit Detection')
root.config(bg='white')
root.resizable(False,False)

model_name = 'Current Model is: fruit_detect.pt'
model = YOLO('best.pt')

label_font = font.Font(size=15, weight="bold")
model_name_label = ttk.Label(root,text=model_name,font=label_font,background='white')
model_name_label.pack(ipady=50)

load_model_button = ttk.Button(text='Import Model',cursor='hand2',command=load_model)
load_model_button.pack(ipady=50,fill='x')
#video_capture(tkinter.Tk(), "Tkinter and OpenCV",'apple_video.mp4',model=YOLO('best_train36.pt'))

load_image_button = ttk.Button(text='Input Image',cursor='hand2',command=image_capture_onclick)
load_image_button.pack(ipady=50,fill='x')


load_video_button = ttk.Button(text='Input Video',cursor='hand2',command=video_capture_onclick)
load_video_button.pack(ipady=50,fill='x')

load_camera_button = ttk.Button(text='Use Camera',cursor='hand2',command=real_time_capture_onclick)
load_camera_button.pack(ipady=50,fill='x')


root.mainloop()