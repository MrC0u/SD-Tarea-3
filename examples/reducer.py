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
    word, doc ,count = line.split('\t')

    try:
        doc = int(doc)
        count = int(count)
    except ValueError:
        continue

    if current_word == word:
        if current_doc == doc:
            current_count += count
            amount[current] = ('('+str(current_count)+','+ str(current_doc) +')')
        else:
            current_doc = doc
            current_count = count
            current += 1
            amount.append('('+str(current_count)+','+ str(current_doc) +')')
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
