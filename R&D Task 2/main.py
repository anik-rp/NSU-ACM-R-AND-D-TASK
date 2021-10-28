import cv2
import cv2 as cv
import numpy as np

def pattern_detect(location):
    img = cv.imread(location)
    output = img.copy()
    gray = cv.cvtColor(img,cv.COLOR_BGR2GRAY)
    img_blur = cv2.medianBlur(gray, 5)
    circles = cv.HoughCircles(gray, cv.HOUGH_GRADIENT, 1, 95,param1=100, param2 = 32, minRadius=0, maxRadius=0)
    detected_circles = np.uint16(np.around(circles))
    for (x, y ,r) in detected_circles[0, :]:
        cv.circle(output, (x, y), r, (0, 0, 255), 2)
    cv.imshow('output', output)
    cv.waitKey(0)

location = input("Enter The IMG File Location:")
pattern_detect(location)


