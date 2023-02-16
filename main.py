import pandas as pd
from sqlalchemy import create_engine

# Leer el archivo CSV
df = pd.read_csv('used_car_dataset.csv')
print(df)

# Conectar a la base de datos
engine = create_engine('sqlite:///data_practica.db')

# Escribir los datos del DataFrame en la base de datos
df.to_sql('Cars', engine, if_exists='replace', index=False)