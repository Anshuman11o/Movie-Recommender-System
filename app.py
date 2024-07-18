import pickle
import streamlit as st
import requests

st.header("Movies Recommendation System Using Machine Learning")
movies = pickle.load(open('/Users/anshumanagarwal/Desktop/Anshuman/My projects/Movie recommender system/artifacts/movie_list.pkl', 'rb'))
similarity = pickle.load(open('/Users/anshumanagarwal/Desktop/Anshuman/My projects/Movie recommender system/artifacts/similarity.pkl', 'rb'))


movie_list = movies['title'].values
st.selectbox(
    'Type or select a movie to get a recommendation',
    movie_list
    )
