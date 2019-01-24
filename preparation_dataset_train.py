import numpy as np
import matplotlib.pyplot as plt

# Ce script permet de copier le dataset train en supprimant les images noires 

array_loaded = np.load ('INSA_Train/train_RGB_0_10_25.npy')
label_loaded = np.load ('INSA_Train/train_label_class.npy')

len1=(array_loaded.shape[0])-1
counter = 0

"""
# la fonction retourne le nombre d'images noires dans la dataset
def images_noires (l1, counter):
	image = np.zeros((32,32,3))
	for line in range (0,l1):
		if (np.count_nonzero(array_loaded[line])==0):
			counter = counter+1
	return counter

# cree un nouveau dataset sans images noires
def create_array (l1,l2, array, label):
	image = np.zeros((32,32,3))
	index = 0
	while(index != (l2-1)):
          for line in range (0,l1):
			if (np.count_nonzero(array_loaded[line])!=0):
				array[index]=image
				label[index]=label_loaded[line]
				index = index + 1
	return array
"""

data1, data2, data3 = np.split(array_loaded, 3)

def images_noires(array):
	index_images_noires = []
	for i in range(0, array.shape[0]):
		if(np.count_nonzero(array[i])==0):
			index_images_noires.append(i)
	return index_images_noires

index_delete1 = images_noires(data1)
index_delete2 = images_noires(data2)
index_delete3 = images_noires(data3)

mask = np.ones(data1.shape[0], dtype=bool)
mask[index_delete1]=False
data1_clean = data1[mask]


"""
# recupere le nb d images noires
result = nb_images_noires(len1,counter)
# si on a detecte des images noires
if (result != 0):
	len2=len1-result
	print("nb d image de la nouvelle array")
	print(len2)
	# creation d'une nouvelle image numpy
	new_array = np.zeros((len2/3, 32,32,3)) 
	new_label = np.zeros((len2/3, 5)) 
	new_array, new_label = create_array (len1,len2/3, new_array, new_label)
	# on la sauve dans un fichier
	np.save('INSA_Train/new_train_RGB.npy', new_array)
	np.save('INSA_Train/new_train_label.npy', new_label)


#sinon
else :
	print("pas d images noires dans le dataset")
"""
