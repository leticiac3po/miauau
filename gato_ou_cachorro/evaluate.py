from keras.models import model_from_json
from keras.optimizers import SGD
import numpy as np
import cv2
import os


# classifies images
def evaluate(path):

	if path != '':
		# prepares the image
		img = cv2.imread(path)
		img = cv2.resize(img,(224,224))
		img = img.astype('float32')
		img = img / 255.
		img = np.expand_dims(img,0)

		# loads the model and weights
		json_file = open('vgg16.json', 'r')
		loaded_model_json = json_file.read()
		json_file.close()
		loaded_model = model_from_json(loaded_model_json)
		loaded_model.load_weights("vgg16.h5")

		# compiles and predicts
		opt = SGD(lr=0.001, momentum=0.9)
		loaded_model.compile(optimizer=opt, loss='binary_crossentropy', metrics=['accuracy'])
		pred = loaded_model.predict(img)

		# organising the output
		percent = np.amax(pred) / (pred[0][0]+pred[0][1])
		index = np.where(pred == percent)
		if pred[0][0] > pred [0][1]:
			lbl = 'cat'
		else:
			lbl = 'dog'
		return percent, lbl
	else:
		return -1
