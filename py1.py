import cv2
import numpy as np
cam = cv2.VideoCapture(0)
fourcc = cv2.VideoWriter_fourcc(*'MJPG')
rec = cv2.VideoWriter('Videos.avi',fourcc,1,(640,480))
while True:
    b, img = Cam.read()
    cv2.imshow("ViewPort",img)
    rec.write(img)
    key = cv2.waitKey(1)&0xFF
    if key == ord('q'):
        rec.release()
        break
        cam.release()
        cv2.destroyAllWindows()


