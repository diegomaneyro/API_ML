from fastapi import FastAPI, HTTPException
import pandas as pd
from pandasql import sqldf

# Inicializa en el objeto app la libreria
app = FastAPI(title='ApiStream', description='Api de consulta para peliculas y series en plataformas de streming. \n By Diego Maneyro', version='1.0.4')

# Leer datos desde 
url = "datos\csvs\peliculas\peliculas_final.csv"

# inicio
@app.get("/")
async def Inicio():
    return {"Inicio":"Api_ml"}

@app.get("/autor")
async def autor():
    datos = {"Nombre y Apellido":"Diego Maneyro",
            "Email":"diegomaneyro@gmail.com"}
    return datos

@app.get("/verificar_conexion")
async def verificar_conexion():
    try:
        # Leer los datos del archivo CSV
        datos = pd.read_csv(url, sep=',', encoding='latin-1')
        return {"Message": "Conexión Exitosa"}
    except Exception as e:
        return {"Message": f"Error en la conexión a los datos: {str(e)}"}


# Definir la ruta para la consulta
@app.get("/max_duration")
async def get_max_duration(year: int = None, platform: str = None, duration_type: str = None):
    # Cargar los datos del archivo CSV en un DataFrame de Pandas           
    datos = pd.read_csv(url, sep=',', encoding='latin-1')        
    # Crear la consulta SQL base
    query = """
        SELECT *
        FROM datos
        WHERE 1 = 1
    """    
    # Agregar condiciones opcionales según los parámetros proporcionados
    if year is not None:
        query += f" AND release_year = {year}"
    if platform is not None:
        
        query = query = f"""
                SELECT *
                FROM datos
                WHERE LOWER(SUBSTR(id, 1, 1)) = '{platform[0]}'
            """
        df_filtrado = sqldf(query, locals())            
    if duration_type is not None:
        query += f" AND duration_type = '{duration_type}'"
    
    # Agregar ordenamiento y limitación
    query += " ORDER BY duration_int DESC LIMIT 1"
    
    # Ejecutar la consulta utilizando pandasql
    df_filtrado = sqldf(query, locals())
    
    # Verificar si se encontraron resultados
    if df_filtrado.empty:
        raise HTTPException(status_code=404, detail="No se encontraron resultados.")
    
    # Obtener el título del DataFrame filtrado
    titulo = df_filtrado["title"].values[0]
    
    # Crear el diccionario de respuesta
    respuesta = {'title': titulo}
    
    # Devolver la respuesta
    return respuesta    


# Definir la ruta y la función correspondiente para obtener la cantidad de películas por plataforma con un puntaje mayor a XX en determinado año
@app.get("/score_count/")
async def get_score_count(platform: str, scored: str, year: int):    
    datos = pd.read_csv(url, sep=',', encoding='latin-1') 
    if platform=='netflix':
        platform='n'
    if platform=='amazon':
        platform='a'
    if platform=='hulu':
        platform='h'
    if platform=='disney':
        platform='d'
    score_count = datos.copy()
    
    # Obtener las películas de la plataforma y del año ingresados por parámetro
    score_count = score_count[(score_count["id"].str[0].str.lower() == platform.lower()) & (score_count["release_year"] == year)]
    
    # Obtener la cantidad de películas con el puntaje mayor al ingresado por parámetro
    score_count = score_count[score_count["rating"] >= scored]
    count = len(score_count)
    
    # Retornar la cantidad de películas
    return {"scored": scored, "año": year, "cantidad de peliculas": count}

# Definir la ruta y la función correspondiente para obtener la cantidad de películas por plataforma
@app.get("/count_platform/")
async def get_count_platform(platform: str):
    datos = pd.read_csv(url, sep=',', encoding='latin-1')     
    if platform=='netflix':
        platform='n'
    if platform=='amazon':
        platform='a'
    if platform=='hulu':
        platform='h'
    if platform=='disney':
        platform='d'
    count_platform = datos.copy()
    
    # Obtener las películas de la plataforma ingresada por parámetro
    count_platform = count_platform[count_platform["id"].str[0].str.lower() == platform.lower()]
    
    # Obtener la cantidad de películas
    count = len(count_platform)
    if platform=='n':
        platform='netflix'
    if platform=='a':
        platform='amazon'
    if platform=='h':
        platform='hulu'
    if platform=='d':
        platform='disney'
    # Retornar la cantidad de películas
    return {"plataforma de streaming": platform, "cantidad de peliculas": count}

# Definir la ruta y la función correspondiente para obtener el actor que más se repite según plataforma y año
@app.get("/actor/")
async def get_actor(platform: str, year: int):       
    datos = pd.read_csv(url, sep=',', encoding='latin-1')  
    if platform=='netflix':
        platform='n'
    if platform=='amazon':
        platform='a'
    if platform=='hulu':
        platform='h'
    if platform=='disney':
        platform='d'
    # Filtrar las filas donde 'cast' no es igual a 'sindato'
    datos = datos[datos['cast'] != 'SinDato']
    datos = datos[datos['id'].str[0].str.lower() == platform]

     # Contar los actores que más se repiten
    actor_count = datos['cast'].str.split(', ', expand=True).stack().value_counts()

    # Verificar si actor_count está vacío o nulo
    if actor_count.empty or actor_count.isna().all():
        return {'actor': 'Dato no disponible'}
        
    # Obtener el actor con el mayor recuento
    top_actor = actor_count.index[0]

    # Retornar el nombre del actor como un diccionario
    return {'actor': top_actor}
