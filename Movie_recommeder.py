import streamlit as st
import pickle
import pandas as pd
import requests
movies_dict = pickle.load(open('movies.pkl','rb'))
movies = pd.DataFrame(movies_dict)
similarity=pickle.load(open('similarity.pkl','rb'))
# def fetch_poster (movie_id):
#     responce=requests.get('https://api.themoviedb.org/3/movie/{ }?api_key=2ea0429a3f4de0f5b90e7cd63c01bf86&language=en-US'.format(movie_id))
#     data=responce.json()
#     pos = "https://image.tmdb.org/t/p/w500/" + data['poster_path']
#     return pos                                                                                                                               ))

def recommend(movie):
    movie_ind = movies[movies['title'] == movie].index[0]
    distance = similarity[movie_ind]
    recomdded_movies = sorted(list(enumerate(distance)), reverse=-1, key=lambda x: x[1])[1:6]
    movie_list=[]
    poster=[]
    for i in recomdded_movies:
        movie_id=movies.iloc[i[0]].movie_id
        movie_list.append(movies.iloc[i[0]].title)
        responce = requests.get(
            'https://api.themoviedb.org/3/movie/{}?api_key=2ea0429a3f4de0f5b90e7cd63c01bf86&language=en-US'.format(
                movie_id))
        data=responce.json()
        poster.append("https://image.tmdb.org/t/p/w500/" + data['poster_path'])
    return movie_list,poster

st.title("Movie recommendation system ")
selected_movie = st.selectbox('Enter Movie Name here: ',movies['title'].values)
if st.button('Recommend'):
    recommendation,posters =recommend(selected_movie)
    col1, col2, col3,col4,col5 = st.columns(5)
    with col1:
        st.text(recommendation[0])
        st.image(posters[0],use_column_width=True)
    with col2:
        st.text(recommendation[1])
        st.image(posters[1],use_column_width=True)
    with col3:
        st.text(recommendation[2])
        st.image(posters[2],use_column_width=True)
    with col4:
        st.text(recommendation[3])
        st.image(posters[3],use_column_width=True)
    with col5:
        st.text(recommendation[4])
        st.image(posters[4],use_column_width=True)

