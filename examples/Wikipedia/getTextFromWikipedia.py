import wikipedia as wiki

wiki.set_lang("es")

a = wiki.page("Anime")
b = wiki.page("One Piece")
c = wiki.page("Liverpool FC")
d = wiki.page("Ryzen")
e = wiki.page("Pisco Elqui")
f = wiki.page("Cerveza")
g = wiki.page("Ron")
h = wiki.page("Pokemon")
i = wiki.page("Digimon")
j = wiki.page("Condorito")

print(a.summary)
print(b.summary)
print(c.summary)
print(d.summary)
print(e.summary)
print(f.summary)
print(g.summary)
print(h.summary)
print(i.summary)
print(j.summary)