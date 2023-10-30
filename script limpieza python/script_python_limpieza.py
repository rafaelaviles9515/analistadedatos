import csv

# Nombre del archivo CSV de entrada y salida
input_file = r'C:\Users\AVILES\Documents\insaforn\git\analistadedatos\out_aerolinea.csv'
output_file = r'C:\Users\AVILES\Documents\insaforn\git\analistadedatos\DimAerolinea.csv'

# Abre el archivo de entrada y crea un archivo de salida
with open(input_file, 'r', newline='') as csvfile, open(output_file, 'w', newline='') as output:
    csv_reader = csv.DictReader(csvfile)
    
    # Lista para almacenar las filas no vacías
    non_empty_rows = []
    # Itera a través de las filas del archivo de entrada
    for row in csv_reader:
        # Verifica si alguna de las columnas de la fila es diferente de vacío
        if row.get('Code'):
            non_empty_rows.append(row)

    # Cabeceras del archivo CSV
    fieldnames = non_empty_rows[0].keys()

    # Escribe las cabeceras al archivo de salida
    csv_writer = csv.DictWriter(output, fieldnames=fieldnames)
    csv_writer.writeheader()

    # Escribe las filas no vacías al archivo de salida
    for row in non_empty_rows:
        csv_writer.writerow(row)

print("Filas vacías eliminadas y archivo filtrado creado en", output_file)
