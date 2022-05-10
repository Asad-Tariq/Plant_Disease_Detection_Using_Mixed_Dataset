import numpy as np
import pickle
import cv2
from keras.preprocessing.image import img_to_array

default_image_size = tuple((256, 256))

def convert_image_to_array(image_dir):
    try:
        image = cv2.imread(image_dir)
        if image is not None:
            image = cv2.resize(image, default_image_size)
            return img_to_array(image)
        else:
            return np.array([])
    except Exception as e:
        print(f"Erorr : {e}")
        return None

model_pickle = open(r'/home/at05439/Documents/cnn_model.pkl', 'rb')
model = pickle.load(model_pickle)

label_encoder = open(r'/home/at05439/Documents/label_transform.pkl', 'rb')
label_transformer = pickle.load(label_encoder)

test_image_path = "/home/at05439/Documents/grape_esca.JPG"
imar = convert_image_to_array(test_image_path)
npimagelist = np.array([imar], dtype=np.float16) / 255.0
pred = model.predict(npimagelist)

print(label_transformer.inverse_transform(pred))
