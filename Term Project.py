from tkinter import *
from abc import ABC, abstractmethod
from collections import deque
import cv2
import imutils
import numpy as np

window=Tk()
window.geometry("600x600")
window.title(" Project")
def start():

    class tennis_ball_detect(ABC):

        def __init__(self):
            self.video_file = ''
            self.WIDTH = 600
            self.ONLY_MAX = False
            self.NO_OF_POINTS = 2
            self.GREEN_RANGE = ((28, 44, 98), (44, 230, 255))

        @abstractmethod
        def num_of_balls(self):
            pass

        @abstractmethod
        def coordinates(self):
            pass

    class region_number(tennis_ball_detect):

        def num_of_balls(self):

            colorLower, colorUpper = self.GREEN_RANGE
            if len(self.video_file) == 0:
                kamera = cv2.VideoCapture(0)
            else:
                kamera = cv2.VideoCapture(self.video_file)
            cv2.namedWindow('proje')
            cv2.moveWindow('proje', 120, 120)
            while True:
                (ok, frame) = kamera.read()
                if len(self.video_file) > 0 and not ok:
                    break
                frame = imutils.resize(frame, self.WIDTH)
                hsv = cv2.GaussianBlur(frame, (1, 1), 0)
                hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
                mask = cv2.inRange(hsv, colorLower, colorUpper)
                mask = cv2.erode(mask, None, iterations=3)
                mask = cv2.dilate(mask, None, iterations=3)
                mask_copy = mask.copy()
                contours = cv2.findContours(mask_copy, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)[-2]
                if len(contours) > 0:
                    for ctr in contours:
                        if self.ONLY_MAX:
                            cmax = max(contours, key=cv2.contourArea)
                            (x, y), radius = cv2.minEnclosingCircle(cmax)

                        else:
                            (x, y), radius = cv2.minEnclosingCircle(ctr)

                        if radius >= 30:
                            cv2.circle(frame, (int(x), int(y)), int(radius), (0, 255, 255), 2)

                number_of_objects_in_image = len(contours)
                cv2.putText(frame, "Number of Balls/Regions: " + str(number_of_objects_in_image), (50, 50),
                            cv2.FONT_HERSHEY_SIMPLEX, 0.75, (0, 0, 0), 3, cv2.LINE_AA)

                cv2.imshow("proje", frame)
                if cv2.waitKey(1) & 0xFF == 27:
                    break
            kamera.release()
            cv2.destroyAllWindows()

        def coordinates(self):
            colorLower, colorUpper = self.GREEN_RANGE
            if len(self.video_file) == 0:
                kamera = cv2.VideoCapture(0)
            else:
                kamera = cv2.VideoCapture(self.video_file)
            pts = deque(maxlen=self.NO_OF_POINTS)
            cv2.namedWindow('proje')
            cv2.moveWindow('proje', 120, 120)
            while True:
                (ok, frame) = kamera.read()
                if len(self.video_file) > 0 and not ok:
                    break
                frame = imutils.resize(frame, self.WIDTH)
                hsv = cv2.GaussianBlur(frame, (1, 1), 0)
                hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
                mask = cv2.inRange(hsv, colorLower, colorUpper)
                mask = cv2.erode(mask, None, iterations=3)
                mask = cv2.dilate(mask, None, iterations=3)
                mask_copy = mask.copy()
                contours = cv2.findContours(mask_copy, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)[-2]
                centers = None
                if len(contours) > 0:
                    for ctr in contours:
                        if self.ONLY_MAX:
                            cmax = max(contours, key=cv2.contourArea)
                            (x, y), radius = cv2.minEnclosingCircle(cmax)
                            centers = (int(x), int(y))

                        else:
                            (x, y), radius = cv2.minEnclosingCircle(ctr)
                            centers = (int(x), int(y))
                        pts.appendleft(centers)
                        for i in range(1, len(pts)):
                            if pts[i] and pts[i]:
                                thickness = 8
                                cv2.line(frame, pts[i], pts[i], (0, 0, 0), thickness)
                                cv2.putText(frame, str(centers), centers, cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 0), 4,
                                            cv2.LINE_AA)

                cv2.imshow("proje", frame)
                if cv2.waitKey(1) & 0xFF == 27:
                    break
            kamera.release()
            cv2.destroyAllWindows()

        def centroid(self):
            pass

    class general_control(tennis_ball_detect):

        def num_of_balls(self):
            pass

        def coordinates(self):
            pass

        def centroid(image):
            WINDOW_NAME = 'GreenBallTracker'
            blur = cv2.GaussianBlur(image, (1, 1), 0)
            hsv = cv2.cvtColor(blur, cv2.COLOR_BGR2HSV)
            lower_green = np.array([28, 44, 98])
            upper_green = np.array([44, 230, 255])
            mask = cv2.inRange(hsv, lower_green, upper_green)
            bmask = cv2.GaussianBlur(mask, (1, 1), 0)
            moments = cv2.moments(bmask)
            m00 = moments['m00']
            centroid_x, centroid_y = None, None
            if m00 != 0:
                centroid_x = int(moments['m10'] / m00)
                centroid_y = int(moments['m01'] / m00)
            ctr = (-1, -1)
            if centroid_x != None and centroid_y != None:
                thickness = 3
                ctr = (centroid_x, centroid_y)
                cv2.circle(image, ctr, 4, (0, 0, 0), thickness)
                cv2.putText(image, "Overall Centroid", ctr, cv2.FONT_HERSHEY_SIMPLEX, 0.65, (0, 0, 0), 2, cv2.LINE_AA)
            cv2.imshow(WINDOW_NAME, image)
            if cv2.waitKey(1) & 0xFF == 27:
                ctr = None
            return ctr

        if __name__ == '__main__':
            capture = cv2.VideoCapture(0)
            while True:
                okay, image = capture.read()
                if okay:
                    if not centroid(image):
                        break
                    if cv2.waitKey(1) & 0xFF == 27:
                        break
                else:
                    print('Capture failed')
                    break

    deneme2 = region_number()
    deneme = general_control()

    deneme2.num_of_balls()
    deneme2.coordinates()
    deneme.centroid()


def stop():
    exit()

label1=Label(window, text='Project', relief="solid", width=20, font=("arial",19,"bold"))
label1.place(x=150, y=55)

label2=Label(window, text='Name:Enes Faruk', width=20, font=("arial",10,"bold"))
label2.place(x=90, y=130)

label3=Label(window, text='Surname:Keskin', width=20, font=("arial",10,"bold"))
label3.place(x=87, y=180)

b1=Button(window, text="Start", width=12, bg="brown", fg="white", command=start)
b1.place(x=150, y=300)

b2=Button(window, text="Exit", width=12, bg="brown", fg="white", command=stop)

b2.place(x=280, y=300)
window.mainloop()
