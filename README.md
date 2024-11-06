# <h1 align=center> **ApiStream** </h1>

<p align="center">
<img src="recursos/icon.png"  height=300>
</p>


# Autor Diego Maneyro

+ [linkedin](https://www.linkedin.com/in/diego-maneyro/)

+ [E-mail](diegomaneyro@gmail.com)

# Descripcion 
ApiStream es un proyecto desarrollado con dos propósitos principales:

API RESTful de Consultas sobre Series y Películas en Plataformas de Streaming:

Descripción: ApiStream ofrece una API RESTful que permite realizar consultas sobre series y películas disponibles en plataformas de streaming como Amazon Prime, Netflix, Disney Plus y Hulu.

Base de Datos: Los datos se almacenan en archivos .csv que contienen información detallada sobre los servicios de streaming. Estos archivos han sido procesados mediante un flujo ETL (Extraer, Transformar, Cargar) realizado en un Jupyter Notebook, y los datos se han normalizado utilizando Python.

Tecnología: La API está construida utilizando la biblioteca FastAPI, que facilita la creación de APIs rápidas y de alto rendimiento.

¿Qué es RESTful?:

Descripción: RESTful (Representational State Transfer) es un estilo de arquitectura para diseñar servicios web. Utiliza HTTP para realizar operaciones CRUD (Crear, Leer, Actualizar, Eliminar) y se basa en recursos, que son entidades accesibles mediante URLs únicas.

Características: Las APIs RESTful son escalables, fáciles de mantener y permiten interacciones con los servicios web de manera uniforme e intuitiva mediante métodos HTTP estándar como GET, POST, PUT y DELETE.

Modelo de Recomendación con Machine Learning:

Descripción: ApiStream incluye un modelo de recomendación basado en Machine Learning, que sugiere series o películas a los usuarios en función de sus elecciones previas.

Input: El modelo recibe el ID de los usuarios de estas plataformas.

Output: Genera recomendaciones personalizadas basadas en el historial de visualización de los usuarios.

Interfaz Gráfica: Además, se proporciona una interfaz gráfica desarrollada con Gradio, desplegada en Hugging Face, para probar y demostrar el modelo de recomendación.


## Repositorio


**`APP/Main`** : Archivo que inicializa la API de consultas

**`ETL`** : jupyter notebook del proceso ETL sobre los archivos de streaming.

**`EDA`** : jupyter notebook del proceso exploratorio y graficas necesarias para comprender la calidad del dato. 

**`Recursos`** : archivos multimedia de repositorio.

**`Modelo`** : Archivos del modelo de recomendación

**`tests`** : Archivos de test


## Deploy Render
Deploy: [Demo](https://apistream.onrender.com)


## Ingreso de datos

* Las consultas deben ser en minusculas:

* platform(str): netflix, amazon, hulu, disney

* duration_type(str): min(minutos), season(temporadas)

* year(int): 1920 hasta 2020

## Consultas

+ **Inicio**: Pagina de inicio. [inicio de api](https://apistream.onrender.com/)

+ **Menu**: Pagina de donde se visualizan las distintas consultas que ofrece la api. [menu opciones](https://apistream.onrender.com/docs)

+ **autor**: Datos del desarrollador resposnsable del proyecto. [datos del autor](https://apistream.onrender.com/docs#/default/autor_autor_get)

+ **verificar conexion**: Ejecute este paso para asegurarse que la api esta accediendo a los datos. [conexion](https://apistream.onrender.com/docs#/default/verificar_conexion_verificar_conexion_get)

+ **get_max_duration**: Película con mayor duración con filtros opcionales de año, plataforma y tipo de duración. [pelicula mayor duración](https://apistream.onrender.com/docs#/default/get_max_duration_max_duration_get)

+ **get_score_count**: Cantidad de películas por plataforma con un puntaje mayor a XX en determinado año. [peliculas por puntaje](https://apistream.onrender.com/docs#/default/get_score_count_score_count__get)


+ **get_count_platform**: Cantidad de películas por plataforma con filtro de plataforma. [peliculas por plataforma](https://apistream.onrender.com/docs#/default/get_count_platform_count_platform__get)


+ **get_actor**: Actor que más se repite según plataforma y año. [actor mas frecuente](https://apistream.onrender.com/docs#/default/get_actor_actor__get)

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


