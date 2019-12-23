import numpy as np
import cv2

img = cv2.imread('../images/devon.jpg')

b = img[:,:,0]
g = img[:,:,1]
r = img[:,:,2]

print(b)
print(g)
print(r)

cv2.imshow('Blue', b)
cv2.imshow('Green', g)
cv2.imshow('Red', r)
cv2.imshow('Image', img)

cv2.waitKey(0)
cv2.destroyAllWindows()
