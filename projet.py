import numpy as np
import matplotlib.pyplot as plt


# Ce script permet d'afficher les images en modifiant les couleurs


#array_loaded = np.load ('INSA_Test/test_RGB_0_10_25.npy')
array_loaded = np.load ('INSA_Test/test_image2.npy')
len1=(array_loaded.shape[0])-1


# Trouve la valeur max des pixels 
def pixel_max (line):
	image = np.zeros((32,32,3))
	for m in range(0,32) :
		for n in range(0,32) :
			image[m,n]=array_loaded[line, m,n]
	max = image.max()
	return max


# Ameliore les couleurs de l image
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



# Appel des fonctions	
for i in range(0,len1):
	image = np.zeros((32,32,3))
	max = pixel_max(i)
	image = img_improvement(i,max)
	array_loaded[i]=image
	plt.imshow(array_loaded[i], alpha=0.75, interpolation='spline36')
	plt.show()

	# on sauve les nouvelles images dans un fichier
	#np.save('INSA_Test/test.npy', array_loaded)
