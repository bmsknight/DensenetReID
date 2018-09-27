import os
import shutil

dataset_directory = '/home/niruhan/Dataset/market/bounding_box_train'
dirs = os.listdir(dataset_directory)

for image_name in dirs:
    a = image_name[0:4]
    out_dir = "market/" + a

    # print os.path.exists(out_dir)

    if not os.path.exists(out_dir):
        os.makedirs(out_dir)

    shutil.copy(dataset_directory + "/" + image_name, out_dir + "/" + image_name)

print "hi"

# shutil.move(dataset_directory + "/" + dirs[0], a + "/" + dirs[0])

