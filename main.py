from tkinter import *
import cv2
from PIL import Image, ImageTk

vid = cv2.VideoCapture(0)
faceCascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

width, height = 1500, 900

vid.set(cv2.CAP_PROP_FRAME_WIDTH, width)
vid.set(cv2.CAP_PROP_FRAME_HEIGHT, height)

app = Tk()

app.bind('<Escape>', lambda e: app.quit())

label_widget = Label(app)
label_widget.pack()

canvas = Canvas(app, width=width, height=height)
canvas.pack()

def draw_box(x, y, w, h):
    canvas.delete("all")
    canvas.create_rectangle(x, y, x+w, y+h, fill='red', width=2, outline='red')

def open_camera():
    _, frame = vid.read()

    imagetemp = cv2.cvtColor(frame, cv2.COLOR_BGR2RGBA)
    
    opencv_image = cv2.flip(imagetemp, 1)

    faces = faceCascade.detectMultiScale(opencv_image, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))

    for (x, y, w, h) in faces:
        draw_box(x, y, w, h)
        
        # cv2.rectangle(opencv_image, (x, y), (x+w, y+h), (0, 255, 0), 2)
        # faceCoordinatesX.append(x) # X-led 
        # faceCoordinatesY.append(y) # Y-led
        # faceCoordinatesW.append(w) # STRL 
        # faceCoordinatesH.append(h) # HÖJD
    
    captured_image = Image.fromarray(opencv_image)

    photo_image = ImageTk.PhotoImage(image=captured_image)

    label_widget.photo_image = photo_image

    # label_widget.configure(image=photo_image) # Ta bort om du inte vill ha bild

    label_widget.after(10, open_camera)


button1 = Button(app, text="Open Camera", command=open_camera)
button1.pack()

app.mainloop()

vid.release()
