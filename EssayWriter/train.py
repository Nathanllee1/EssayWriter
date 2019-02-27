import numpy as np
import pandas as pd
from keras.models import Sequential
from keras.layers import Dense
from keras.layers import Dropout
from keras.layers import LSTM
from keras.layers import RNN
from keras.utils import np_utils


#load data
text = (open(r"C:\Users\Nathan Lee\Workspace\EssayWriter\training_data.txt", encoding="utf-8").read())
text = text.lower()

#character word mappings
characters = sorted(list(set(text)))
n_to_char = {n:char for n, char in enumerate(characters)}
char_to_n = {char:n for n, char in enumerate(characters)}

#data preprocessing
x = []
y = []

length = len(text)
seq_length = 100

for i in range(0, length - seq_length, 1):
    sequence = text[i:i + seq_length]
    label = text[i + seq_length]
    x.append([char_to_n[char] for char in sequence])
    y.append(char_to_n[label])

#shape input vectors to fit conv network
X_modified = np.reshape(x, (len(x), seq_length, 1))
X_modified = X_modified / float(len(characters))
Y_modified = np_utils.to_categorical(y)

# set up a model
model = Sequential()
model.add(LSTM(700, input_shape=(X_modified.shape[1], X_modified.shape[2]), return_sequences=True))
model.add(Dropout(0.2))
model.add(LSTM(700))
model.add(Dropout(0.2))
model.add(Dense(Y_modified.shape[1], activation='softmax'))
model.compile(loss='categorical_crossentropy', optimizer='adam')

model.fit(X_modified, Y_modified, epochs=5, batch_size=50)

#save weights
model.save_weights(r'C:\Users\Nathan Lee\Workspace\EssayWriter\models\2.h5')

#load save_weights
model.load_weights(r'C:\Users\Nathan Lee\Workspace\EssayWriter\models\2.h5')

string_mapped = x[99]
# generating characters

string_mapped = X[99]
full_string = [n_to_char[value] for value in string_mapped]
# generating characters
for i in range(400):
    x = np.reshape(string_mapped,(1,len(string_mapped), 1))
    x = x / float(len(characters))

    pred_index = np.argmax(model.predict(x, verbose=0))
    seq = [n_to_char[value] for value in string_mapped]
    full_string.append(n_to_char[pred_index])

    string_mapped.append(pred_index)
    string_mapped = string_mapped[1:len(string_mapped)]


txt=""
for char in full_string:
    txt = txt+char

print(txt)
