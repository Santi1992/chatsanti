import random
import json
import pickle
import numpy as np
import nltk
from nltk.stem import WordNetLemmatizer
from keras.models import load_model

lemmatizer = WordNetLemmatizer()
intents = json.loads(open('intents.json').read())

# Todas las palabras lemattizadas tengo acá
words = pickle.load(open("words.pkl", 'rb'))
# Aca tengo todos los tipos de tags o clases posible de respuesta.
classes = pickle.load(open("classes.pkl", 'rb'))

model = load_model('chatbot_model_h5')

def clean_up_sentence(sentence):
    sentence_words = nltk.word_tokenize(sentence)
    sentence_words = [lemmatizer.lemmatize(word) for word in sentence_words]
    return sentence_words

def bag_of_words(sentence):
    sentence_words = clean_up_sentence(sentence)
    bag = [0]*len(words) # De todas las palabras donde tengo pongo un 1.
    for w in sentence_words:
        for i,word in enumerate(words):
            if word == w:
                bag[i]=1
    return np.array(bag)


def predict_class(sentence):
    bow = bag_of_words(sentence)
    # Devuelve probabilidad de que pertenezca a cada categoria
    res = model.predict(np.array([bow]))[0]
    # Dame el indice que tiene más probabilidad
    max_index = np.where(res == np.max(res))[0][0]
    category = classes[max_index]
    # Me quede con el máximo de la clase.
    return category

def get_response(tag, intents_json):
    list_of_intents = intents_json['intents']
    result = ""
    for i in list_of_intents:
        if i["tag"]==tag:
            result = random.choice(i['responses'])
            break
    return result

while True:
    message = input("")
    ints= predict_class(message)
    res = get_response(ints, intents)
    print(res)

