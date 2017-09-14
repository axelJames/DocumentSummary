# -*- coding: utf-8 -*-
import sys
import nltk
import string
import os
from collections import namedtuple
from nltk.tokenize import sent_tokenize
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
import re

Sentence = namedtuple('Sentence', ['text', 'wordset','pos','Named_Entity_count','Numerical_count', 'Summary_phrase_count'])
SenNode = namedtuple('SenNode', ['score', 'sentence'])

def ExtractDocument(File):
    """
    Takes input file and prints the summary
    """
    with open(File, "r") as inputfile:
        content = inputfile.read()
    content = " ".join(content.splitlines())
    content = content.replace('”','"').replace('“','"')
    sentences = sent_tokenize(content.decode('utf-8'))
    word_tokens = [word for word in word_tokenize(content.decode("utf-8"))
                   if word not in stopwords.words('english')
                   and word not in string.punctuation ]
    words = nltk.pos_tag(word_tokens)
    wordset = repetitionWord(words)
    sen = []
    pos = 0
    for sentence in sentences:
        summ = SummeryPhrases(sentence)
        senwordSet={}
        for word in wordset.keys():
            if word[0] in sentence:
                senwordSet[word] = wordset[word]
        if len(senwordSet) < 5: #removing short sentences
            continue
        # Finding Named Entity and number Words
        Num_Named_entity= []
        Num_Numbers = 0
        for word in senwordSet:
            if word[1]=="NNP":
                Num_Named_entity.append(word)
            if word[1]=="CD":
                Num_Numbers +=1
        sen.append(Sentence(sentence, senwordSet, pos, Num_Named_entity, Num_Numbers, summ))
        if pos <3:
            pos +=1
        else:
            pos=0
    score={}
    Sentences=[]
    for i in sen:
        word_count = float(len(i.wordset.keys()))
        score = ((3-i.pos)/3.0)*1 + (len(i.Named_Entity_count)/word_count)*3 + (i.Numerical_count)*0.75 + (i.Summary_phrase_count)*2 + (word_count)*0.1
        Sentences.append(SenNode(score, i))
    sort_score = sorted(Sentences, reverse=True)
    summary = []
    for i in range(len(sort_score)*3/10 + 1):
        summary.append(sort_score[i].sentence.text)
    return "\n".join(summary)
    

def SummeryPhrases(text, score = 0):
    """
    Increses score of the sentences in case of summary phrases
    """
    summ_phra = [u"after all",
                 u"all in all",
                 u"all things considered",
                 u"briefly",
                 u"by and large",
                 u"in any case",
                 u"in any event",
                 u"in brief",
                 u"in conclusion",
                 u"on the whole",
                 u"in short",
                 u"in summary",
                 u"in the final analysis",
                 u"in the long run, on balance",
                 u"to sum up",
                 u"to summarize",
                 u"finally"]
    count = 0
    for phrase in summ_phra:
        if phrase in text.lower():
            count +=1
    return count

def repetitionWord(words):
    """
    Finding how many times a word repeats 
    """
    WordsSet = {}
    for word in set(words):
        if word[0] in stopwords.words('english'):
            continue
        WordsSet[word] = words.count(word)
    return WordsSet
 
if __name__ == "__main__":
    path = raw_input("Enter the path to a directory containing text files: ")
    output_path = raw_input("Enter the path to a directory for output: ")
    for filename in os.listdir(path):
        filepath = os.path.join(path, filename)
        if not os.path.exists(output_path):
            os.makedirs(output_path);
        output = os.path.join(output_path, filename)
        summary = ExtractDocument(filepath)
        fp = open(output, "w+")
        fp.write(summary.encode('utf8'))
