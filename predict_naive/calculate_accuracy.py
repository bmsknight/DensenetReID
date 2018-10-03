import numpy as np

gallery_features = np.loadtxt('saved/gallery_feature_list_epoch10.txt', dtype = float)
query_features = np.loadtxt('saved/query_reid_feature_list_epoch10.txt', dtype = float)

gallery_names = np.loadtxt('saved/test_names_epoch10.txt', dtype =str)
query_names = np.loadtxt('saved/query_names_epoch10.txt', dtype =str)

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

    query_id = query_names[query_index][0:4]
    gallery_id = gallery_names[min_dist_gallery_index][0:4]

    # print  query_id + "  " + gallery_id

    # if gallery_names[0] == '-':
    #     continue
    if query_names[query_index][0:4] == gallery_names[min_dist_gallery_index][0:4]:
        corrects = corrects + 1
    else:
        errors = errors + 1

print errors
accuracy = corrects / (corrects + errors)