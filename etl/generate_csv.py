import pandas as pd
import random
import datetime

# Parámetros de configuración para los datos
num_records = 10000
productos = ['Laptop', 'Teléfono', 'Monitor', 'Teclado', 'Mouse', 'Tablet', 'Impresora']
precio_range = {
    'Laptop': (700, 1500),
    'Teléfono': (200, 800),
    'Monitor': (100, 400),
    'Teclado': (15, 50),
    'Mouse': (10, 30),
    'Tablet': (150, 500),
    'Impresora': (80, 250)
}

# Generar datos de prueba
data = []
start_date = datetime.date(2023, 1, 1)
for i in range(1, num_records + 1):
    producto = random.choice(productos)
    cantidad = random.randint(1, 20)
    precio = random.uniform(precio_range[producto][0], precio_range[producto][1])
    fecha = start_date + datetime.timedelta(days=random.randint(0, 364))
    data.append([i, producto, cantidad, round(precio, 2), fecha])

# Crear un DataFrame y guardar a CSV
df = pd.DataFrame(data, columns=['id', 'producto', 'cantidad', 'precio', 'fecha'])
df.to_csv('ventas_extenso.csv', index=False)

print("Archivo CSV extenso creado con éxito.")
