#!/usr/bin/env python
# -*-coding:utf-8 -*

import sys
import re

aux = 1

for line in sys.stdin:
    line = re.sub(r'\W+',' ',line.strip())
    words = line.split()

    
    for word in words:
        if word == 'DocumentEnd':
            aux += 1
            continue
        print('{}\t{}'.format(word,aux))

