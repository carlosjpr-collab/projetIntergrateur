import numpy as np
import matplotlib.pyplot as plt

array_loaded = np.load ('INSA_Test/test_RGB_0_10_25.npy')
#(42805, 32, 32, 3)

s1=10701
s2=21402
s3=32103

j=0

image1 = np.zeros((10701, 32,32,3))	
for i in range(0,s1):
	image1[j] = array_loaded[i]
	j = j+1
np.save('image_split1.npy', image1)


j=0
image2 = np.zeros((10701, 32,32,3))	
for i in range(s1,s2):	
	image2[j] = array_loaded[i]
	j = j+1
np.save('image_split2.npy', image2)


j=0
image3 = np.zeros((10701, 32,32,3))
for i in range(s2,s3):	
	image3[j] = array_loaded[i]
	j = j+1
np.save('image_split3.npy', image3)

j=0
image4 = np.zeros((10702, 32,32,3))
for i in range(s3,42805):
	image4[j] = array_loaded[i]
	j = j+1
np.save('image_split4.npy', image4)


