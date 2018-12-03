import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt
from time import sleep


img1 = cv.imread("moon.jpg", 1)
img2 = cv.imread("huble.jpeg", 1)

x = 0.1
while x <= 1:
    img1[600:600] *= x
    img2[600:600] *= (1 - x)
    novaimg[600:600] = img1[:] + img2[:]
    x+=0.1
    cv.imshow("imagens", novaimg)
    cv.waitKey(0)

cv.destroyAllWindows()
