import wikipedia as wiki
import sys

arg = sys.argv

wiki.set_lang("es")

a = wiki.page(arg)

print(a.content)