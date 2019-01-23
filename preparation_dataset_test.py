import numpy as np
import matplotlib.pyplot as plt

# Ce script permet de copier le dataset test en supprimant les images noires

array_loaded = np.load ('INSA_Test/test_RGB_0_10_25.npy')

len1=(array_loaded.shape[0])-1
print(len1)
counter = 0

# la fonction retourne le nombre d'images noires dans la dataset
def nb_images_noires (l1, counter):
	image = np.zeros((32,32,3))
	for line in range (0,l1):
		for m in range(0,32) :
			for n in range(0,32) :
				image[m,n]=array_loaded[line, m,n]
		maximum = image.max()
		if (maximum == 0.0):
			counter = counter+1
	return counter

# créé un nouveau dataset sans images noires
def create_array (l1,l2):
	new_array=np.zeros((l2, 32,32,3))
	image = np.zeros((32,32,3))
	index = 0
	for line in range (0,l1):
		for i in range(0,32) :
			for j in range(0,32) :
				image[i,j]=array_loaded[line,i,j]
		max = image.max()
		if (max != 0.0):
			new_array[index]=image
			index = index + 1
	return new_array


# récupère le nb d images noires
result = nb_images_noires(len1,counter)

# si on a detecté des images noires
if (result != 0):
	len2=len1-result
	print("nb d image de la nouvelle array")
	print(len2)
	# création d'une nouvelle image numpy
	new_array = np.zeros((len2, 32,32,3)) 
	new_array = create_array (len1,len2)
	# on la sauve dans un fichier
	np.save('INSA_Test/new_test_RGB.npy', new_array)

#sinon
else :
	print("pas d images noires dans le dataset")


