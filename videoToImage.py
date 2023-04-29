# Imports
import cv2
import os

# Playing video from file:
cap = cv2.VideoCapture('VID_20230410_142719.mp4')

# Creation data folder
try:
    if not os.path.exists('data'):
        os.makedirs('data')
except OSError:
    print('Error: Creating folder data')

currentFrame = 0
while True:
    # Capture frame-by-frame
    ret, frame = cap.read()

    # Saves image of the current frame in jpg file
    name = './data/' + str(currentFrame) + '.jpg'
    print('Creating...' + name)
    cv2.imwrite(name, frame)

    # Increase currentFrame, to stop duplicate images
    currentFrame += 1
