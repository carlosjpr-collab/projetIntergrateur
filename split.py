import numpy as np
import matplotlib.pyplot as plt

array_loaded = np.load ('INSA_Train/train_RGB_0_10_25.npy')


for i in range(0,57073):
	image = np.zeros((57074, 32,32,3))	
	print(image.shape)
	#image[i] = array_loaded[i]
	#np.save('image_split1.npy', image)

for i in range(57074, 114148):
	image = np.zeros((57074, 32,32,3))
	print(image.shape)	
	#image[i] = array_loaded[i]
	#np.save('image_split2.npy', image)

for i in range(114149, 171222):
	image = np.zeros((57074, 32,32,3))
	print(image.shape)	
	#image[i] = array_loaded[i]
	#np.save('image_split3.npy', image)




