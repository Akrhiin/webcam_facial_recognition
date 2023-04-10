# imports
import cv2  
import tkinter as tk
from tkinter import simpledialog

# load cascade classifier training file for haarcascade
frontCascPath = "face_data/haarcascade_frontalface_default.xml"
profilCascPath = "face_data/haarcascade_profileface.xml"
frontFaceCascade = cv2.CascadeClassifier(frontCascPath)
profilFaceCascade = cv2.CascadeClassifier(profilCascPath)

# initialize camera
cam = cv2.VideoCapture(0)

# create window
cv2.namedWindow("cam_feed")

while(True):
    # read frame
    ret, frame = cam.read()
    if not ret:
        print("Failed to grab frame.")
        break
    # convert to grayscale
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    # detect faces
    frontFaces = frontFaceCascade.detectMultiScale(
        gray,
        scaleFactor=1.1,
        minNeighbors=5,
        minSize=(30, 30),
        flags=cv2.CASCADE_SCALE_IMAGE
    )
    profileFaces = profilFaceCascade.detectMultiScale(
        gray,
        scaleFactor=1.1,
        minNeighbors=5,
        minSize=(30, 30),
        flags=cv2.CASCADE_SCALE_IMAGE
    )
    # draw rectangle around faces
    if len(frontFaces) > 0:
        for (x, y, w, h) in frontFaces:
            cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)
    elif len(profileFaces) > 0:
        for (x, y, w, h) in profileFaces:
            cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)
    # display frame
    cv2.imshow("cam_feed", frame)
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