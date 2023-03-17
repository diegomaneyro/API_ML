# Importar librerias necesarias
from fastapi import FastAPI
import csv
import pandas as pd



# Inicializa en el objeto app la libreria
app = FastAPI(title='API-ML', description='Api de consulta para peliculas y series en plataformas de streming. \n By Diego Maneyro', version='1.0.1')

# Conexión inicial
@app.get("/")
async def Inicio():
    return {"Test":"API_ML conexión realizada",
            }

# Menu
@app.get("/menu")
async def menu():
    return {"Consultas de API_ML": 
            {"get_max_duration" : "Pelicula con mayor duracion","get_score_count" : "Cantidad de películas por plataforma por puntaje","get_count_plataforma" : "Cantidad de películas por plataforma con filtro de plataforma", "get_actor" : "Actor que más se repite según plataforma y año"}}


# Película con mayor duración con filtros opcionales de AÑO, PLATAFORMA Y TIPO DE DURACIÓN    
@app.get('/get_max_duration/{year}/{platform}/{duration_type}') 
def get_max_duration(year: int = None, platform: str = None, duration_type: str = None):
    df = pd.read_csv('peliculas_final.csv')
    # Aplicar los filtros opcionales al DataFrame
    if year:
        df_filtered = df[df['release_year'] == year]
    else:
        df_filtered = df.copy()
    if platform:
        df_filtered = df_filtered[df_filtered['plataforma'] == platform]
    if duration_type:
        df_filtered = df_filtered[df_filtered['duration_type'] == duration_type]
    # Encontrar la película con mayor duración en el DataFrame filtrado
        max_duration_movie = df_filtered.loc[df_filtered['duration_int'].idxmax()]
    # Retornar la película con mayor duración como un diccionario
    return max_duration_movie.to_dict()  


# Cantidad de películas por plataforma con un puntaje mayor a XX en determinado año
@app.get("/get_score_count/{platform}/{scored}/{year}")
def get_score_count(platform: str, scored: int, year: int):
    df = pd.read_csv('peliculas_final.csv')
    # Filtrar las películas por plataforma, puntaje y año
    df_filtered = df[(df['plataforma'] == platform) & (df['score'] > scored) & (df['release_year'] == year)]
    # Contar el número de películas en el DataFrame filtrado
    count = df_filtered['title'].count()
    # Retornar la cantidad de películas como un diccionario
    return {'count': count}

# Cantidad de películas por plataforma con filtro de plataforma
@app.get("/get_count_plataforma/{platform}")
def get_count_platform(platform: str):
    df = pd.read_csv('peliculas_final.csv')
    # Filtrar las películas por plataforma
    df_filtered = df[df['plataforma'] == platform]
    # Contar el número de películas en el DataFrame filtrado
    count = df_filtered['title'].count()
    # Retornar la cantidad de películas como un diccionario
    return {'count': count}


# Actor que más se repite según plataforma y año. (La función debe llamarse get_actor(platform, year))
@app.get("/get_actor/{platform}/{year}")
def get_actor(platform: str, year: int):
    df = pd.read_csv('peliculas_final.csv')
    # Filtrar las películas por plataforma y año
    df_filtered = df[(df['plataforma'] == platform) & (df['release_year'] == year)]
    # Contar la cantidad de veces que aparece cada actor en el DataFrame filtrado
    actor_counts = df_filtered['cast'].str.split(', ', expand=True).stack().value_counts()
    # Encontrar el actor que más se repite
    actor_most_frequent = actor_counts.index[0]
    # Retornar el actor que más se repite como un diccionario
    return {'actor': actor_most_frequent}


# Datos de contacto 
@app.get("/Autor")
async def Datos_Contacto():
    contacto = {"Nombre":"Diego Maneyro", "email":"diegomaneyro@gmail.com","github":"https://github.com/diegomaneyro"}
    return contacto

