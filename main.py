from fastapi import FastAPI
import csv
from typing import Union
from deta import Deta  
import pandas as pd

# Inicializar con una clave de proyecto
deta = Deta("e0kgopbpahs_gHLJU5Cg4hpbaCVZdbwUQ8WFbSuBoVp1")
# Leer csv
csv_peliculas = r"datos\peliculas_completo.csv"

# Inicializa en el objeto app la libreria
app = FastAPI(title='API-REC', description='Api de consulta para peliculas y series en plataformas de streming. \n By Diego Maneyro', version='1.0.1')

@app.get("/")
async def Inicio():
    return {"API_REC":{"Test":"/test",
                       "Inicio":"/docs",
                       }}

# Inicio e informacion
@app.get("/test")
async def test():
    return {"message": "API_REC: test_conection OK"}


@app.get("/menu")
async def menu():
    return {"Consultas de API_REC": 
            {"get_max_duration" : "Pelicula con mayor duracion","get_score_count" : "Cantidad de películas por plataforma por puntaje","get_count_plataforma" : "Cantidad de películas por plataforma con filtro de plataforma", "get_actor" : "Actor que más se repite según plataforma y año"}}


# Película con mayor duración con filtros opcionales de AÑO, PLATAFORMA Y TIPO DE DURACIÓN    
@app.get('/get_max_duration') 
def get_max_duration(year:int, platform:str, duration_type:str): 
    datos_csv = pd.read_csv(r'src\datos\peliculas_final.csv')
    respuesta = ''
    res = datos_csv[(datos_csv['release_year']==year) & (datos_csv['duration_type']==duration_type) & (datos_csv['plataforma']==platform)]
    res = res.sort_values('duration_int', ascending=False)
    res = res.head(1)
    respuesta = res.title.to_list()  
    return respuesta[0]

    



# Cantidad de películas por plataforma con un puntaje mayor a XX en determinado año
@app.get("/get_score_count/{platform}/{scored}/{year}")
def get_score_count(platform: str, scored: int, year: int):
    cantidad_pelicula = 0
    return {"cantidad pelicula" : cantidad_pelicula}


# Cantidad de películas por plataforma con filtro de plataforma
@app.get("/get_count_plataforma/{platform}")
def get_count_plataforma(platform: str):
     cantidad_pelicula = 0
     return {"cantidad pelicula" : cantidad_pelicula}


# Actor que más se repite según plataforma y año. (La función debe llamarse get_actor(platform, year))
@app.get("/get_actor/{platform}/{year}")
def get_actor():
    return 


# Datos de contacto 
@app.get("/Autor")
async def Datos_Contacto():
    contacto = {"Nombre":"Diego Maneyro", "email":"diegomaneyro@gmail.com","github":"https://github.com/diegomaneyro"}
    return contacto

