import pickle
import numpy as np
import tensorflow as tf
from keras.engine.saving import load_model

# ----------------------------------------------------------------------------------------------------------------------

config = tf.compat.v1.ConfigProto()
config.gpu_options.allow_growth = True
config.log_device_placement = True
sess = tf.compat.v1.Session(config=config)
tf.compat.v1.keras.backend.set_session(sess)

# ----------------------------------------------------------------------------------------------------------------------

with open("model/chars.txt", "r", encoding="utf-8") as char_file:
    chars = char_file.read().splitlines()
    char_file.close()
chars.insert(0, "\n")
char_indexes = pickle.load(open("model/char_indexes.pkl", "rb"))
index_char = pickle.load(open("model/index_char.pkl", "rb"))
model = load_model("model/model.h5")


# ----------------------------------------------------------------------------------------------------------------------

def predict(message, size):
    counter = 0
    while size > counter or message[-1] != ".":
        _matrix = np.zeros((1, len(message), len(chars)))
        for _x, _c in enumerate(message):
            _matrix[0, _x, char_indexes[_c]] = 1

        _prob = model.predict(_matrix)[0]
        _prob = np.asarray(_prob).astype("float64")
        _prob = np.log(_prob) / 0.8
        _prob = np.exp(_prob)
        _prob = _prob / np.sum(_prob)
        _prob = np.random.multinomial(1, _prob, 1)
        _char = index_char[np.argmax(_prob)]
        message = message[:] + _char
        counter += 1
    return message
