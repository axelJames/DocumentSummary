#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep  7 10:59:08 2017

@author: axel
"""

from nltk.tokenize import sent_tokenize
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
import re

inputfile = open("Document.txt", "r").read()inputfile = inputfile.replace('”','"').replace('“','"')
inputfile = re.sub(r'"\s*(?=[A-Z])',r'" .',inputfile)
inputfile = re.sub(r'"(?=\n)','" .',inputfile)
inputfile = inputfile.replace('”','"').replace('“','"')
inputfile = re.sub(r'"\s*(?=[A-Z])',r'" .',inputfile)
inputfile = re.sub(r'"(?=\n)','" .',inputfile)
sentences = sent_tokenize(inputfile)
summ_phra = ["after all",
                     "all in all",
                     "all things considered",
                     "briefly",
                     "by and large",
                     "in any case",
                     "in any event",
                     "in brief",
                     "in conclusion",
                     "on the whole",
                     "in short",
                     "in summary",
                     "in the final analysis",
                     "in the long run, on balance",
                     "to sum up",
                     "to summarize",
                     "finally"]
stopWords = set(stopwords.words('english'))
word_dict = dict()
score = dict()
sumPhrase = dict()
namedEntities = dict()
numWords = dict()
i=0

for sentence in sentences:
    namedEntities[i] = 0
    numWords[i] = 0
    words = word_tokenize(sentence)
    coreWords = [word for word in words if word.lower() not in stopWords]
    for word in coreWords:
        lword = word.lower()
        if lword in word_dict:
            word_dict[lword] += 1
        else:
            word_dict[lword] = 1
        if word[0].isupper():
            namedEntities[i]+=1
    score[i]=0           
    for phrase in summ_phra:
        if phrase in sentence.lower():
            sumPhrase[i] = 1
        else:
            sumPhrase[i] = 0
    i+=1 
i=0
for sentence in sentences:
    coreWords = [word for word in words if word.lower() not in stopWords]
    for word in coreWords:
        lword = word.lower()
        numWords[i] += word_dict[lword];
    score[i] = numWords[i]*0.1 + namedEntities[i] * 0.5 + sumPhrase[i]*2;
    i+=1

rank = sorted(score , key= score.get, reverse=True)
for i in range(4):
    print(str(i)+'\t')
    print(sentences[rank[i]])
    print("\n")
    
