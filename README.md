# <h1 align=center> **ApiStream** </h1>

<p align="center">
<img src="recursos/icon.png"  height=300>
</p>


# Autor Diego Maneyro

+ [linkedin](https://www.linkedin.com/in/diego-maneyro/)

+ [E-mail](diegomaneyro@gmail.com)

# Descripcion del proyecto
 
ApiStream es un proyecto desarrollado con dos propósitos principales:
1. API de consultas sobre series y películas en plataformas de streaming, utilizando archivos en formato .csv como base de datos. Estos archivos contienen información de servicios como Amazon Prime, Netflix, Disney Plus y Hulu. Mediante un proceso de ETL (extraer, transformar, cargar) realizado en un Jupyter Notebook y una normalización de datos en Python, se ha creado la API utilizando la biblioteca FastAPI.

2. Modelo de recomendación con Machine Learning que recibe el ID de usuarios de estas plataformas y sugiere series o películas en función de las elecciones previas. Además, se proporciona una interfaz gráfica desarrollada con Gradio, desplegada en HugginsFace, para probar la demostración del modelo de recomendación.


## Repositorio

**`DATOS/ETL`** : jupyter notebook del proceso ETL sobre los archivos de streaming.

**`DATOS/EDA`** : jupyter notebook del proceso exploratorio y graficas necesarias para comprender la calidad del dato. 

**`Recursos`** : archivos multimedia de repositorio.

**`APP/Main`** : Archivo que inicializa la API de consultas

**`Modelo`** : Archivos del modelo de recomendación

## Docker
<p align="left">
<img src="recursos/docker.png"  height=180>
</p>
 Usando Docker realize una imgen de la aplicacion para luego alojarla en Microsoft Azure, por medio de un registro de contenedores que luego se utiliza desde el Web Services. los datos se leen desde un contenedor en una cuenta de almacenamiento en Microsoft Azure Storage para alimentar a la api. 


## Flujo del Dato
<p align="left">
<img src="recursos/flujoDato.png"  height=450>
</p>


## Deploy Api
+ Demo: webappapistream.azurewebsites.net
Por cuestion de costos luego del desarrollo se retiro la app del portal de Azure adjunto captura 
![Captura](https://github.com/diegomaneyro/ApiStream/assets/68664243/bde7f0be-861b-4e1f-b588-e1c3d4f45696)

## Probar api desde Render
Deploy: [Demo]()
## Ingreso de datos

* Las consultas deben ser en minusculas:

* platform(str): netflix, amazon, hulu, disney

* duration_type(str): min(minutos), season(temporadas)

* year(int): 1920 hasta 2020

## Consultas

+ **Inicio**: Pagina de inicio. [inicio de api](https://webappapistream.azurewebsites.net/)

+ **Menu**: Pagina de donde se visualizan las distintas consultas que ofrece la api. [menu opciones](https://webappapistream.azurewebsites.net/docs)

+ **autor**: Datos del desarrollador resposnsable del proyecto. [datos del autor](https://webappapistream.azurewebsites.net/docs#/default/autor_autor_get)

+ **verificar conexion**: Ejecute este paso para asegurarse que la api esta accediendo a los datos. [conexion](https://webappapistream.azurewebsites.net/docs#/default/verificar_conexion_verificar_conexion_get)

+ **get_max_duration**: Película con mayor duración con filtros opcionales de año, plataforma y tipo de duración. [pelicula mayor duración](https://webappapistream.azurewebsites.net/docs#/default/get_max_duration_max_duration_get)

+ **get_score_count**: Cantidad de películas por plataforma con un puntaje mayor a XX en determinado año. [peliculas por puntaje](https://webappapistream.azurewebsites.net/docs#/default/get_score_count_score_count__get)


+ **get_count_platform**: Cantidad de películas por plataforma con filtro de plataforma. [peliculas por plataforma](https://webappapistream.azurewebsites.net/docs#/default/get_count_platform_count_platform__get)


+ **get_actor**: Actor que más se repite según plataforma y año. [actor mas frecuente](https://webappapistream.azurewebsites.net/docs#/default/get_actor_actor__get)

## Api Caracteristicas

``http
  GET / Autor
``

| Parameter | Type     | Description                |
| :-------- | :------- | :------------------------- |
| `No requerido` | `string` | `Datos Desarrollador` |

``http
  GET / verificar Conexion
``

| Condition | Type     | Description                |
| :-------- | :------- | :------------------------- |
| **ok** | `string` |  **Conexion Exitosa** |
| **error** | `string` |  **Error en la conexion a los datos** |

``http
  GET /get_max_duration(year, platform, duration_type)
``

| Parameter | Type     | Description                |
| :-------- | :------- | :------------------------- |
| `Filtro Opcional` | `Integer` | **year** |
| `Filtro Opcional` | `string` | **platform**  |
| `Filtro Opcional` | `string` | **duration_type** |

``http
  GET /get_score_count
``

| Parameter | Type     | Description                |
| :-------- | :------- | :------------------------- |
| `Plataforma` | `String` | **platform** |
| `Puntuación` | `string` | **scored**  |
| `año` | `Integer` | **year**|



``http
  GET /get_count_platform(platform)
``

| Parameter | Type     | Description                |
| :-------- | :------- | :------------------------- |
| `Plataforma` | `string` | **platform** |


``http
  GET /get_actor(platform, year)
``

| Parameter | Type     | Description                |
| :-------- | :------- | :------------------------- |
| `Plataforma` | `string` | **platform** |
| `año` | `Integer` | **year**  |

## Deploy Modelo Recomendacion
* Hugginsface: [Modelo](https://huggingface.co/spaces/diegomaneyro/ApiStream)
  
Se ingresa el IdUsuario y en la salida de datos veremos los titulos de la recomendación

<p align="left">
<img src="recursos/gradio.png"  height=180>
</p>

## Licencia

Este proyecto se distribuye bajo la Licencia MIT. Puedes encontrar los términos y condiciones de la licencia en [este enlace](https://github.com/diegomaneyro/ApiStream/blob/main/License).


