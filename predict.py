from keras import Model
from keras.preprocessing import image
from keras.models import load_model
from keras.applications.densenet import preprocess_input
import numpy as np
from keras_preprocessing.image import ImageDataGenerator

# trained_model = load_model('market_trained_model.h5')
#
# trained_model.summary()
#
# # M.inputs, M.get_layer('last_conv').output
# feature_extraction_model = Model(trained_model.inputs, trained_model.get_layer("avg_pool").output)
#
# feature_extraction_model.summary()
#
# # name_list = ['gow.jpg', 'gunes.jpg', 'niru.jpg', 'gow_query.jpg']
# # reid_feature_list = []
# #
# # for name in name_list:
# #     img_path = 'custom_input/' + name
# #     img = image.load_img(img_path, target_size=(224, 224))
# #     img_data = image.img_to_array(img)
# #     img_data = np.expand_dims(img_data, axis=0)
# #     img_data = preprocess_input(img_data)
# #
# #     reid_feature_list.append(feature_extraction_model.predict(img_data))
# #
# # for feature in reid_feature_list:
# #     dist = np.linalg.norm(feature - reid_feature_list[3])
# #     print dist
# #
# # print dist
#
# gallery_path = 'market_for_keras/test'
# query_path = 'market_for_keras/query'
# custom_input_dir = 'custom_input'
#
# gallery_batches = ImageDataGenerator().flow_from_directory(gallery_path, target_size=(224, 224), batch_size=10)
# query_batches = ImageDataGenerator().flow_from_directory(query_path, target_size=(224, 224), batch_size=10)
#
# # test_generator = ImageDataGenerator().flow_from_directory(custom_input_dir, target_size=(224, 224), batch_size=10)
#
# gallery_names = gallery_batches.filenames
# query_names = query_batches.filenames
#
# np.savetxt('gallery_names.txt', gallery_names, fmt='%s')
# np.savetxt('query_names.txt', query_names, fmt='%s')
#
#
# a = query_names[10][13:17]
# b = gallery_names[1000][18:22]
#
# gallery_features = feature_extraction_model.predict_generator(gallery_batches)
# query_features = feature_extraction_model.predict_generator(query_batches)
#
# np.savetxt('gallery_features.txt', gallery_features, fmt='%f')
# np.savetxt('query_features.txt', query_features, fmt='%f')





gallery_features = np.loadtxt('gallery_features.txt', dtype = float)
query_features = np.loadtxt('query_features.txt', dtype = float)

gallery_names = np.loadtxt('gallery_names.txt', dtype =str)
query_names = np.loadtxt('query_names.txt', dtype =str)

corrects = 0.0
errors = 0.0

for query_index in range(len(query_features)): # len(query_features)
    if query_index % 500 == 0:
        print query_index
        accuracy = corrects / (corrects + errors + 1)
        print accuracy

    # print accuracy
    min_distance = float('inf')
    min_dist_gallery_index = -1

    for gallery_index in range(len(gallery_features)):
        current_distance = np.linalg.norm(gallery_features[gallery_index] - query_features[query_index])

        if current_distance < min_distance:
            min_distance = current_distance
            min_dist_gallery_index = gallery_index

    query_id = query_names[query_index][13:17]
    gallery_id = gallery_names[min_dist_gallery_index][18:22]

    # print  query_id + "  " + gallery_id

    # if gallery_names[18] == '-':
    #     continue
    if query_names[query_index][13:17] == gallery_names[min_dist_gallery_index][18:22]:
        corrects = corrects + 1
    else:
        errors = errors + 1

print errors
accuracy = corrects / (corrects + errors)

# print accuracy


