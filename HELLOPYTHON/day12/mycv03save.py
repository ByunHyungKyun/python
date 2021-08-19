import cv2  

img = cv2.imread("test.jpg",cv2.IMREAD_COLOR)
cv2.imshow("color_image",img)
 
gray_img = cv2.imread("test.jpg",cv2.IMREAD_GRAYSCALE)
cv2.imshow("grayscale_image",gray_img)
 
cv2.imwrite("gray_lena.tif",gray_img)
cv2.waitKey()

'''
# 이미지 윈도우 삭제 
cv2.destroyAllWindows() 
# 이미지 다른 파일로 저장 
cv2.imwrite('test2.png', img)
'''
