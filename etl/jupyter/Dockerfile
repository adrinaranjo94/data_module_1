# Usa una imagen base de Python
FROM python:3.9

# Establece el directorio de trabajo en el contenedor
WORKDIR /app

# Copia el archivo de requisitos al contenedor
COPY requirements.txt .

# Instala las dependencias listadas en requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Instala Jupyter Notebook
RUN pip install jupyter

# Copia la carpeta de notebooks al contenedor
COPY notebooks /app/notebooks

# Copia el archivo .env al contenedor
# El archivo .env está en la carpeta superior, por lo que usamos COPY ../.env ./

# Expone el puerto 8888 para Jupyter Notebook
EXPOSE 8888

# Comando para iniciar Jupyter Notebook
CMD ["jupyter", "notebook", "--ip=0.0.0.0", "--no-browser", "--allow-root", "--NotebookApp.token=''"]
