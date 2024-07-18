import pickle
import streamlit as st
import requests

st.header("Movies Recommendation System Using Machine Learning")
movies = pickle.load(open('artifacts/movies_list.pkl', 'rb'))
similarity = pickle.load(open('artifacts/similarity.pkl', 'rb'))


movie_list = movies['title'].values
st.selectbox(
    'Type or select a movie to get a recommendation',
    movie_list
    )
