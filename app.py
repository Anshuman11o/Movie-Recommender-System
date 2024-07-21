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
    
def popularity():
    try:
        # Getting top 5 most popular movies from the whole list
        top_5_popular_movies = movies.nlargest(5, 'popularity')
        popular_titles = []
        popular_posters = []
        for id in top_5_popular_movies['movie_id']:
            popular_titles.append(top_5_popular_movies['title'])
            popular_posters.append(fetch_poster(id))
        return popular_titles, popular_posters
    except:
        st.error("Sorry we ran into some sort of trouble")

def vote_avg():
    try:
        # Getting top 5 best voted movies from the whole list
        top_5_popular_movies = movies.nlargest(5, 'vote_average')
        rated_titles = []
        rated_posters = []
        for id in top_5_popular_movies['movie_id']:
            rated_titles.append(top_5_popular_movies['title'])
            rated_posters.append(fetch_poster(id))
    except:
        st.error("Sorry we ran into some sort of trouble")

movies = load_compressed_pickle('artifacts/movies.pkl.lzma')
similarity = load_compressed_pickle('artifacts/similarity.pkl.lzma')

movie_list = ["None"] + list(movies['title'].values)

option = st.selectbox(
    'Select or type a movie to get recommendation', 
    movie_list
)
typed_movie = st.text_input('Or type a movie name')

# Determine which input to use
if typed_movie:
    selected_movie = typed_movie
elif option != "None":
    selected_movie = option
else:
    selected_movie = None

if st.button('Show recommendation'):
    if selected_movie:
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
    else:
        st.error("Please select or type a movie name.")

if st.button("Most popular"):
    most_popular_titles, most_popular_posters = popularity()
    if most_popular_titles:
            col1, col2, col3, col4, col5 = st.columns(5)
            with col1:
                st.text(most_popular_titles[0])
                st.image(most_popular_posters[0])
            with col2:
                st.text(most_popular_titles[1])
                st.image(most_popular_posters[1])
            with col3:
                st.text(most_popular_titles[2])
                st.image(most_popular_posters[2])
            with col4:
                st.text(most_popular_titles[3])
                st.image(most_popular_posters[3])
            with col5:
                st.text(most_popular_titles[4])
                st.image(most_popular_posters[4])
    else:
        st.error("Sorry we ran into some sort of trouble")

if st.button("Highly rated"):
    highly_rated_titles, highly_rated_posters = popularity()
    if highly_rated_titles:
            col1, col2, col3, col4, col5 = st.columns(5)
            with col1:
                st.text(highly_rated_titles[0])
                st.image(highly_rated_posters[0])
            with col2:
                st.text(highly_rated_titles[1])
                st.image(highly_rated_posters[1])
            with col3:
                st.text(highly_rated_titles[2])
                st.image(highly_rated_posters[2])
            with col4:
                st.text(highly_rated_titles[3])
                st.image(highly_rated_posters[3])
            with col5:
                st.text(highly_rated_titles[4])
                st.image(highly_rated_posters[4])
    else:
        st.error("Sorry we ran into some sort of trouble")
