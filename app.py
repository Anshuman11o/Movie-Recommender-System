import lzma
import pickle
import streamlit as st
import requests

st.header("Movies Recommendation System Using Machine Learning")

def fetch_poster(movie_id):
    url = "https://api.themoviedb.org/3/movie/{}?api_key=84ae8c152d7ace2a5e3a57a50c75caec".format(movie_id)
    data = requests.get(url)
    data = data.json()
    poster_path = data['poster_path']
    full_path = "http://image.tmdb.org/t/p/w500/" + poster_path
    return full_path

def recommend(movie_title):
    try:
        index = movies[movies['title'] == movie_title].index[0]
        distances = sorted(list(enumerate(similarity[index])), reverse=True, key=lambda x: x[1])
        # Distance 1:6 gives out the top 5 movies which match the inputted name
        recommended_movies_name = []
        recommended_movies_poster = []
        for i in distances[1:6]:
            movie_id = movies.iloc[i[0]]['movie_id']
            recommended_movies_poster.append(fetch_poster(movie_id))
            recommended_movies_name.append(movies.iloc[i[0]].title)
        return recommended_movies_name, recommended_movies_poster
    except IndexError:
        st.error("Could not find the movie you were looking for. Try using a more specific name.")
        return [], []
    except Exception as e:
        st.error(f"An error occurred: {e}")
        return [], []

def load_compressed_pickle(file_path):
    with lzma.open(file_path, 'rb') as f:
        return pickle.load(f)

movies = load_compressed_pickle('artifacts/movies.pkl.lzma')
similarity = load_compressed_pickle('artifacts/similarity.pkl.lzma')

movie_list = movies['title'].values
selected_movie = st.selectbox(
    'Type or select a movie to get recommendation', 
    movie_list
)

if st.button('Show recommendation'):
    recommended_movies_name, recommended_movies_poster = recommend(selected_movie)
    if recommended_movies_name:
        col1, col2, col3, col4, col5 = st.columns(5)
        with col1:
            st.text(recommended_movies_name[0])
            st.image(recommended_movies_poster[0])
        with col2:
            st.text(recommended_movies_name[1])
            st.image(recommended_movies_poster[1])
        with col3:
            st.text(recommended_movies_name[2])
            st.image(recommended_movies_poster[2])
        with col4:
            st.text(recommended_movies_name[3])
            st.image(recommended_movies_poster[3])
        with col5:
            st.text(recommended_movies_name[4])
            st.image(recommended_movies_poster[4])
    else:
        st.error("Could not find the movie you were looking for. Try using a more specific name.")
