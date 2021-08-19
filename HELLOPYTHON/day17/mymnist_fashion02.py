import tensorflow as tf
import cv2  
from numpy.distutils.tests.test_exec_command import emulate_nonposix
from threading import _enumerate

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

model.fit(train_images_refine, train_labels, epochs=10)


for i,img in enumerate(train_images):
    cv2.imwrite("image_train/"+str(train_labels[i])+"_"+str(i)+".jpg",train_images[i])
    
for i,img in enumerate(test_images):
    cv2.imwrite("image_test/"+str(test_labels[i])+"_"+str(i)+".jpg",test_images[i])


cv2.waitKey(0)
cv2.destroyAllWindows()