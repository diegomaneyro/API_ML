from fastapi import FastAPI, HTTPException
import pandas as pd
from pandasql import sqldf

# Inicializa en el objeto app la libreria
app = FastAPI(title='API-ML', description='Api de consulta para peliculas y series en plataformas de streming. \n By Diego Maneyro', version='1.0.2')

# Conexión inicial
@app.get("/")
async def Inicio():
    return {"Inicio":"Api_ml"}
@app.get("/verificar_conexion")
def verificar_conexion():
    try:
        # Cargar los datos del archivo CSV en un DataFrame de Pandas
        url = "datos/csvs/peliculas/peliculas_final.csv"
        datos = pd.read_csv(url, sep=',', encoding='latin-1')
        return {"Message": "Conexion Exitosa"}
    except FileNotFoundError:
        return {"Message": "No se encontró el archivo de datos."}
    except Exception as e:
        return {"Message": f"Error en la conexión a los datos: {str(e)}"}

# Definir la ruta para la consulta
@app.get("/max_duration")
def get_max_duration(year: int = None, platform: str = None, duration_type: str = None):
    # Cargar los datos del archivo CSV en un DataFrame de Pandas
    url = "datos/csvs/peliculas/peliculas_final.csv"     
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
def get_score_count(platform: str, scored: str, year: int):
    url = "datos/csvs/peliculas/peliculas_final.csv"     
    datos = pd.read_csv(url)
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
def get_count_platform(platform: str):
    url = "datos/csvs/peliculas/peliculas_final.csv"
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
    
    # Contar los actores que más se repiten
    actor_count = datos['cast'].str.split(', ', expand=True).stack().value_counts()

    # Obtener el actor con el mayor recuento
    top_actor = actor_count.index[0]

    # Retornar el nombre del actor como un diccionario
    return {'actor': top_actor}
