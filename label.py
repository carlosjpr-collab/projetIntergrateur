import numpy as np

# Modifie la nomenclature des labels du dataset de test

label = np.load('test_labels_0_10_25.npy')
#label1 = np.load('test_labels_0_10_25.npy')

for line in range(0,42805):
	index = np.zeros((5))
	index=label[line]
	if (index[0] == 1) :
		label[line, 0] = 1
	if (index[1] == 1) :
		label[line, 1] = 2
	if (index[2] == 1) :
		label[line, 2] = 3
	if (index[3] == 1) :
		label[line, 3] = 4
	if (index[4] == 1) :
		label[line, 4] = 5

np.save('train_label_class.npy', label)

