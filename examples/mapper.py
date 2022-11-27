#!/usr/bin/env python
# -*-coding:utf-8 -*

import sys
import re

arr = []
doc = 0
aux = 0

for line in sys.stdin:
    line = re.sub(r'\W+',' ',line.strip())
    line = line.lower()
    words = line.split()
    
    for word in words:
        if word.find("documentbegin") != -1:
            doc , aux = word.split('documentbegin')
        arr.append('{}\t{}\t{}'.format(word,doc,1))

for out in sorted(arr):
    print(out)

