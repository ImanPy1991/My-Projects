import cv2
import matplotlib.pyplot as pt
from cvlib.object_detection import imagedetect_common_objects
import cvlib as cv
from cvlib.object_detection import draw_bbox

image = cv2.imread('iman-testRaw.jpg')
bbox , label , config = cv.imagedetect_common_objects(image)
output_image = draw_bbox(image , bbox , label , config)
pt.imshow(output_image)
pt.show()
print("number of Cars in the image is " ,str(label.count('car')))