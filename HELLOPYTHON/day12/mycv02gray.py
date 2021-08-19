import cv2  

img = cv2.imread("test.jpg",cv2.IMREAD_COLOR)
cv2.imshow("color_image",img)
cv2.waitKey()


cv2.imwrite('ui.jpg', img)

