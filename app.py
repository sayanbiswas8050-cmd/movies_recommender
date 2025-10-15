import streamlit as st
import pickle
import pandas as pd
import requests

# 8.collect movies image thorough the API keys and movies id
def fetch_movies_poster(movie_id):
    response = requests.get("https://api.themoviedb.org/3/movie/{}?api_key=69165607e15ec37b615c342efa2eaf77&language=en-US".format(movie_id))
    data = response.json()
    return "http://image.tmdb.org/t/p/w500/" + data["poster_path"]

# 2.movies recommender function 
def recommend(movie):
    # 3.collect selected movie index
    movie_index = movies[movies["title"]== movie].index[0]
    # 4.similar movies distance collect thourgh the selected movie index
    distance = similarity[movie_index]
    # 5.store top 5 similar movies list
    movies_list = sorted(list(enumerate(distance)),reverse = True,key=lambda x:x[1])[1:6]
    
    # 6. separate all 5 movies and collect movies title , id 
    recommended_movies = []
    recommended_movies_poster = []
    for i in movies_list:

       recommended_movies.append(movies.iloc[i[0]].title)
       
       movie_id = movies.iloc[i[0]].id
       # 7.fetch poster from API
       recommended_movies_poster.append(fetch_movies_poster(movie_id))
    # 9.return all of them 
    return recommended_movies,recommended_movies_poster

# load similarity.pkl file , movies_dict
similarity= pickle.load(open("similarity.pkl","rb"))
movies_dict = pickle.load(open("movies_dict.pkl","rb"))


st.title("Movies Recommender System")
# 1. movie select box
movies = pd.DataFrame(movies_dict)
selected_movie_name= st.selectbox("Select Movies", movies["title"].values)

# 10.recommend button
if st.button("Recommend"):
    
    names, posters = recommend(selected_movie_name)
    
#     col1, col2, col3, col4, col5 = st.columns(5)
    
#     with col1:
#            st.write(names[0])
#            st.image(posters[0])
    
#     with col2:
#            st.write(names[1])
#            st.image(posters[1])
    
#     with col3:
#            st.write(names[2])
#            st.image(posters[2])
    
#     with col4:
#            st.write(names[3])
#            st.image(posters[3])
    
#     with col5:
#            st.write(names[4])
#            st.image(posters[4])
      
    cols = st.columns(5)
    for col ,i in zip(cols,range(0,5)):
        with col:
            st.write(names[i])
            st.image(posters[i])
            


    
        
