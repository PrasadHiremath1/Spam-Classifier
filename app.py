import streamlit as st
import pickle
import nltk
import string
from nltk.corpus import stopwords
from nltk.stem.porter import PorterStemmer
from sklearn.feature_extraction.text import TfidfVectorizer



tfidf = pickle.load(open('vectorizer.pkl', 'rb'))
model = pickle.load(open('model.pkl', 'rb'))

st.title("Email/SMS Spam Classifier")

input_sms = st.text_area(
    "Enter the message.."
)

ps = PorterStemmer()

def transformText(text):
    text = text.lower()
    text = nltk.word_tokenize(text)
    y = []
    for i in text:
        if i.isalnum():
            y.append(i)

    text = y[:]
    y.clear()
    for i in text:
        if i not in string.punctuation and i not in stopwords.words('english'):
            y.append(i)

    text = y[:]
    y.clear()

    for i in text:
        y.append(ps.stem(i))
    return " ".join(y)

if st.button('Predict'):
    # preprocess
    transformed_text = transformText(input_sms)
    # vectorize
    vector_input = tfidf.transform([transformed_text])
    # predict
    result = model.predict(vector_input)[0]
    # display
    if result == 1:
        st.header("SPAM")
    else:
        st.header("NOT SPAM")