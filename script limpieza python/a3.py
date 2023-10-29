import csv

# Nombre del archivo CSV de entrada y salida
input_file = r'C:\Users\AVILES\Documents\insaforn\git\analistadedatos\DimAeropuertoColumnas.csv'
output_file = r'C:\Users\AVILES\Documents\insaforn\git\analistadedatos\DimAeropuertoColumnasLimpias.csv'

# Abre el archivo de entrada y crea un archivo de salida
with open(input_file, 'r', newline='') as csvfile, open(output_file, 'w', newline='') as output:
    csv_reader = csv.DictReader(csvfile)
    
    # Lista para almacenar las filas no vacías
    non_empty_rows = []
    i=0
    # Itera a través de las filas del archivo de entrada
    for row in csv_reader:
        i+=1
        # Verifica si alguna de las columnas de la fila es diferente de vacío
        if not row.get('OriginAirportID'):
           continue
        if not row.get('OriginCityName'):
           continue
        if not row.get('OriginState'):
           continue
        if len(row)>3:
            continue

        bandera = False
        ultima_columna = None
        if '\n' in row.get('OriginState'):
            # Divide el string en dos filas si '\n' está presente
            filas = row.get('OriginState').split('\n')
            i=1
            dict_fila=[]
            for fila in filas:
                if i==1:
                    ultima_columna = fila
                    i+=1
                else:
                    arreglo = fila.split(',')
                    if len(arreglo)>3:
                        continue
                    if len(arreglo)<3:
                        continue
                    diccionario={'OriginAirportID':arreglo[0],'OriginCityName':arreglo[1],'OriginState':arreglo[2],}
                    i=1
                    non_empty_rows.append(diccionario)
                bandera = True
        
        if not bandera and row.get('OriginState'):
            row['OriginState'] = row.get('OriginState').replace('"', '').replace(',', '').replace('\n', '')
        elif bandera and ultima_columna:
            row['OriginState'] = ultima_columna.replace('"', '').replace(',', '')
        
        non_empty_rows.append(row)
        # break

    # Cabeceras del archivo CSV
    fieldnames = non_empty_rows[0].keys()

    # Escribe las cabeceras al archivo de salida
    csv_writer = csv.DictWriter(output, fieldnames=fieldnames)
    csv_writer.writeheader()

    # Escribe las filas no vacías al archivo de salida
    for row in non_empty_rows:
        csv_writer.writerow(row)

print("Filas vacías eliminadas y archivo filtrado creado en", output_file)

