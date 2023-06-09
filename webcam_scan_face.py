# file: webcam_scan_face.py
# author: Michael Pace
# created: 
# updated: 06.08.2023


# check os
from sys import platform
this_os = platform

# linux
def linux():
    this_os = "linux"

# mac
def mac():
    this_os = "darwin"

# windows
def windows():
    this_os = "win32"

# ==================================================================
# imports
import cv2  
import subprocess
import tkinter as tk
from tkinter import simpledialog

# load cascade classifier training file for haarcascade
# front view
front_casc_path = "face_data/haarcascade_frontalface_default.xml"
front_face_cascade = cv2.CascadeClassifier(front_casc_path)
# front view alt
front_alt_casc_path = "face_data/haarcascade_frontalface_alt.xml"
front_alt_face_cascade = cv2.CascadeClassifier(front_alt_casc_path)
# front view alt2
front_alt2_casc_path = "face_data/haarcascade_frontalface_alt2.xml"
front_alt2_face_cascade = cv2.CascadeClassifier(front_alt2_casc_path)
# profile view
profile_casc_path = "face_data/haarcascade_profileface.xml"
profile_face_cascade = cv2.CascadeClassifier(profile_casc_path)

# initialize camera
# *find camera device number*
if this_os == "linux":
    try:
        cam = cv2.VideoCapture(0)   # *set 0 to camera device number*
    except:
        cam = cv2.VideoCapture(1)   # *set 1 to camera device number*
if this_os == "darwin":
    pass
if this_os == "win32":
    cam = cv2.VideoCapture(0)   # *set 0 to camera device number*

# create window
#cv2.namedWindow("[ESC] to close, [SPACE] to save image")

while(True):
    # read frame
    ret, frame = cam.read()
    if not ret:
        print("Failed to grab frame.")
        break
    # convert to grayscale
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    # detect faces
    front_faces = front_face_cascade.detectMultiScale(              # front view
        gray,
        scaleFactor=1.1,
        minNeighbors=5,
        minSize=(30, 30),
        flags=cv2.CASCADE_SCALE_IMAGE
    )
    front_alt_faces = front_alt_face_cascade.detectMultiScale(      # front view alt
        gray,
        scaleFactor=1.1,
        minNeighbors=5,
        minSize=(30, 30),
        flags=cv2.CASCADE_SCALE_IMAGE
    )
    front_alt2_faces = front_alt2_face_cascade.detectMultiScale(    # front view alt2
        gray,
        scaleFactor=1.1,
        minNeighbors=5,
        minSize=(30, 30),
        flags=cv2.CASCADE_SCALE_IMAGE
    )
    profile_faces = profile_face_cascade.detectMultiScale(          # profile view
        gray,
        scaleFactor=1.1,
        minNeighbors=5,
        minSize=(30, 30),
        flags=cv2.CASCADE_SCALE_IMAGE
    )
    
    # draw rectangle around faces
    # front view
    if len(front_faces) > 0:
        #print("front face detected")       # *uncomment for debugging*
        for (x, y, w, h) in front_faces:
            cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)
    # front view alt
    elif len(front_alt_faces) > 0:
        #print("front alt face detected")   # *uncomment for debugging*
        for (x, y, w, h) in front_alt_faces:
            cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)
    # front view alt2
    elif len(front_alt2_faces) > 0:
        #print("front alt2 face detected")  # *uncomment for debugging*
        for (x, y, w, h) in front_alt2_faces:
            cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)
    # profile view
    elif len(profile_faces) > 0:
        #print("profile face detected")     # *uncomment for debugging*
        for (x, y, w, h) in profile_faces:
            cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)

    # display frame
    cv2.imshow("[ESC] to close, [SPACE] to save image", frame)
    k = cv2.waitKey(1)      # on key press
    if k%256 == 27:             # ESC pressed
        print("closing...")
        break
    elif k%256 == 32:           # SPACE pressed
        image_save = True  # toggle image saving --> True = save, False = save disabled
        if image_save:
            pass
            # *uncomment to enable frame capture & saving*
            # ***
            ROOT = tk.Tk()
            ROOT.withdraw()
            USER_INP = simpledialog.askstring(title="name",prompt="Name: ")

            img_name = "{}.png".format(USER_INP)
            cv2.imwrite(img_name, frame)
            print("{} written".format(img_name))
            # ***
        else:
            print("Image saving currently disabled.")
        
# release camera
cam.release()
# close windows
cv2.destroyAllWindows()
