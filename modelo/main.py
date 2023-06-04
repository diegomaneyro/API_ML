# -*- coding: utf-8 -*-
"""
modelo de recomendacion de peliculas usando el alroritmo de prediccion SVD de surprise

Autor: Diego Maneyro
version: 1.0.0
"""
# importar librerias necesarias
from surprise import Dataset, Reader, SVD
from surprise.model_selection import train_test_split
import pandas as pd
from fastapi import FastAPI



# Inicializa en el objeto app la libreria
app = FastAPI(title='Modelo_Recomendacion', description='Api_recomendacion_peliculas', version='1.0.0')


@app.get("/")
async def Inicio():
    return {'Test':{"Modelo_Recomendacion":"Conexión realizada"}}


# ingesta de datos
rating_url = ("https://drive.google.com/file/d/17A-JGJ8qevofrLmYhWUTcPHmnTr_vZQ4/view?usp=share_link")
peliculas_url = ("https://github.com/diegomaneyro/API_ML/blob/main/peliculas_final.csv")

df_scores = pd.read_csv(rating_url, usecols=['userId','score','movieId'])
df_movie = pd.read_csv(peliculas_url, usecols=['id','title'])
df_movie = df_movie.reset_index(drop=True)

limite = 205000
reader = Reader(rating_scale=(1,5))
data = Dataset.load_from_df(df_scores[['userId', 'movieId','score']][:limite], reader)

# Dividir los datos en conjuntos de entrenamiento y prueba
trainset, testset = train_test_split(data, test_size=0.3, random_state=42)

# Entrenar un modelo SVD
model = SVD(n_factors=50, lr_all=0.005, reg_all=0.02, n_epochs=100)
model.fit(trainset)


# funcion de recomendacion
@app.get("/get_movieId/")
def recomendacion_pelicula(userId, movieId: str):
    # Hacer predicciones para un usuario específico
    user_id = userId
    movies_watched_by_user = df_scores[df_scores['userId'] == user_id]['movieId'].tolist()
    unseen_movies_by_user = df_scores[~df_scores['movieId'].isin(movies_watched_by_user)]['movieId'].tolist()
    testset = [[user_id, movie_id, 4] for movie_id in unseen_movies_by_user]
    predictions = model.test(testset)

    # Obtener las 5 películas más recomendadas
    top_n = 5
    recommended_movies = []
    for uid, iid, _, est, _ in predictions:
        recommended_movies.append((iid, est))
    recommended_movies.sort(key=lambda x: x[1], reverse=True)
    recommended_movies = recommended_movies[:top_n]

    # Obtener los títulos de las películas recomendadas
    recommended_movies_titles = df_movie[df_movie['id'].isin([x[0] for x in recommended_movies])]['title'].tolist()

    print('Las películas recomendadas para el usuario {} son:'.format(user_id))
    for i, movie_title in enumerate(recommended_movies_titles):
        peliculas_lis = '{}. {}'.format(i+1, movie_title).to_list()
          
    return {'peliculas recomendadas:': peliculas_lis}
