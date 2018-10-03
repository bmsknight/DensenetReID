import os
import pickle
from keras import Model
from keras.preprocessing import image
from keras.models import load_model
from keras.applications.densenet import preprocess_input
import numpy as np
from keras_preprocessing.image import ImageDataGenerator

trained_model = load_model('../market_trained_model_epoch5_resnet50.h5')
# trained_model.summary()

feature_extraction_model = Model(trained_model.inputs, trained_model.get_layer("avg_pool").output)
# feature_extraction_model.summary()


test_path = '/home/niruhan/PycharmProjects/DensenetReID/market_for_keras/test/bounding_box_test/'

test_names = os.listdir(test_path)

np.savetxt('test_names_epoch5_resnet50.txt', test_names, fmt='%s')

reid_feature_list = np.empty([19732, 2048])

print 'hi'

for name_index in range(len(test_names)):
    if name_index % 500 == 0:
        print name_index
    img_path = test_path + test_names[name_index]
    img = image.load_img(img_path, target_size=(224, 224))
    img_data = image.img_to_array(img)
    img_data = np.expand_dims(img_data, axis=0)
    img_data = preprocess_input(img_data)

    reid_feature_list[name_index] = feature_extraction_model.predict(img_data)

np.savetxt('gallery_feature_list_epoch5_resnet50.txt', reid_feature_list, fmt='%f')

# for feature in reid_feature_list:
#     dist = np.linalg.norm(feature - reid_feature_list[3])
#     print dist

print 'hi'
