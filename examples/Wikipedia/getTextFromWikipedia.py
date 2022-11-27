import wikipedia as wiki

wiki.set_lang("es")

datos = [wiki.page("Anime"), wiki.page("One Piece"), wiki.page("Liverpool FC"), 
wiki.page("Ryzen"), wiki.page("Pisco Elqui"), wiki.page("Cerveza"), wiki.page("Ron"), wiki.page("Pokemon"), 
wiki.page("Digimon"), wiki.page("Condorito")]

data1 = open("data1.txt", "w", encoding="utf-8")
data2 = open("data2.txt", "w", encoding="utf-8")
data3 = open("data3.txt", "w", encoding="utf-8")
data4 = open("data4.txt", "w", encoding="utf-8")
data5 = open("data5.txt", "w", encoding="utf-8")
data6 = open("data6.txt", "w", encoding="utf-8")
data7 = open("data7.txt", "w", encoding="utf-8")
data8 = open("data8.txt", "w", encoding="utf-8")
data9 = open("data9.txt", "w", encoding="utf-8")
data10 = open("data10.txt", "w", encoding="utf-8")

output = [data1, data2, data3, data4, data5, data6, data7, data8, data9, data10]

for i in range(len(output)):
    output[i].write(datos[i].content)
    output[i].close()
