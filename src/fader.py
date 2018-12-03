import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt
from time import sleep


imagem1 = cv.imread("gandalf.jpg", 1)
imagem2 = cv.imread("gandalfrosa.jpeg", 1)

img1 = cv.resize(imagem1, (400,400))
img2 = cv.resize(imagem2, (400,400))

novaimg = img1 + img2

cv.imshow("imagens", novaimg)

cv.waitKey(0)
cv.destroyAllWindows()
