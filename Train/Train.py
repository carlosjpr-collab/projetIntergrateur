#https://machinelearningmastery.com/save-load-keras-deep-learning-models/
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import matplotlib.pylab as plt
import imageio
import tensorflow as tf
print(tf.__version__)

tain_images  = np.load ('INSA_Train/train_RGB_0_10_25.npy')
train_labels = np.load('INSA_Train/train_label.npy')
print(tain_images.shape)
print(train_labels.shape)
class_names = ['urban area', 'agricultural territory', 'forests', 'wetlands' , 'surfaces with water']
'''
plt.figure(figsize=(10,10))
plt.xticks([])
plt.yticks([])
plt.grid(True)

for line in range(0,30):
    image = np.zeros((32,32,3))
    for m in range(0,32) :
        for n in range(0,32) :
            image[m,n]=tain_images[line, m,n]

    plt.subplot(9,4,line+1)
    plt.imshow(image*128, cmap=plt.cm.binary,alpha=0.75, interpolation='spline36')
    plt.xlabel(train_labels[line])
plt.tight_layout()
plt.show()



def plot_image(i, predictions_array, true_label, img):
  predictions_array, true_label, img = predictions_array[i], true_label[i], img[i]
  plt.grid(False)
  plt.xticks([])
  plt.yticks([])

  plt.imshow(img, cmap=plt.cm.binary)

  predicted_label = np.argmax(predictions_array)
  if predicted_label == true_label:
    color = 'blue'
  else:
    color = 'red'

  plt.xlabel("{} {:2.0f}% ({})".format(class_names[predicted_label],
                                100*np.max(predictions_array),
                                class_names[true_label]),
                                color=color)

def plot_value_array(i, predictions_array, true_label):
  predictions_array, true_label = predictions_array[i], true_label[i]
  plt.grid(False)
  plt.xticks([])
  plt.yticks([])
  thisplot = plt.bar(range(10), predictions_array, color="#777777")
  plt.ylim([0, 1])
  predicted_label = np.argmax(predictions_array)

  thisplot[predicted_label].set_color('red')
  thisplot[true_label].set_color('blue')
'''
# Importing the Keras libraries and packages
from keras.models import Sequential
from keras.layers import Convolution2D
from keras.layers import MaxPooling2D
from keras.layers import Flatten
from keras.layers import Dense
# importing
from keras.preprocessing import image

# Initialising the CNN
classifier = Sequential()

# Step 1 - Convolution
classifier.add(Convolution2D(32, 3, 3, input_shape = (32, 32, 3), activation = 'relu'))

# Step 2 - Pooling
classifier.add(MaxPooling2D(pool_size = (2, 2)))

# Adding a second convolutional layer

classifier.add(Convolution2D(32, 3, 3, activation = 'relu'))

classifier.add(MaxPooling2D(pool_size = (2, 2)))

# Step 3 - Flattening
classifier.add(Flatten())

# Step 4 - Full connection
classifier.add(Dense(output_dim = 128, activation = 'relu'))
classifier.add(Dense(output_dim = 5, activation = 'sigmoid'))

# Compiling the CNN
classifier.compile(optimizer = 'adam', loss = 'binary_crossentropy', metrics = ['accuracy'])

# Part 2 - Fitting the CNN to the images
classifier.fit(tain_images[1:100], train_labels[1:100], epochs=5)

#Make predictions
predictions = classifier.predict(tain_images)
print(predictions[1])
print(train_labels[1])

# serialize model to JSON
model_json = classifier.to_json()
with open("Model/classifier.json", "w") as json_file:
    json_file.write(model_json)
# serialize weights to HDF5
model.save_weights("Model/classifier.h5")
print("Saved model to disk Model/*")
