import cv2
import numpy as np
cam = cv2.VideoCapture(0)
fourcc = cv2.VideoWriter_fourcc(*'MJPG')
rec = cv2.VideoWriter("output.avi", fourcc, 17 , (640, 480))
flag = False

while 1:
    b, img = cam.read()
    if b:
        cv2.putText(img,"c-capture s-save q-quit",(100,50),cv2.FONT_HERSHEY_PLAIN,
                    fontScale=2,color=(100,100,100), thickness=3)
        key = cv2.waitKey(1) & OXFF
        if key == ord('0'):
            flag = True
            if flag:
                cv2.puttext(img, "Recording", (50, 100), cv2.FONT_HERSHEY_PLAIN, fontscale=2,
                            color=(100, 100, 100)
                            rec.write(img)
                            if key == ord('a'):
                                flag = False
                                if not flag:
                                    rec.release()

                                    if key == ord('q'):
                                        rec.release()
                                        break
                cv2.imshow("ViewPort", img)

                cv2.destroyAllWindows()



                      )