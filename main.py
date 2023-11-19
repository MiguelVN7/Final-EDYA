import json
import random



# Función para generar una relación de forma aleatoria
def generar_relacion(id_emisor, id_receptor):
    nombres = ["Juan", "Maria", "Luis", "Ana", "Pedro", "Edison", "Gertrudis", "Rafaella", "Tulio", "Laura", "Carlos", "Miguel", "Elena", "Sofia"]
    mensaje = f"Hola {nombres[id_receptor]}, soy {nombres[id_emisor]}. Amigos!!!."

    relacion = {
        "id_emisor": id_emisor,
        "nombre_emisor": nombres[id_emisor],
        "id_receptor": id_receptor,
        "nombre_receptor": nombres[id_receptor],
        "mensaje": mensaje
    }
    return relacion




def main(cantidad):
    # Número de relaciones a generar
    n = cantidad

    # Lista para almacenar las relaciones
    relaciones = []

    # Generar n relaciones y agregarlas a la lista
    for _ in range(n):
        id_emisor = random.randint(0, 13)
        id_receptor = random.randint(0, 13)
        while (id_emisor == id_receptor):
            id_receptor = random.randint(0, 13)
        relacion = generar_relacion(id_emisor, id_receptor)
        relaciones.append(relacion)

    # Guardar la lista de relaciones en un archivo JSON
    with open('C:\\Users\\Miguel\\Downloads\\historial_comunicaciones.json', "w") as archivo_json:
        json.dump(relaciones, archivo_json, indent=2)

    print(f"Se han generado y guardado {n} relaciones en el archivo 'historial_comunicaciones.json'.")

if __name__ == '__main__':
    main(int(input("¿Cuantos datos desea generar?: ")))

    nombres = ["Juan", "Maria", "Luis", "Ana", "Pedro", "Edison", "Gertrudis", "Rafaella", "Tulio", "Laura", "Carlos",
               "Miguel", "Elena", "Sofia"]


print("\nDatos generados en forma de lista: ")
with open('C:\\Users\\Miguel\\Downloads\\historial_comunicaciones.json', 'r') as file:
    data = json.load(file)

for x in data:
    print(x)



print('\nCantidad de veces que se repite cada nombre como emisor y receptor: ')
# Diccionarios para los conteos de emisor y receptor
conteo_emisores = {nombre: 0 for nombre in nombres}
conteo_receptores = {nombre: 0 for nombre in nombres}

# Recorrer la lista y aumentar los contadores
for relacion in data:
    conteo_emisores[relacion['nombre_emisor']] += 1
    conteo_receptores[relacion['nombre_receptor']] += 1

# Resultados
for nombre in nombres:
    print(f'{nombre}: como emisor(a) se repite: {conteo_emisores[nombre]} veces, como receptor(a) se repite: {conteo_receptores[nombre]} veces')



print()
# Encontrar el emisor que más y menos solicitudes envió
emisor_mas = max(conteo_emisores, key=conteo_emisores.get)
emisor_menos = min(conteo_emisores, key=conteo_emisores.get)

# Encontrar el receptor que más y menos solicitudes recibió
receptor_mas = max(conteo_receptores, key=conteo_receptores.get)
receptor_menos = min(conteo_receptores, key=conteo_receptores.get)

# Resultados
print(f'El emisor que más solicitudes envió es: {emisor_mas} con {conteo_emisores[emisor_mas]} solicitudes')
print(f'El emisor que menos solicitudes envió es: {emisor_menos} con {conteo_emisores[emisor_menos]} solicitudes')
print(f'El receptor que más solicitudes recibió es: {receptor_mas} con {conteo_receptores[receptor_mas]} solicitudes')
print(f'El receptor que menos solicitudes recibió es: {receptor_menos} con {conteo_receptores[receptor_menos]} solicitudes')



print()
# Diccionario para los conteos de las relaciones
conteo_relaciones = {}

# Recorrer la lista e ir aumentando los contadores
for relacion in data:
    # Tupla de la relación (emisor y receptor)
    relacion_tupla = (relacion['nombre_emisor'], relacion['nombre_receptor'])

    # Revisar si la relacion existe o no en el diccionario y, si existe, aumentar el conteo
    if relacion_tupla in conteo_relaciones:
        conteo_relaciones[relacion_tupla] += 1
    # Si no existe, se crea con valor inicial de 1
    else:
        conteo_relaciones[relacion_tupla] = 1

# Encontrar la relación más fuerte
relacion_mas_solicitudes = max(conteo_relaciones, key=conteo_relaciones.get)

# Imprimirla con el numero de solicitudes
print(f'La relación con más solicitudes es entre {relacion_mas_solicitudes[0]} y {relacion_mas_solicitudes[1]}, con {conteo_relaciones[relacion_mas_solicitudes]} solicitudes.')



print()
# Diccionario para el total de solicitudes enviavads y recibidas por persona
suma_solicitudes = {}

# Calcular la suma de solicitudes de cada persona
for nombre in nombres:
    suma_solicitudes[nombre] = conteo_emisores[nombre] + conteo_receptores[nombre]

# Persona con más solicitudes enviadas y recibidas
persona_mas_solicitudes = max(suma_solicitudes, key=suma_solicitudes.get)

# Imprimir con el numero de solicitudes
print(f'La persona con la mayor suma de solicitudes enviadas y recibidas es: {persona_mas_solicitudes} con {suma_solicitudes[persona_mas_solicitudes]} solicitudes.')