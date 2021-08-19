import cv2  

img = cv2.imread("test.jpg",cv2.IMREAD_COLOR)

img_crop = img[10:180,150:350]


#print(len(img))
#print(len(img[0]))




cv2.imshow("color_image",img_crop)
cv2.imwrite('ui.jpg', img_crop)

cv2.waitKey(0)
cv2.destroyAllWindows()
