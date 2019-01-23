import numpy as np

# Modifie la nomenclature des labels du dataset de test et train

label_train = np.load('INSA_Train/train_labels_0_10_25.npy')
label_test = np.load('INSA_Test/test_labels_0_10_25.npy')

for line in range(0,42805):
	index = np.zeros((5))
	index=label_train[line]
	if (index[0] == 1) :
		label_train[line, 0] = 1
	if (index[1] == 1) :
		label_train[line, 1] = 2
	if (index[2] == 1) :
		label_train[line, 2] = 3
	if (index[3] == 1) :
		label_train[line, 3] = 4
	if (index[4] == 1) :
		label_train[line, 4] = 5

np.save('INSA_Train/train_label_class.npy', label_train)

for line in range(0,42805):
	image = np.zeros((5))
	image=label_test[line]
	if (image[0] == 1) :
		label_test[line, 0] = 1
	if (image[1] == 1) :
		label_test[line, 1] = 2
	if (image[2] == 1) :
		label_test[line, 2] = 3
	if (image[3] == 1) :
		label_test[line, 3] = 4
	if (image[4] == 1) :
		label_test[line, 4] = 5

np.save('INSA_Test/test_label_class.npy', label_test)

