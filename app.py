import os
import pickle
import streamlit as st
import requests

st.header("Movies Recommendation System Using Machine Learning")

try:
    # Assuming the script is in the same directory as the artifacts folder
    current_directory = os.path.dirname('/Users/anshumanagarwal/Desktop/Anshuman/My projects/Movie recommender system/artifacts')
    movie_list_path = os.path.join(current_directory, 'artifacts/movie_list.pkl')
    similarity_path = os.path.join(current_directory, 'artifacts/similarity.pkl')

except FileNotFoundError as e:
    st.error(f"File not found: {e.filename}")

# Loading the pickled files
movies = pickle.load(open(movie_list_path, 'rb'))
similarity = pickle.load(open(similarity_path, 'rb'))

movie_list = movies['title'].values
st.selectbox(
    'Type or select a movie to get a recommendation',
    movie_list
    )
