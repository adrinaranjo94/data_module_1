import pandas as pd
import mysql.connector
import matplotlib.pyplot as plt

# Configuración de conexión a MySQL
conexion = mysql.connector.connect(
    host="localhost",
    user="root",        # Reemplazar por tu usuario de MySQL
    password="rootpassword",  # Reemplazar por tu contraseña de MySQL
    database="ETL"      # Nombre de la base de datos a usar/crear
)

cursor = conexion.cursor()

# Crear base de datos si no existe
cursor.execute("USE ETL")

# Crear tabla de ventas
cursor.execute('''
    CREATE TABLE IF NOT EXISTS ventas (
        id INT PRIMARY KEY,
        producto VARCHAR(50) NOT NULL,
        cantidad INT,
        precio FLOAT,
        fecha DATE
    )
''')

# Leer el archivo CSV extenso
df = pd.read_csv('ventas_extenso.csv')

# Insertar datos en la tabla de MySQL
for _, row in df.iterrows():
    cursor.execute('''
        INSERT INTO ventas (id, producto, cantidad, precio, fecha)
        VALUES (%s, %s, %s, %s, %s)
    ''', tuple(row))

# Confirmar los cambios en la base de datos
conexion.commit()

# Cerrar la conexión a MySQL
conexion.close()
