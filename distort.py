import numpy as np
import cv2, random
from itertools import cycle


#Distortion types

def colorGray(frame):
    return cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

def colorYellow(frame):
    frame[:,:,0] = 0
    return frame


def colored(frame):
    return frame
def blacked(frame):
    frame [:,:,:] = 0
    return frame

def tearY(frame):
    size = frame.shape
    sizex = size[1]
    block = sizex/10
    blockx = random.random()*10*block
    frame[:,blockx:blockx+block,:] = 0
    return frame

#array to hold all the distortion types, colored is entered more times for more clear image

funcs = [colored,colored,colored,colorGray,colorYellow, tearY,blacked]

def main():
    cap = cv2.VideoCapture(0)
    disto = cycle(funcs)

    time = 0
    while(True):
        # Capture frame-by-frame
        ret, frame = cap.read()
        if time % 3 == 0:       #chooses how long to change the distortion
            distfunc = disto.next()
        frm = distfunc(frame)

        # Our operations on the frame come here
        #gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        # Display the resulting frame
        cv2.imshow('frame',frm)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
        time += int(random.random() * 10)       #add a random element to the distortion

        if time / 50  > 1:
            disto = cycle(funcs)                ## reshuffle the effects so it won't repeat so much.
            time = 0

    # When everything done, release the capture
    cap.release()
    cv2.destroyAllWindows()

if __name__ == '__main__':
    main()
