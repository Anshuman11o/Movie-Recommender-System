import lzma
import pickle
import streamlit as st

st.header("Movies Recommendation System Using Machine Learning")

def load_compressed_pickle(file_path):
    with lzma.open(file_path, 'rb') as f:
        return pickle.load(f)

movies = load_compressed_pickle('artifacts/movies.pkl.lzma')
similarity = load_compressed_pickle('artifacts/similarity.pkl.lzma')

movie_list = movies['title'].values
st.selectbox(
    'Type or select a movie to get recommendation', 
    movie_list
)
