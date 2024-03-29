import streamlit as st
import pickle
import pandas as pd
import requests

def fetch_poster(movie_id):
    response = requests.get('https://api.themoviedb.org/3/movie/{}?api_key=8265bd1679663a7ea12ac168da84d2e8&language=en-US'.format(movie_id))
    data = response.json()
    return "https://image.tmdb.org/t/p/w500" + data['poster_path']

def recommend(movie):
        index = newmovies[newmovies['title'] == movie].index[0]
        newmovie_list = sorted(list(enumerate(similarity[index])), reverse=True, key=lambda x: x[1])

        recommend_movie=[]
        recommend_movie_posters=[]

        for i in newmovie_list[1:6]:
            movie_id = newmovies.iloc[i[0]].movie_id

            recommend_movie.append(newmovies.iloc[i[0]].title)
            #fetching poster
            recommend_movie_posters.append(fetch_poster(movie_id))
        return recommend_movie,recommend_movie_posters

newmovies_dict = pickle.load(open('movies_dict.pkl','rb'))
newmovies = pd.DataFrame(newmovies_dict)
similarity = pickle.load(open('newsimilarity.pkl','rb'))

st.title('Movie Recommendation')

selected_movie_name = st.selectbox(
'How would you like to be contacted?',
newmovies['title'].values)

if st.button('Recommed movies'):
    names,posters = recommend(selected_movie_name)

    col1, col2, col3, col4, col5 = st.columns(5)

    with col1:
        st.text(names[0])
        st.image(posters[0])


    with col2:
        st.text(names[1])
        st.image(posters[1])

    with col3:
        st.text(names[2])
        st.image(posters[2])

    with col4:
        st.text(names[3])
        st.image(posters[3])
    with col5:
        st.text(names[4])
        st.image(posters[4])