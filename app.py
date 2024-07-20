import os
import pickle
import streamlit as st

st.header("Movies Recommendation System Using Machine Learning")


movies = pickle.load(open('artifacts/movies.pkl.lzma', 'rb'))
similarity = pickle.load(open('artifacts/similarity.pkl.lzma', 'rb'))
movie_list = movies[ 'title'].values
st.selectbox(
    'Type or select a movie to get recommendation', 
    movie_list
)
