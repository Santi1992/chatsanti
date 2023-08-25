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
classes = []
documents = []
ignore_letters = ['?','!', "?", "."]

for intent in intents["intents"]:
    for pattern in intent["patterns"]:
        # Divide el texto en unidades mas pequeñas.
        word_list = nltk.word_tokenize(pattern)
        words.extend(word_list)
        # Pongo cada pregunta con su posible tageo ya tokenizada la oración.
        documents.append((word_list, intent["tag"]))
