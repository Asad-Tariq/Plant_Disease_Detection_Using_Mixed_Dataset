# Plant_Disease_Detection_Using_Mixed_Dataset

Implementation of a custom neural network in python using TensorFlow and Keras that is trained and validated on a custom plant disease database.

## The Datasets

The neural network has been trained on a merger of two different datasets:

1. PlantVillage Dataset: An open-source US based, non-profit initiative by Penn State University and the Switzerland based Federal Institute of Technology Lausanne. This dataset consists of around 54,000 images of healthy leaves and disease cases classified by 14 different species (such as apple, blueberry, cherry, orange and others).
2. PlantDoc Dataset: This dataset contains 2,569 images across 13 different plant species and 30 classes (diseased and healthy) for image classification and object detection. There are a total of 8,851 labels. It was originally formed by researchers at the Indian Institute of Technology.

Using these two datasets we have formed our own, which consists of images from both PlantVillage (studio quality images) and PlantDoc (field quality images). In this dataset there are a total of around 56,000 images of 14 different plant species with a ratio of 28:12 for diseased to healthy classes. Each image is of uniform dimension, i.e 256 x 256.
