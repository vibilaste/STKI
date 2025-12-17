# app.py

import pandas as pd
import streamlit as st
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB

# Load dataset
data = pd.read_csv('berita_HOAX_indonesia.csv', sep=';')
data.dropna(inplace=True)
data['kategori'] = data['kategori'].map({'valid': 1, 'hoax': 0})

# Preprocessing
X = data['berita']
y = data['kategori']

# Vectorization
vectorizer = CountVectorizer()
X_vectorized = vectorizer.fit_transform(X)

# Train model
model = MultinomialNB()
model.fit(X_vectorized, y)

# Streamlit app
st.title("Deteksi Berita Hoax")
st.write("Masukkan berita yang ingin Anda periksa:")

# Input text
user_input = st.text_area("Berita:")

if st.button("Deteksi"):
    if user_input:
        # Transform input
        user_input_vectorized = vectorizer.transform([user_input])
        
        # Predict
        prediction = model.predict(user_input_vectorized)
        
        # Display result
        if prediction[0] == 1:
            st.success("Berita ini VALID.")
        else:
            st.error("Berita ini HOAX.")
    else:
        st.warning("Silakan masukkan berita untuk dideteksi.")

# Menambahkan pilihan untuk menampilkan isi dataset
show_data = st.checkbox("Tampilkan Isi Dataset")

if show_data:
    st.write("### Isi Dataset:")
    st.dataframe(data[['berita', 'kategori']])  # Menampilkan seluruh dataset