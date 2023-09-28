# Usar la imagen oficial de Python como base
FROM python:3.11

# Establecer el directorio de trabajo en /code
WORKDIR /code

# Copiar archivo de los requisitos de aplicación al contenedor
COPY ./requirements.txt /code/requirements.txt

# instalar dependencias
RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt

# Copiar el codigo dentro del directori de trabajo
COPY ./app /code/app

# Comando para ejecutar la aplicación (ajusta según sea necesario)
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "80"]