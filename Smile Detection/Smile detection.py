import cv2
#The_desired_image = cv2.imread('Smile Pic1.jpg','Smile Pic2.jpg','Smile Pic3.jpg','Smile Pic4.jpg','Smile Pic5.jpg','Smile Pic6.jpg')
for The_desired_image in range(5):
    The_desired_image = cv2.imread('Smile Pic1.jpg')
    smile_detect = cv2.CascadeClassifier('haarcascade_smile.xml')
    smilesS = smile_detect.detectMultiScale(The_desired_image , scaleFactor= 1.8 , minNeighbors= 20)
for (XCoordinate , YCoordinate , W_Coordinate , H_Coordinate) in smilesS:
    cv2.rectangle(The_desired_image , (XCoordinate ,YCoordinate) , ((XCoordinate + W_Coordinate) ,(YCoordinate + H_Coordinate)) ,
                  (40,20,200) , 3)

cv2.imshow("Smiles Detected By Iman" , The_desired_image)
cv2.waitKey(0)
cv2.destroyAllWindows()