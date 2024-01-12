from keras.models import load_model
import tensorflow as tf

model = load_model("model.h5")

converter = tf.lite.TFLiteConverter.from_keras_model(model)
tflite = converter.convert()

print("model Converted")

with open('model41.tflite','wb')as f:
    f.write(tflite)