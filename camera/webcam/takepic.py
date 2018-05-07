import numpy as np
import cv2
import datetime
import os
import sys
import time
cwd = os.path.dirname(os.path.abspath(__file__))
img_dir = "{}/data/5-7-2018_0".format(cwd)

print(img_dir)

cap = cv2.VideoCapture(1)
delay = 10.0 # seconds
print("Starting with delay time: {}".format(delay))
while(True):
    # Capture frame-by-frame
    ret, frame = cap.read()

    # Our operations on the frame come here
    # gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    frame = frame[:,700:-300]
    # Display the resulting frame
    # cv2.imshow('frame', frame)
    timestamp = str(datetime.datetime.now()).replace(" ", "_")
    filename = "{}/{}.png".format(img_dir, timestamp)
    print("Writing to {}".format(filename))
    cv2.imwrite(filename, frame)

    # if cv2.waitKey(1) & 0xFF == ord('q'):
    #     break

    time.sleep(delay)

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()
