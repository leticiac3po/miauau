# save the final model to file
from keras.applications.vgg16 import VGG16
from keras.models import Model
from keras.layers import Dense
from keras.layers import Flatten
from keras.optimizers import SGD
from keras.preprocessing.image import ImageDataGenerator

def define_model():

	# loads vgg16 and marks layers as non trainable
	model = VGG16(include_top=False, input_shape=(224, 224, 3))
	for layer in model.layers:
		layer.trainable = False

	# adds new layers
	flat1 = Flatten()(model.layers[-1].output)
	class1 = Dense(128, activation='relu', kernel_initializer='he_uniform')(flat1)
	output = Dense(2, activation='softmax')(class1)
	model = Model(inputs=model.inputs, outputs=output)
	opt = SGD(lr=0.001, momentum=0.9)
	model.compile(optimizer=opt, loss='binary_crossentropy', metrics=['accuracy'])
	return model

# trains, evaluates and saves the model
def run_test_harness():

	model = define_model()
	datagen = ImageDataGenerator(featurewise_center=True)

	# imagenet centering
	datagen = ImageDataGenerator(rescale=1.0/255.0)

	# gets train and test data generators
	train_it = datagen.flow_from_directory('dataset_dogs_vs_cats/train/',
		class_mode='categorical', batch_size=64, target_size=(224, 224))
	test_it = datagen.flow_from_directory('dataset_dogs_vs_cats/test/',
		class_mode='categorical', batch_size=64, target_size=(224, 224))

	# fits and evaluates model
	history = model.fit_generator(train_it, steps_per_epoch=len(train_it),
		validation_data=test_it, validation_steps=len(test_it), epochs=10, verbose=2)
	_, acc = model.evaluate_generator(test_it, steps=len(test_it), verbose=0)
	print('> %.3f' % (acc * 100.0))

	# saves the model
	model_json = model.to_json()
	with open("vgg16_255.json", "w") as json_file:
		json_file.write(model_json)
	model.save_weights("vgg16_255.h5")

run_test_harness()