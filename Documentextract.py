# -*- coding: utf-8 -*-
import sys
import nltk
import string
from collections import namedtuple
from nltk.tokenize import sent_tokenize
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
import re

Sentence = namedtuple('Sentence', ['text', 'wordset','Named_Entity_count', 'Summary_phrase_count'])
def ExtractDocument(File):
    """
    Takes input file and prints the summary
    """
    with open(File, "r") as inputfile:
        content = inputfile.read()
    content = content.replace('”','"').replace('“','"')
    sentences = sent_tokenize(content.decode('utf-8'))
    word_tokens = [word for word in word_tokenize(content.decode("utf-8"))
                   if word not in stopwords.words('english')
                   and word not in string.punctuation ]
    words = nltk.pos_tag(word_tokens)
    wordset = repetitionWord(words)
    sen = []
    for sentence in sentences:
        summ = SummeryPhrases(sentence)
        senwordSet={}
        for word in wordset.keys():
            if word[0] in sentence:
                senwordSet[word] = wordset[word]
        # Finding Named Entity Words
        Num_Named_entity= 0
        for word in senwordSet:
            if word[1]=="NNP":
                Num_Named_entity += 1
        sen.append(Sentence(sentence, senwordSet, Num_Named_entity, summ))
    for i in sen:
        print i
    print "The Summary\n"
    

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
    ExtractDocument(sys.argv[1])
