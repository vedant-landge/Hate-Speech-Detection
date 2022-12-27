import emoji
import pickle
from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.stem import LancasterStemmer
from nltk.stem import WordNetLemmatizer
import re
import pandas as pd
import numpy as np
import tensorflow as tf
from sklearn.feature_extraction.text import CountVectorizer, TfidfVectorizer,TfidfTransformer
import logging
tf.get_logger().setLevel(logging.ERROR)



from nltk.corpus import stopwords

STOPWORDS = stopwords.words('english')
STOPWORDS.append("rt")
STOPWORDS.append("<user>")
STOPWORDS.append("<url>")


def stemSentence(sentence):
    lemmatizer = WordNetLemmatizer()
    stemmer = LancasterStemmer()
    words=word_tokenize(sentence)
    stem_sentence=[]
    for word in words:
        stem_sentence.append(lemmatizer.lemmatize(word))
        stem_sentence.append(" ")
    return "".join(stem_sentence)

def clean_text(sentence):
    sentence = sentence.lower()
    sentence = re.sub('(@[^\s]+)|(#[^\s]+)', '', sentence)
    sentence = re.sub('((www\.[^\s]+)|(https?://[^\s]+))','',sentence)
    sentence = re.sub(r'[ ]+', ' ', sentence)
    words = word_tokenize(sentence)
    words = [word for word in words if not word in STOPWORDS]
    clean_sentence=[]
    for word in words:
        clean_sentence.append(" ")
    return "".join(clean_sentence)


def emoticon(sentence):
    words=word_tokenize(sentence)
    stem_sentence=[]
    for word in words:
        if emoji.demojize(word)== None:
            stem_sentence.append(word)
            stem_sentence.append(" ")
        else:
            word= emoji.demojize(word)
            word = word.replace(":"," ")
            stem_sentence.append(word)
            stem_sentence.append(" ")
    return "".join(stem_sentence)


#model pickle file

model = pickle.load(open('hate_speech.pickle', 'rb'))

#tfidf vectorizer pickle file

vectorizer = pickle.load(open('tfidf.pickle', 'rb'))

sentence = input("sentence: ")
sentence=emoticon(sentence)
stemmed = stemSentence(sentence)
sentence=[stemmed]
sentence = vectorizer.transform(sentence)
print('normal' if model.predict(sentence)==1 else 'hateful')



