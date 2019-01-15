import numpy as np
import matplotlib.pyplot as plt

array_loaded = np.load ('test.npy')
print(array_loaded.shape)

"""
for i in range(0,42805):
#for i in range(0,2000):
	image = np.zeros((32,32,3))	
	image = array_loaded[i]
	plt.imshow(image, alpha=0.75, interpolation='spline36')
	plt.show()
"""
