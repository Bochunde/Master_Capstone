import tkinter
import cv2
import PIL.Image, PIL.ImageTk
from ultralytics import YOLO
class video_capture:
    def __init__(self, window, window_title, video_source,model):
        self.window = window
        self.window.title(window_title)
        self.video_source = video_source
        self.model = model
        # open video source

        self.vid = MyVideoCapture(video_source,self.model)
        # Create a canvas that can fit the above video source size
        self.canvas = tkinter.Canvas(window, width = self.vid.width, height = self.vid.height)
        self.canvas.pack()

        self.delay=15
        self.update()
        self.window.mainloop()
    def update(self):
        ret, frame = self.vid.get_frame()
        if ret:
            self.photo = PIL.ImageTk.PhotoImage(image = PIL.Image.fromarray(frame))
            self.canvas.create_image(0, 0, image = self.photo, anchor = tkinter.NW)
            #press q to quit
            if cv2.waitKey(1) & 0xFF == ord("q"):
                self.window.destroy()
        else:
            self.window.destroy()
        self.window.after(self.delay, self.update)

# Create a window and pass it to the Application object


class MyVideoCapture:
    def __init__(self, video_source,model):
        self.model = model
        self.vid = cv2.VideoCapture(video_source)
        if not self.vid.isOpened():
            raise ValueError("Unable to open video source", video_source)

        self.width = self.vid.get(cv2.CAP_PROP_FRAME_WIDTH)
        self.height = self.vid.get(cv2.CAP_PROP_FRAME_HEIGHT)

     # Release the video source when the object is destroyed

    def __del__(self):
        if self.vid.isOpened():
           self.vid.release()
        self.window.mainloop()

    def get_frame(self):
        if self.vid.isOpened():
            ret, frame = self.vid.read()
            results = self.model(frame)

        # view on frame
            annotated_frame = results[0].plot()
            if ret:
                # Return a boolean success flag and the current frame converted to BGR
                return (ret, cv2.cvtColor(annotated_frame, cv2.COLOR_BGR2RGB))
            else:
                return (ret, None)
        else:
            return (ret, None)
        


