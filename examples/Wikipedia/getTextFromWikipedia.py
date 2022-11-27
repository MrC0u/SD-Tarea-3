# Importar API de Wikipedia
import wikipedia as wiki

# Cambiamos el lenguaje en el que vamos a buscar
wiki.set_lang("es")

# Hacemos un arreglo con las busquedas que deseamos realizar 
busquedas = ["Anime","One Piece","Liverpool FC", "Ryzen", "Pisco Elqui", "Cerveza", "Ron", "Pokemon", "Digimon", "Condorito"]

# Creamos arreglos para guardar los archivos y la data
datos = []
data = []

print('Descargando data...')

# Guardamos la data en un arreglo y creamos los archivos de salida 
for i in range(len(busquedas)):
    #print(i)
    datos.append(wiki.page(busquedas[i]))
    data.append(open("./Output/data"+str(i+1)+".txt", "w", encoding="utf-8"))

# Guardamos la data en los archivos de salida
for i in range(len(data)):
    print('Escribiendo data'+str(i+1)+'.txt')
    # Insertamos un numero de documento + un "DocumentBegin" que utilizaremos luego para el procesamiento del mapper
    data[i].write(str(i+1)+'DocumentBegin'+'\n')
    # Luego insertamos el contenido de la busqueda
    data[i].write(datos[i].content)
    data[i].close()

print('Escritura Finalizada')