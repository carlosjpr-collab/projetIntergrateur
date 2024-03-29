import numpy as np
import matplotlib.pyplot as plt

# Ce script permet de copier le dataset test en supprimant les images noires et le fragmente ensuite en 3 avec les labels

array_loaded = np.load ('INSA_Test/test_RGB_0_10_25.npy')
label_loaded = np.load ('INSA_Test/test_label_class.npy')

len1=(array_loaded.shape[0])-1
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
def create_array (l1,l2, array, label):
	image = np.zeros((32,32,3))
	index = 0
	for line in range (0,l1):
		for i in range(0,32) :
			for j in range(0,32) :
				image[i,j]=array_loaded[line,i,j]
		max = image.max()
		if (max != 0.0):
			array[index]=image
			label[index]=label_loaded[line]
			index = index + 1
	return array, label


# récupère le nb d images noires
result = nb_images_noires(len1,counter)

# si on a detecté des images noires
if (result != 0):
	len2=len1-result
	print("nb d image de la nouvelle array")
	print(len2)
	# création d'une nouvelle image numpy
	new_array = np.zeros((len2, 32,32,3)) 
	new_label = np.zeros((len2, 5)) 
	new_array, new_label = create_array (len1,len2, new_array, new_label)

	# on les sauve dans des fichiers
	np.save('INSA_Test/new_test_RGB.npy', new_array)
	np.save('INSA_Test/new_label.npy', new_label)

	# pour fragmenter en 3 le nouveau dataset
	array1, array2, array3 = np.split(new_array,3)
	# on les sauvegarde
	np.save('INSA_Test/test_image1.npy',array1)
	np.save('INSA_Test/test_image2.npy',array2)
	np.save('INSA_Test/test_image3.npy',array3)
	print('Decoupage du dataset')

	# decoupage des labels
	label1, label2, label3 = np.split(new_label,3)
	np.save('INSA_Test/test_label1.npy',label1)
	np.save('INSA_Test/test_label2.npy',label2)
	np.save('INSA_Test/test_label3.npy',label3)
	print('Decoupage des labels')
	
#sinon
else :
	print("pas d images noires dans le dataset")
