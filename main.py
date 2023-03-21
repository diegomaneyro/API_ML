# importar librerias
from fastapi import FastAPI
import pandas as pd

# Cargar el archivo CSV como un DataFrame de Pandas
df = pd.read_csv("https://github.com/diegomaneyro/API_ML/raw/main/peliculas_final.csv")

# Inicializa en el objeto app la libreria
app = FastAPI(title='API-ML', description='Api de consulta para peliculas y series en plataformas de streming. \n By Diego Maneyro', version='1.0.2')

# Crear la columna 'platform'
df['platform'] = df['id'].str[0]

# Conexión inicial
@app.get("/")
async def Inicio():
    return {"API_ML":{"Test":"API_ML conexión realizada"}}


# Definir la ruta y la función correspondiente para obtener la película con mayor duración
@app.get("/max_duration/")
def get_max_duration(year: int = None, platform: str = None, duration_type: str = None):
    if platform=='netflix':
        platform='n'
    if platform=='amazon':
        platform='a'
    if platform=='hulu':
        platform='h'
    if platform=='disney':
        platform='d'
     # Filtrar por año, plataforma y tipo de duración si se especifican
    if year:
        df_filtered = df[df['release_year'] == year]
    else:
        df_filtered = df
    if platform:
        df_filtered = df_filtered[df_filtered['platform'] == platform]
    if duration_type:
        df_filtered = df_filtered[df_filtered['duration_type'] == duration_type]

    # Encontrar la película con la duración máxima
    max_duration = df_filtered[df_filtered['duration_int'] == df_filtered['duration_int'].max()]

    # Retornar el título y la duración de la película como un diccionario
    return max_duration[['title', 'duration_int']].to_dict('records')
    

# Definir la ruta y la función correspondiente para obtener la cantidad de películas por plataforma con un puntaje mayor a XX en determinado año
@app.get("/score_count/")
def get_score_count(platform: str, scored: str, year: int):
    if platform=='netflix':
        platform='n'
    if platform=='amazon':
        platform='a'
    if platform=='hulu':
        platform='h'
    if platform=='disney':
        platform='d'
    score_count = df.copy()
    
    # Obtener las películas de la plataforma y del año ingresados por parámetro
    score_count = score_count[(score_count["id"].str[0].str.lower() == platform.lower()) & (score_count["release_year"] == year)]
    
    # Obtener la cantidad de películas con el puntaje mayor al ingresado por parámetro
    score_count = score_count[score_count["rating"] >= scored]
    count = len(score_count)
    
    # Retornar la cantidad de películas
    return {"scored": scored, "año": year, "cantidad de peliculas": count}

# Definir la ruta y la función correspondiente para obtener la cantidad de películas por plataforma
@app.get("/count_platform/")
def get_count_platform(platform: str):
    if platform=='netflix':
        platform='n'
    if platform=='amazon':
        platform='a'
    if platform=='hulu':
        platform='h'
    if platform=='disney':
        platform='d'
    count_platform = df.copy()
    
    # Obtener las películas de la plataforma ingresada por parámetro
    count_platform = count_platform[count_platform["id"].str[0].str.lower() == platform.lower()]
    
    # Obtener la cantidad de películas
    count = len(count_platform)
    
    # Retornar la cantidad de películas
    return {"platform": platform, "count": count}

# Definir la ruta y la función correspondiente para obtener el actor que más se repite según plataforma y año
@app.get("/actor/")
def get_actor(platform: str, year: int):
    if platform=='netflix':
        platform='n'
    if platform=='amazon':
        platform='a'
    if platform=='hulu':
        platform='h'
    if platform=='disney':
        platform='d'
    # Filtrar por plataforma y año
    df_filtered = df[(df['platform'] == platform) & (df['release_year'] == year)]

    # Contar los actores que más se repiten
    actor_count = df_filtered['cast'].str.split(', ', expand=True).stack().value_counts()

    # Obtener el actor con el mayor recuento
    top_actor = actor_count.index[0]

    # Retornar el nombre del actor como un diccionario
    return {'actor': top_actor}


"""
@app.get("/get_max_duration")
def get_max_duration(year: int = None, platform: str = None, duration_type: str = None):
    # Filtrar por año, plataforma y tipo de duración si se especifican
    if year:
        df_filtered = df[df['release_year'] == year]
    else:
        df_filtered = df
    if platform:
        df_filtered = df_filtered[df_filtered['platform'] == platform]
    if duration_type:
        df_filtered = df_filtered[df_filtered['duration_type'] == duration_type]

    # Encontrar la película con la duración máxima
    max_duration = df_filtered[df_filtered['duration_int'] == df_filtered['duration_int'].max()]

    # Retornar el título y la duración de la película como un diccionario
    return max_duration[['title', 'duration_int']].to_dict('records')

@app.get("/get_score_count")
def get_score_count(platform: str, scored: float, year: int = None):
    # Filtrar por plataforma y año si se especifican
    df_filtered = df[df['platform'] == platform]
    if year:
        df_filtered = df_filtered[df_filtered['release_year'] == year]

    # Contar el número de películas con puntaje mayor a 'scored'
    count = len(df_filtered[df_filtered['score'] >= scored])

    # Retornar la cuenta como un diccionario
    return {'count': count}

@app.get("/get_count_platform")
def get_count_platform(platform: str):
    # Filtrar por plataforma y contar el número de películas
    count = len(df[df['platform'] == platform])

    # Retornar la cuenta como un diccionario
    return {'count': count}

@app.get("/get_actor")
def get_actor(platform: str, year: int):
    # Filtrar por plataforma y año
    df_filtered = df[(df['platform'] == platform) & (df['release_year'] == year)]

    # Contar los actores que más se repiten
    actor_count = df_filtered['cast'].str.split(', ', expand=True).stack().value_counts()

    # Obtener el actor con el mayor recuento
    top_actor = actor_count.index[0]

    # Retornar el nombre del actor como un diccionario
    return {'actor': top_actor}
"""









'''
# Menu
@app.get("/menu")
async def menu():
    return {"Consultas de API_ML": 
            {"get_max_duration" : "Pelicula con mayor duracion","get_score_count" : "Cantidad de películas por plataforma por puntaje","get_count_plataforma" : "Cantidad de películas por plataforma con filtro de plataforma", "get_actor" : "Actor que más se repite según plataforma y año"}}

@app.get("/get_max_duration")
async def get_max_duration(year: int = None, platform: str = None, duration_type: str = None):
    df = datos.copy()
    if year is not None:
        df = df[df['release_year'] == year]
    if platform is not None:
        df = df[df['plataforma'] == platform]
    if duration_type is not None:
        df = df[df['duration_type'] == duration_type]
    max_duration = df[df['duration_int'] == df['duration_int'].max()]
    return max_duration[['title', 'duration_int']].to_dict(orient='records')

@app.get("/get_score_count")
async def get_score_count(platform: str, scored: float, year: int):
    df = datos.copy()
    df = df[(df['plataforma'] == platform) & (df['score'] >= scored) & (df['release_year'] == year)]
    count = df['plataforma'].value_counts().to_dict()
    return count

@app.get("/get_count_platform")
async def get_count_platform(platform: str):
    df = datos.copy()
    df = df[df['plataforma'] == platform]
    count = df['plataforma'].value_counts().to_dict()
    return count

@app.get("/get_actor")
async def get_actor(platform: str, year: int):
    df = datos.copy()
    df = df[(df['plataforma'] == platform) & (df['release_year'] == year)]
    actor = df['cast'].value_counts().index[0]
    return actor

'''