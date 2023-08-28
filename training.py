# tag es el asunto del tema de que tag va la pregunta
# 
import random
import json
# guardar archivos
import pickle
import numpy as np
import nltk

from nltk.stem import WordNetLemmatizer

from keras.models import Sequential
from keras.layers import Dense, Activation, Dropout
from keras.optimizers import SGD

lemmatizer = WordNetLemmatizer()

intents = json.loads(open('intents.json').read())
nltk.download('punkt')
nltk.download("wordnet")
nltk.download('omw-1.4')

words = []
classes = [] # TIPOS DE TAG GUARDO ACÁ
documents = []
ignore_letters = ['?','!', "?", "."]

for intent in intents["intents"]:
    for pattern in intent["patterns"]:
        # Divide el texto en unidades mas pequeñas.
        word_list = nltk.word_tokenize(pattern)
        words.extend(word_list)
        # Pongo cada pregunta con su posible tageo ya tokenizada la oración.
        documents.append((word_list, intent["tag"]))
        if intent["tag"] not in classes:
            classes.append(intent["tag"])
# En words estan todas las palabras que existen.
# Nueva lista con palabras simplificadas

words = [lemmatizer.lemmatize(word) for word in words if word not in ignore_letters]
words = sorted(set(words))

pickle.dump(words, open('words.pkl','wb'))
pickle.dump(classes, open('classes.pkl','wb'))

training = []
output_empty = [0]*len(classes)

# esto tiene las palabras con el tageo, es una tupla.
for document in documents:
    bag = []
    word_patterns = document[0]
    # Convierto lo que estaba tageado ya lematizado.
    word_patterns = [lemmatizer.lemmatize(word.lower()) for word in word_patterns]
    for word in words:
        # Agrego un 1 si la palabra esta en el patron de las palabras o un 0 si no esta.
        bag.append(1) if word in word_patterns else bag.append(0)
    output_row = list(output_empty)
    # A que tag pertenece, donde hay un 1 es la clase a la que pertenece
    output_row[classes.index(document[1])] = 1
    # Agrego a la bolsa de palabra on el tag correspondiente.
    training.append([bag, output_row])

random.shuffle(training)
training = np.array(training)
# Hay 6 listas porque son 6 posibles preguntas. 
print(training)

train_x = list(training[:,0])
train_y = list(training[:,1])

model = Sequential()
model.add(Dense(128, input_shape=(len(train_x[0]),),activation='relu'))
model.add(Dropout(0,5))
model.add(Dense(64, activation='relu'))
model.add(Dropout(0,5))
model.add(Dense(len(train_y[0]), activation='softmax'))
sgd = SGD(learning_rate=0.001, decay=1e-6, momentum=0.9, nesterov=True)
model.compile(loss='categorical_crossentropy', optimizer=sgd, metrics =['accuracy'])
train_process = model.fit(np.array(train_x), np.array(train_y), epochs=100, batch_size=5, verbose=1)
model.save("chatbot_model_h5", train_process)

