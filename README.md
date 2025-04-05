# 📧 Spam Classifier - Email/SMS Detection App

This project is a **Streamlit-based web application** that classifies a given message as **SPAM** or **NOT SPAM** using a machine learning model trained on SMS data.

🚀 **Live Demo**: [Click here to use the app](https://spam-classifier-j5dwyghvpewtbsgpgkman8.streamlit.app/)

---

## 🧠 Features

- Preprocessing with NLTK (stopword removal, stemming, tokenization)
- Vectorization using **TF-IDF**
- Spam classification using a **trained machine learning model**
- Simple and interactive **Streamlit UI**
- Model and vectorizer are stored using `.pkl` for fast loading

---

## 🛠 Tech Stack

- **Frontend**: Streamlit
- **Backend**: Python, Scikit-learn
- **NLP Tools**: NLTK
- **Model Persistence**: Pickle
- **Hosting**: Streamlit Cloud

---

## 🔧 How It Works

1. **User inputs** a message (email or SMS).
2. The message is **cleaned and tokenized** using NLTK.
3. The message is transformed into TF-IDF features.
4. The **trained classifier** predicts whether it is SPAM or NOT SPAM.
5. The result is displayed on the screen.

---

## 🖥️ Local Setup
# 1. Clone the repo
git clone https://github.com/PrasadHiremath1/Spam-Classifier.git
cd Spam-Classifier

# 2. Create a virtual environment (optional but recommended)
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# 3. Install dependencies
pip install -r requirements.txt

# 4. Run the Streamlit app
streamlit run app.py
