import numpy as np
import cv2
img = cv2.imread('../images/typewriter.jpg')
#print(img.shape)

with open('../model/synset_words.txt', 'r') as syn_f:
    all_rows = syn_f.read().strip().split("\n")

classes = [r[r.find(' ')+1:] for r in all_rows]

net = cv2.dnn.readNetFromCaffe('../model/bvlc_googlenet.prototxt')

for i, c in enumerate(classes):
    if i == 100:
        break
    print( 1, c )


cv2.imshow('Image', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
