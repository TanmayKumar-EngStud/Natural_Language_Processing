from numpy.core.numeric import NaN
import pandas as pd
import numpy as np
import os
os.system('clear')
df = pd.read_csv('amazonreviews.tsv', sep = '\t')
#df['review']
#we have to extract feature form this column
#thus 
rawData = [val for val in df['review']] 
data = []
 
for value in rawData:
    if value is NaN:
        continue
    else:
        val = value.split()
    data.append(val)


import re

filteredData= [[re.findall('[a-zA-Z]+',text.lower()) for text in reviews]for reviews in data]

i=0
vocab = {}
# building a vocabulary
for review in filteredData:
    for words in review:
        for word in words:    
            if word in vocab:
                continue
            else:
                vocab[word] = i + 1
                i+= 1 
print("this is vocabulary length from 1\'st tsv file:\t",len(vocab))
#now every word has a new ID 
# vocabulary is made.
df = pd.read_csv('moviereviews.tsv', sep = '\t')


rawData = [value for value in df['review']] 
data = []
 
for value in rawData:
    if value is NaN:
        continue
    else:
        val = value.split()
    data.append(val)


filteredData= [[re.findall('[a-zA-Z]+',text.lower()) for text in reviews]for reviews in data]

i=0
# building a vocabulary
for review in filteredData:
    for words in review:
        for word in words:    
            if word in vocab:
                continue
            else:
                vocab[word] = i + 1
                i+= 1

print("this is vocabulary length from 2\'nd tsv file:\t",len(vocab))
df = pd.read_csv('moviereviews2.tsv', sep = '\t')

rawData = [values for values in df['review']]

data = []
 
for value in rawData:
    if value is NaN :
        continue
    else:
        val = value.split()
    data.append(val)



filteredData= [[re.findall('[a-zA-Z]+',text.lower()) for text in reviews]for reviews in data]

i=0
# building a vocabulary
for review in filteredData:
    for words in review:
        for word in words:    
            if word in vocab:
                continue
            else:
                vocab[word] = i + 1
                i+= 1 
print("this is vocabulary length from 3\'rd tsv file:\t",len(vocab))


#  after building the vocabulary
one = ['raw.txt']+[0]*len(vocab)
cleaner = open('raw.txt','w')
cleaner.write('')
cleaner.close()
with open('raw.txt','a') as dictionary:
    for vocabulary in vocab:
        dictionary.write(f"{vocabulary :{20}}{vocab[vocabulary] :{10}}\n")