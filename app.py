import os
import pickle
import streamlit as st

st.header("Movies Recommendation System Using Machine Learning")

# Print current working directory for debugging
current_directory = os.getcwd()
st.write(f"Current working directory: {current_directory}")

# Define the paths to the pickle files
movies_path = '/Users/anshumanagarwal/Desktop/Anshuman/My projects/Movie recommender system/artifacts/movies.pkl'
similarity_path = '/Users/anshumanagarwal/Desktop/Anshuman/My projects/Movie recommender system/artifacts/similarity.pkl'

# Ensure the paths are absolute
movies_path = os.path.abspath(movies_path)
similarity_path = os.path.abspath(similarity_path)

# Print the absolute paths for debugging
st.write(f"Movies path: {movies_path}")
st.write(f"Similarity path: {similarity_path}")

# Load the pickled files
try:
    with open(movies_path, 'rb') as f:
        movies = pickle.load(f)
    with open(similarity_path, 'rb') as f:
        similarity = pickle.load(f)
except FileNotFoundError as e:
    st.error(f"File not found: {e.filename}")

# Ensure movies is loaded before accessing it
if 'movies' in locals():
    movie_list = movies['title'].values
    st.selectbox(
        'Type or select a movie to get a recommendation',
        movie_list
    )
else:
    st.error("Movies data could not be loaded.")
