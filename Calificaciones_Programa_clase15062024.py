import csv

def obtener_fichero_calificaciones():
    lista = []
    with open(r"C:\Users\cetecom\Downloads\calificaciones1.csv", "r", newline="") as archivo:
        lector_csv = csv.reader(archivo, delimiter=";")
        pos = 0
        for linea in lector_csv:
            if pos != 0:
                for i in range(2, len(linea)):
                    if linea[i] == '':
                        linea[i] = '0,0'

                Apellidos = linea[0]
                nombre = linea[1]
                Asistencia = float(linea[2].replace('%', '').replace(',', '.'))
                Parcial1 = float(linea[3].replace(',', '.'))
                Parcial2 = float(linea[4].replace(',', '.'))
                Ordinario1 = float(linea[5].replace(',', '.'))
                Ordinario2 = float(linea[6].replace(',', '.'))
                Practicas = float(linea[7].replace(',', '.'))
                OrdinarioPracticas = float(linea[8].replace(',', '.'))
                lista.append({
                    'Apellidos': Apellidos,
                    'Nombre': nombre,
                    'Asistencia': Asistencia,
                    'Parcial1': Parcial1,
                    'Parcial2': Parcial2, 
                    'Ordinario1': Ordinario1, 
                    'Ordinario2': Ordinario2,
                    'Practicas': Practicas, 
                    'OrdinarioPracticas': OrdinarioPracticas,
                })

                print(linea)
            else:
                pos = 1
    return lista
        
obtener_fichero_calificaciones()
