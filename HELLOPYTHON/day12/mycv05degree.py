import cv2  

img = cv2.imread("test.jpg",cv2.IMREAD_COLOR)

height, width, channel = img.shape
matrix = cv2.getRotationMatrix2D((width/2, height/2), 10, 1)
dst = cv2.warpAffine(img, matrix, (width, height))


cv2.imshow("color_image",dst)
cv2.waitKey(0)
cv2.destroyAllWindows()
