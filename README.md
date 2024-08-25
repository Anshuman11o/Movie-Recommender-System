Movie Recommender System (Link: https://movie-recommender-system-11o-7fec3d4e884a.herokuapp.com/)

Built a movie recommender web app using Python Jupyter. This app displays top 5 movies from the TMDB database using content based filtering. 
User can input a movie title and can get 5 movie recommendations as output. These recommendations are generated using cosine similarity, hence the recommendations will be similar to the input movie.
Additionally, users can also generate and see the most popular and highly rated movies of all time based present in the database.

Cleaning and processing the database, programming the cosine similarity search algorithm, and building the other functionalites were all completed in Jupyter notebook using Python.
The web application was designed using Streamlit and Git. The final software was launched using Heroku.

The search functionality works on cosine similarity, as it is one of the most common search functionality metric for movie search.
The search basically generates a similarity index for each movie based on the words and contents of its tags and the words used in the search by the user.
Then it gets the top 5 similar movie which basically had the least cosine distance in their indexes.

Python Jupyter notebook was used to filter out important fields from the movie databse. After retrieving all the relevant fields I converted them into tags.
Moreover, I used Jupyter notebook to build my search algorithm and was able to test it using the TMDB data in the notebook. 
Similarly I built the most popular and highly rated movies generation functionalities.
Finally, using Jupyter notebook I was able to run a lot of tests and was able to check if the data was as expected before starting the desing part in Streamlit.

Web application was then desgined using Streamlit and was connected through Git. Deployment was conducted using Heroku.

Final application was tested and adjustments were made depending on user feedbacks.
