import tensorflow as tf
import cv2  
from numpy.distutils.tests.test_exec_command import emulate_nonposix
from threading import _enumerate
import numpy as np

fashion_mnist = tf.keras.datasets.fashion_mnist
(train_images, train_labels), (test_images, test_labels) = fashion_mnist.load_data()

class_names = ['T-shirt/top', 'Trouser', 'Pullover', 'Dress', 'Coat',
               'Sandal', 'Shirt', 'Sneaker', 'Bag', 'Ankle boot']

train_images_refine = train_images / 255.0
test_images_refine = test_images / 255.0

model = tf.keras.Sequential([
    tf.keras.layers.Flatten(input_shape=(28, 28)),
    tf.keras.layers.Dense(128, activation='relu'),
    tf.keras.layers.Dense(10, activation='softmax')
])

model.compile(optimizer='adam',
              loss='sparse_categorical_crossentropy',
              metrics=['accuracy'])

model.fit(train_images_refine, train_labels, epochs=1)
img = cv2.imread("baji.jpg",cv2.IMREAD_GRAYSCALE)
 
img28 = cv2.resize(img, dsize=(28,28))

img28_refine = (255-img28)/255.0
img28_refine = img28_refine.reshape((1,28,28))



predictions = model.predict(img28_refine)


print(np.argmax(predictions))

cv2.waitKey()
cv2.destroyAllWindows()

'''
cv2.imshow("grayscale_image",img28)
cv2.waitKey()
cv2.destroyAllWindows()
'''





