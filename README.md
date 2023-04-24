# <h1 align=center> **API_ML** </h1>

<p align="center">
<img src="https://github.com/diegomaneyro/API_ML/blob/main/src/imagenes/icon.png"  height=300>
</p>

## Api

API_ML es una API desarrollada con el proposito de realizar diferentes consultas sobre series y peliculas en plataformas de Streaming a 
partir de archivos en formato .csv que se utilizan a modo de database, contienen informacion de: Amazon prime, Netflix, Disney plus y Hulu. Luego de un proceso de ETL(extraer, transformar, cargar) en un jupyter Notebook y normalización de los datos con python, se desarrolo la pi con la libreria FastApi. el Deployment se realiza desde render [link](https://api-ml-vk4n.onrender.com/docs) 

## Modelo de recomendacion de Peliculas

Modelo de Machine Learning para realizar recomendaciones a usuarios en base a sus elecciones previas. [link](https://github.com/diegomaneyro/modelo_recomendacion)

# <h1 align=center>**`Descripcion del proyecto`**</h1>


## Documentación

**`ETL_peliculas`** : jupyter notebook del proceso ETL sobre los archivos de streaming [link](https://github.com/diegomaneyro/API_ML/blob/main/src/ETL/ETL_peliculas.ipynb)


**`ETL_ratings`** : jupyter notebook del proceso ETL sobre los archivos de ratings [link](https://github.com/diegomaneyro/API_ML/blob/main/src/ETL/ETL_ratings.ipynb)




**`main.py`** : archivo python de la API, necesario para realizar las consultas [link](https://github.com/diegomaneyro/API_ML/blob/main/main.py)

## EDA


+ **`EDA`** : Exploración de los archivos final luego del ETL, analisis y visualizacion las variables a utilizar por el modelo de predicción [link](https://github.com/diegomaneyro/API_ML/blob/main/src/EDA/eda_peliculas_colab.ipynb)


## Consultas

+ **get_max_duration**: Película con mayor duración con filtros opcionales de año, plataforma y tipo de duración.


+ **get_score_count**: Cantidad de películas por plataforma con un puntaje mayor a XX en determinado año.


+ **get_count_platform**: Cantidad de películas por plataforma con filtro de plataforma.


+ **get_actor**: Actor que más se repite según plataforma y año. 



#### Inicio

``http
  GET /inicio
``

| Parameter | Type     | Description                |
| :-------- | :------- | :------------------------- |
| `No requerido` | `string` | **API_ML: Test ok**. Conección realizada  |




#### get_max_duration

``http
  GET /get_max_duration(year, platform, duration_type)
``

| Parameter | Type     | Description                |
| :-------- | :------- | :------------------------- |
| `Filtro Opcional` | `Integer` | **year** |
| `Filtro Opcional` | `string` | **platform**  |
| `Filtro Opcional` | `string` | **duration_type** |



#### get_score_count(platform, scored, year)

``http
  GET /get_score_count
``

| Parameter | Type     | Description                |
| :-------- | :------- | :------------------------- |
| `Plataforma` | `String` | **platform** |
| `Puntuación` | `string` | **scored**  |
| `año` | `Integer` | **year**|


#### get_count_platform

``http
  GET /get_count_platform(platform))
``

| Parameter | Type     | Description                |
| :-------- | :------- | :------------------------- |
| `Plataforma` | `string` | **platform** |


#### get_actor

``http
  GET /get_actor(platform, year))
``

| Parameter | Type     | Description                |
| :-------- | :------- | :------------------------- |
| `Plataforma` | `string` | **platform** |
| `año` | `Integer` | **year**  |


## Consultas de Ejemplo

* Las consultas deben ser en minusculas:
* platform: netflix, amazon, hulu, disney
* duration_type: min(minutos), season(temporadas)
* year: 1920 hasta 2021

#### [Get_max_duration](https://api-ml-vk4n.onrender.com/max_duration/?year=2020&platform=amazon&duration_type=min)
* /2020/amazon/min:

**respuesta**  "title": "night sky with nature sounds with 432hz nature sound track for sleep","duration_int": 540

#### [Get_score_count](https://api-ml-vk4n.onrender.com/score_count/?platform=netflix&scored=20&year=2020)
* /2020/netflix/20

**respuesta**  "scored": "20","año": 2020,
  "cantidad de peliculas": 953
  
#### [Get_count_plataforma](https://api-ml-vk4n.onrender.com/count_platform/?platform=netflix)
* /netflix

**respuesta**  "platform": "n","count": 8807

#### [Get_actor](https://api-ml-vk4n.onrender.com/actor/?platform=disney&year=2020) 
* /disney/2020

**respuest**  "actor": "jonathan groff"

## Deploy
+ Render: [deploy](https://api-ml-vk4n.onrender.com/docs)
<p align="left">
<img src="https://github.com/diegomaneyro/API_ML/blob/main/src/imagenes/Render-logo.png"  height=180>
</p>


## Descargas
 
+ [peliculas.csv](https://vosjaatcfqxsgchnfgds.supabase.co/storage/v1/object/sign/peliculas/peliculas_final.csv?token=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1cmwiOiJwZWxpY3VsYXMvcGVsaWN1bGFzX2ZpbmFsLmNzdiIsImlhdCI6MTY3OTM5NTQyMSwiZXhwIjoxNjgxOTg3NDIxfQ.VeyW8FlS6XyaO5wlSFr4KNvBT80s3DKz617eqHBb_jU&t=2023-03-21T10%3A43%3A42.592Z)

+ [score.csv](https://vosjaatcfqxsgchnfgds.supabase.co/storage/v1/object/sign/peliculas/ratings_final.zip?token=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1cmwiOiJwZWxpY3VsYXMvcmF0aW5nc19maW5hbC56aXAiLCJpYXQiOjE2NzkzOTcwMjMsImV4cCI6MTY4MTk4OTAyM30.t0IxFdanysxDLFtc4Q98nzQUIo5oFY1-yzT-q_jtPwg&t=2023-03-21T11%3A10%3A23.566Z)

## Autor

+ diego-maneyro [linkedin](https://www.linkedin.com/in/diego-maneyro/)


+ @diegomaneyro [github](https://www.github.com/octokatherine)


+ E-mail diegomaneyro@gmail.com

