import cv2
import numpy as np
from matplotlib import pyplot as plt
from time import sleep


img1 = cv2.imread("thiago.jpeg", 1)
img2 = cv2.imread("huble.jpeg", 1)

for x in range(0, 100000):
    cv2.imshow("imagem", img1 * x)
    cv2.waitKey(0)

cv2.destroyAllWindows()