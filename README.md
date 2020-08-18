# MIAUAU
Django web application that classifies submitted images as cats or dogs.
## The dataset
https://www.kaggle.com/c/dogs-vs-cats/data?select=train.zip

Dogs vs. Cats was used in a competition. The test.zip file isn't labeled, so only the train.zip file was used. It contains 25,000 images of cats and dogs.

To preprocess it for the data generator, have train.zip extracted in the same folder as prep.py. The algorithm will separate the images into train and test folders, and then further separate them into cats and dogs. 25% of the data was used in testing and 75% in training.
## The model
It's a VGG-16 model pre-trained on ImageNet, with the top removed and two dense layers added. Only the new layers are trainable. It's included in the vgg16.py file, but there's no need to run it. The evaluate.py file loads the trained model and evaluates samples, returning the label and its corresponding probability.
## The application
It contains three views. One for submitting the image, one for displaying the results and a gallery that showcases all the previous results in chronological order. They refer to evaluate.py to classify the images.
