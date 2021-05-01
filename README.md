# image-processing
Image Processing

Project Report
	While creating this project, I defined 3 different classes. These are tennis_ball_detect (ABC), region_number (tennis_ball_detect) and finally general_control (tennis_ball_detect). Tennis_ball_detect (ABC) class is abstract class and objects cannot be created from this class. There are init method and 2 abstract methods num_of_balls and coordinates.

	Since there is no object created from the abstract class, I have defined 2 subclasses region_number (tennis_ball_detect) and general_control(tennis_ball_detect).Region_number subclass which inherits from tennis_ball_detect super class and  with the num_of_balls function it finds the number of balls on the camera and with the coordinates function it finds the coordinates of the balls on the camera.Second subclass is general_control(tennis_ball_detect) this subclass also inherits from the tennis ball detect class. There is a def centroid method in this general_control (tennis_ball_detect) class. The def centroid method in this class shows us the centroid coordinates of the tennis balls shown on the camera.

	I used tkinter to create the homepage interface to run this project. In this interface, there is a field that shows my information and there are buttons to start and end the project.For this I have defined two methods def start and def exit. The def start method is for the button that starts the project, and the def exit method contains the properties of the button that ends the project.

	There are some imports required for this project to work. These are from tkinter import *, from abc import ABC, abstractmethod,
from collections import deque, import cv2, import imutils, import numpy as np.

References;

- https://medium.com/operations-management-türkiye/opencv-ile-temel-resim-kamera-i̇şlemleri-14294a688965

- https://medium.com/@rinu.gour123/ai-python-computer-vision-tutorial-with-opencv-b7f86c3c6a1a

- https://www.btkakademi.gov.tr/portal/course/s-f-rdan-ileri-seviye-python-programlama-5877#!/about

- https://opencv-python-tutroals.readthedocs.io/en/latest/py_tutorials/py_tutorials.html


								Enes Faruk KESKİN
