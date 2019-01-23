
import numpy as np
import matplotlib.pyplot as plt

# Ce script affiche les images du fichier passé en entré sans les modifiers

array_loaded = np.load ('INSA_Test/test_RGB_0_10_25.npy')
len1=(array_loaded.shape[0])-1


for i in range(0,len1):
	image = np.zeros((32,32,3))	
	image = array_loaded[i]
	plt.imshow(image, alpha=0.75, interpolation='spline36')
	plt.show()
