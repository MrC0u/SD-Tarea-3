#!/usr/bin/env python
# -*-coding:utf-8 -*

import sys

current_word = None
current_count = 0
current_doc = 0
current = 0
word = None

for line in sys.stdin:
    line = line.strip()
    word, doc = line.split('\t',1)
    count = 1

    try:
        doc = int(doc)
    except ValueError:
        continue
    if current_word == word:
        if current_doc == doc:
            amount[current] = ('('+str(current_count)+','+ str(current_doc) +')')
            current_count += count
        else:
            current_doc = doc
            current_count = count
            current += 1
            amount.append('('+str(current_count)+','+ str(current_doc) +')')
            current_count += 1
    else:
        if current_word:
            print('{}\t{}'.format(current_word,amount))
        current_word = word
        current_count = count
        current_doc = doc
        current = 0
        amount = []
        amount.append('('+str(current_count)+','+ str(current_doc) +')')
        #print(amount)


if current_word == word:
    print('{}\t{}'.format(current_word,current_count))