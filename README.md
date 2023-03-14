# <h1 align=center> **API_REC** </h1>

<p align="center">
<img src="https://github.com/diegomaneyro/API_REC/blob/main/src/logo.png"  height=300>
</p>


API_REC es una API desarrollada con dos propositos la primera es poder realizar diferentes consultas sobre series y peliculas en plataformas de Streaming a 
partir de archivos en formato .csv que se utilizan a modo de database, contienen informacion de plataformas de estreaming: Amazon prime, Netflix, Disney plus y 
Hulu. 

En segunda instancia se utiliza esta api para alimentar un modelo de Machine Learning para realizar recomendaciones a usuarios en base a sus elecciones 
previas. Luego de un proceso de ETL(extraer, transformar, cargar) en un jupyter Notebook y normalización de los datos con python, se desarrolo la pi con la 
libreria FastApi. el Deployment se realiza desde Deta.Space.

# <h1 align=center>**`Descripcion del proyecto`**</h1>


## Documentación

**`transformaciones_datos`** : jupyter notebook del proceso ETL sobre los archivos alojados en la carpeta datos


**`transformaciones_ratings`** : jupyter notebook del proceso ETL sobre los archivos alojados en la carpeta ratings


**`main.py`** : archivo python de las API, donde se alojan las querys


**`ratings`** [link](https://drive.google.com/file/d/1cucDq5gdXSD8Q69KN4cOsIbkotHVM3gA/view?usp=share_link) : Datos de los usuarios y sus preferencias sobre peliculas y series


**`peliculas`** [link](https://drive.google.com/file/d/1wRHYGI-SGKNUrYTN8cNXyjdlkTMf1lSv/view?usp=sharing) : Archivos csv que se usaron de base de datos de las plataformas de streaming



## Consultas

+ **get_max_duration**: Película con mayor duración con filtros opcionales de año, plataforma y tipo de duración.


+ **get_score_count**: Cantidad de películas por plataforma con un puntaje mayor a XX en determinado año.


+ **get_count_platform**: Cantidad de películas por plataforma con filtro de plataforma.


+ **get_actor**: Actor que más se repite según plataforma y año. 


## Default

#### Test Conectividad

``http
  GET /test
``

| Parameter | Type     | Description                |
| :-------- | :------- | :------------------------- |
| `No requerido` | `string` | **API_REC: Test ok**. Conección realizada  |



#### Menu

``http
  GET /menu
``

| Parameter | Type     | Description                       |
| :-------- | :------- | :-------------------------------- |
| `No requerido`      | `string` | **Menu opciones**|



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
| `Puntuación` | `Integer` | **scored**  |
| `año` | `Integer` | **year**|


#### get_count_platform

``http
  GET /get_count_platform(platform))
``

| Parameter | Type     | Description                |
| :-------- | :------- | :------------------------- |
| `Plataforma` | `Integer` | **platform** |


#### get_actor

``http
  GET /get_actor(platform, year))
``

| Parameter | Type     | Description                |
| :-------- | :------- | :------------------------- |
| `Plataforma` | `string` | **platform** |
| `año` | `Integer` | **year**  |

## Consultas de Ejemplo

+ [Test](https://pi_1-1-s3688866.deta.app/docs#/default/test_Test_get)
<p align="left">
<img src="https://github.com/diegomaneyro/API_REC/blob/main/src/test.PNG" width="300" height="200">
</p>

+ [Menu](https://pi_1-1-s3688866.deta.app/docs#/default/menu_Menu_get)
<p align="left">
<img src="https://github.com/diegomaneyro/API_REC/blob/main/src/menu.PNG" width="300" height=200>
</p>

+ [Get_max_duration](https://pi_1-1-s3688866.deta.app/docs#/default/get_max_duration_get_max_duration_get)

*

+ [Get_score_count](https://pi_1-1-s3688866.deta.app/docs#/default/get_score_count_get_score_count__platform___scored___year__get)

*

+ [Get_count_plataforma](https://pi_1-1-s3688866.deta.app/docs#/default/get_count_plataforma_get_count_plataforma__platform__get)

*

+ [Get_actor](https://pi_1-1-s3688866.deta.app/docs#/default/get_actor_get_actor__platform___year__get) 

*

+ [DatosContacto](https://pi_1-1-s3688866.deta.app/docs#/default/DatosContacto_Autor_get)


## Deploy
+ Deta.Space: [deploy](https://deta.space/discovery/@diegomaneyro/api_rec)



## Autor

+ diego-maneyro [linkedin](https://www.linkedin.com/in/diego-maneyro/)


+ @diegomaneyro [github](https://www.github.com/octokatherine)


+ E-mail diegomaneyro@gmail.com
# API_ML
