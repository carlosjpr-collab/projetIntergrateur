import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import matplotlib.pylab as plt



array_loaded = np.load ('test_RGB_0_10_25.npy')
#label = np.load('test_labels_0_10_25.npy')


#Finding the value of the max pixel 
def pixel_max (line):
	image = np.zeros((32,32,3))
	for m in range(0,32) :
		for n in range(0,32) :
			image[m,n]=array_loaded[line, m,n]
	max = image.max()
	# red
	#red = image[..., 0].max()
	# green
	#green = image[..., 1].max()
	# blue
	#blue = image[..., 2].max()
	return max


#Improve the colors of the image
def img_improvement (line, max) :
	image = np.zeros((32,32,3))
	for k in range(0,32) :
		for l in range(0,32) :
			image[k,l]=array_loaded[line,k,l]
			#finding the values of RGB
			#r,g,b=image[k,l] 
			np.seterr(divide='ignore', invalid='ignore')
			image[k,l]= image[k,l]/max		
	return image


		
for i in range(0,42805):
#for i in range(0,2000):
	image = np.zeros((32,32,3))
	max = pixel_max(i)
	image = img_improvement(i,max)
	array_loaded[i]=image
	#plt.imshow(array_loaded[i], alpha=0.75, interpolation='spline36')
	#plt.show()

np.save('test.npy', array_loaded)

