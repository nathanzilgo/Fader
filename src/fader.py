import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt
from time import sleep

imagem1 = cv.imread("thiago.jpeg", 1)

#plt.hist(imagem1.ravel(), 256, [0,256])
#plt.show()

for x in range(0, 10000):
    cv.imshow("imagem1", imagem1 * x)
    cv.waitKey(0)

cv.waitKey(0)
cv.destroyAllWindows()
