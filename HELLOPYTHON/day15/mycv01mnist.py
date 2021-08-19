import cv2  
import numpy as np

arr2d = [
        [0,255,255,255,0],
        [255,0,0,0,255],
        [255,0,0,0,255],
        [255,0,0,0,255],
        [0,255,255,255,0]
    ]


arr2d_np = np.array(arr2d,dtype=np.uint8)

print(arr2d_np.shape)

cv2.imshow("test_image",arr2d_np)
 
cv2.waitKey(0)
cv2.destroyAllWindows()


'''
# 이미지 윈도우 삭제 
cv2.destroyAllWindows() 
# 이미지 다른 파일로 저장 
cv2.imwrite('test2.png', img)
'''
