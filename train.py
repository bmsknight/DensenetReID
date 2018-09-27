from keras.optimizers import Adam
from keras.preprocessing.image import ImageDataGenerator
from keras.applications.densenet import DenseNet121

train_path = "/home/niruhan/Dataset/market_for_keras/train"
# valid_path = "market/validate"
# test_path = "market/test"

train_batches = ImageDataGenerator().flow_from_directory(train_path, target_size=(224, 224), batch_size=10)

# valid_batches = ImageDataGenerator().flow_from_directory(valid_path, target_size=(224, 224), batch_size=10)

# train_imgs = train_batches.

model = DenseNet121(include_top=True, weights=None, input_shape=(224, 224, 3), classes=751)

model.summary()

model.compile(Adam(lr=0.0001), loss="categorical_crossentropy", metrics=["accuracy"])

model.fit_generator(train_batches, epochs=5, verbose=2)

print 'hi'




