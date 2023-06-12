# importar librerias necesarias
from surprise import Dataset, Reader, SVD
from surprise.model_selection import train_test_split
from surprise import dump
import pandas as pd

# importar datos
df_movie = pd.read_csv("../datos/csvs/peliculas/peliculas_final.csv", sep=',', usecols=['id', 'title'])
df_scores = pd.read_csv("../datos/csvs/ratings/ratings_final.csv", sep=',', usecols=['userId', 'score', 'movieId'])
df_movie = df_movie.reset_index(drop=True)

# Crear un objeto Reader para analizar los datos de entrada
reader = Reader(rating_scale=(1.0, 5.0))

# Limitar los datos para evitar overfitting durante el aprendizaje
limite = 205000
data = Dataset.load_from_df(df_scores[['userId', 'movieId', 'score']][:limite], reader)

# Dividir los datos en conjuntos de entrenamiento y prueba
trainset, testset = train_test_split(data, test_size=0.3, random_state=42)

# Entrenar un modelo SVD
n_factors = 30
n_epochs = 80
lr_all = 0.005
reg_all = 0.02
model = SVD(n_factors=n_factors, lr_all=lr_all, reg_all=reg_all, n_epochs=n_epochs)
model.fit(trainset)

# Guardar el modelo entrenado en un archivo
model_file = 'modelo_entrenado.pkl'
dump.dump(model_file, algo=model)