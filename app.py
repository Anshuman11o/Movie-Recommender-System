import os
import pickle
import streamlit as st
import requests

st.header("Movies Recommendation System Using Machine Learning")

try:
    movies = pickle.load(open('/Users/anshumanagarwal/Desktop/Anshuman/My projects/Movie recommender system/artifacts/movies.pkl', 'rb'))
    similarity = pickle.load(open('/Users/anshumanagarwal/Desktop/Anshuman/My projects/Movie recommender system/artifacts/similarity.pkl', 'rb'))

except FileNotFoundError as e:
    st.error(f"File not found: {e.filename}")

movie_list = movies['title'].values
st.selectbox(
    'Type or select a movie to get a recommendation',
    movie_list
)
