from keras import Model, Sequential, Input
from keras.layers import Conv2D, GlobalAveragePooling2D, Dense
from keras.optimizers import Adam
from keras.preprocessing.image import ImageDataGenerator
from keras.applications.densenet import DenseNet121
from keras.applications.resnet50 import ResNet50

train_path = "/home/niruhan/Dataset/market_for_keras/train"
# valid_path = "market/validate"
# test_path = "market/test"

train_batches = ImageDataGenerator().flow_from_directory(train_path, target_size=(224, 224), batch_size=10)

# valid_batches = ImageDataGenerator().flow_from_directory(valid_path, target_size=(224, 224), batch_size=10)

# train_imgs = train_batches.

model = ResNet50(include_top=True, weights=None, input_shape=(224, 224, 3), classes=751)

model.summary()

# input_tensor = Input(shape=(224,224,3))
#
# popped_model = Model(model.inputs, model.get_layer("conv5_block16_concat").output)
#
# x = popped_model(input_tensor)
#
# x = Conv2D(512, (7, 7), activation='relu')(x)
#
# # x = layers.GlobalAveragePooling2D(name='avg_pool')(x)
# # x = layers.Dense(classes, activation='softmax', name='fc1000')(x)
# x = GlobalAveragePooling2D(name='my_avg_pool')(x)
# x = Dense(751, activation='softmax', name='fc751')(x)
# my_model = Model(input_tensor, x)
#
# my_model.summary()
#
# # a = my_model.layers
#
# # b = Sequential()
# # for layer in my_model.layers:
# #    b.add(layer)
#
# # b.summary()

model.compile(Adam(lr=0.0001), loss="categorical_crossentropy", metrics=["accuracy"])

model.fit_generator(train_batches, epochs=5, verbose=2)

print 'hi'




