import wikipedia as wiki

wiki.set_lang("es")

datos = [wiki.page("Anime"), wiki.page("One Piece"), wiki.page("Liverpool FC"), 
wiki.page("Ryzen"), wiki.page("Pisco Elqui"), wiki.page("Cerveza"), wiki.page("Ron"), wiki.page("Pokemon"), 
wiki.page("Digimon"), wiki.page("Condorito")]

data1 = open("./Output/data1.txt", "w", encoding="utf-8")
data3 = open("./Output/data3.txt", "w", encoding="utf-8")
data4 = open("./Output/data4.txt", "w", encoding="utf-8")
data2 = open("./Output/data2.txt", "w", encoding="utf-8")
data5 = open("./Output/data5.txt", "w", encoding="utf-8")
data6 = open("./Output/data6.txt", "w", encoding="utf-8")
data7 = open("./Output/data7.txt", "w", encoding="utf-8")
data8 = open("./Output/data8.txt", "w", encoding="utf-8")
data9 = open("./Output/data9.txt", "w", encoding="utf-8")
data10 = open("./Output/data10.txt", "w", encoding="utf-8")

output = [data1, data2, data3, data4, data5, data6, data7, data8, data9, data10]

for i in range(len(output)):
    output[i].write(str(i+1)+'DocumentBegin'+'\n')
    output[i].write(datos[i].content)
    output[i].close()
