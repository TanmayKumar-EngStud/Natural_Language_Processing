from numpy.core.fromnumeric import argmax
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.decomposition import NMF
#import numpy as np
import pandas as pd
import os
import spacy
os.system('clear')
df = pd.read_csv('moviereviews.tsv', sep ='\t', encoding='UTF-8')

nlp = spacy.load('en_core_web_sm')

# CountVectorizer, TfidfTransformer, Fit_Transform
tfidf = TfidfVectorizer(max_df = 0.95, min_df = 2, stop_words='english')
newData =tfidf.fit_transform(df['review'].values.astype('U'))

# applying NMF
nmf = NMF(n_components = 20, random_state = 42)
nmf.fit(newData)
RelationSet =[]
for i, topic in enumerate(nmf.components_):
    print("Topic #{}:".format(i))
    tempSet =" ".join(tfidf.get_feature_names()[i] for i in topic.argsort()[:-10 - 1:-1])
    print(tempSet)
    RelationSet.append(tempSet)
total_result = nmf.transform(newData)

df['Category'] = total_result.argmax(axis= 1)

def getRelation(X):
    resultSet =[]
    for i in X :
        resultSet.append(RelationSet[i])
    return resultSet

df['Relation'] = getRelation(df['Category'])
df.to_csv("NewMovieReviewGenerated.tsv", sep ="\t")