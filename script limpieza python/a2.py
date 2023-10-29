import pandas as pd

# Lee el archivo CSV en un DataFrame
df = pd.read_csv(r'C:\Users\AVILES\Documents\insaforn\git\analistadedatos\DimAeropuertoColumnasLimpias.csv')

# Elimina las filas duplicadas basadas en todas las columnas
df = df.drop_duplicates()

# Guarda el DataFrame resultante en un nuevo archivo CSV
df.to_csv(r'C:\Users\AVILES\Documents\insaforn\git\analistadedatos\DimAeropuertoColumnasArregladoDuplciado.csv', index=False)