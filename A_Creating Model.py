from pickle import dump
from keras.layers import Dense, LSTM, Embedding
from keras.models import Sequential
from keras.utils import to_categorical
import numpy as np
import math
from keras.preprocessing.text import Tokenizer

import spacy
import os
import re
from tensorflow.python.keras.backend import categorical_crossentropy

os.system('clear')

nlp = spacy.load('en')
file = open(
    '/home/tanmay/Desktop/NLP Workflow/Working with a big data/collected_data.txt', 'r')
minidata = file.readline()
club = [text.lower() for text in re.findall('[A-Za-z]+', minidata)]


# using the tokenizer
tk = Tokenizer(num_words=len(club), lower=True)
tk.fit_on_texts(club)
sequence = tk.texts_to_sequences(club)

# making the 2D matrix
training_length = math.trunc(math.sqrt(len(sequence)))

new_Matrix = []
for i in range(training_length, len(sequence)):
    row = sequence[i-training_length:i]
    new_Matrix.append(row)
Matrix = np.array(new_Matrix)

vocabulary_size = len(club)
X = Matrix[:, :-1]
y = Matrix[:, -1]
y = to_categorical(y, num_classes=vocabulary_size + 1)
seq_len = X.shape[1]


def create_model(vocab_Size, seq_Len):
    model = Sequential()
    model.add(Embedding(vocab_Size, seq_Len, input_length=seq_Len))
    model.add(LSTM(seq_Len*2, return_sequences=True))
    model.add(LSTM(seq_Len*2))
    model.add(Dense(seq_Len*2, activation='relu'))
    model.add(Dense(vocab_Size, activation='softmax'))

    model.compile(loss='categorical_crossentropy',
                  optimizer='adam', metrics=['accuracy'])
    print("Summary :-")
    print(model.summary())
    return model


model = create_model(vocabulary_size + 1, seq_len)

model.fit(X, y, batch_size=128, verbose=2, epochs=3)

model.save('/home/tanmay/Desktop/NLP Workflow/LSTM/PickleFile/Training sample.h5')
dump(tk, open('/home/tanmay/Desktop/NLP Workflow/LSTM/PickleFile/Training sample.h5', 'wb'))


pickle_out = open("/home/tanmay/Desktop/NLP Workflow/LSTM/PickleFile/X.pickle", 'wb')
dump(X, pickle_out)
pickle_out.close()


pickle_out = open("/home/tanmay/Desktop/NLP Workflow/LSTM/PickleFile/y.pickle", "wb")
dump(y, pickle_out)
pickle_out.close()
