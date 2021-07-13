from sklearn.feature_extraction.text import CountVectorizer
import spacy
import pandas as pd
import os
os.system('clear')
# This program is to understand the concept of Topic modelling using 
# Latent Dirichlet Allocation
nlp = spacy.load('en_core_web_sm')

#print(nlp.Defaults.stop_words)
fileTemp = open("shakesphere.txt",'r')

# creating a temporary vocabulary 
data = fileTemp.read()
vocab = {}
for text in data.lower().split(): 
    if text not in vocab:
        # Add the text to the vocab 
        vocab[text] = 1
    else:
        # If the text is already in the vocab, add 1 to the count 
        vocab[text] += 1

for keys, values in sorted(vocab.items(), key=lambda x: x[1], reverse=True)[:19]:
    if nlp.vocab[str(keys)].is_stop:
        continue
    else:
        nlp.Defaults.stop_words.add(str(keys))
fileTemp.close()

file = open('shakesphere.txt','r')
cVector = CountVectorizer(max_df=0.95, min_df=3, stop_words=nlp.Defaults.stop_words)

#creating a paragraph from the file
doc = file.read()
vector = cVector.fit_transform([text for text in doc.split('\n\n')])

from sklearn.decomposition import LatentDirichletAllocation
LDA = LatentDirichletAllocation(n_components = 7)
LDA.fit(vector)

for index,topic in enumerate(LDA.components_):
    print(f'THE TOP 10 WORDS FOR TOPIC #{index}')
    print([cVector.get_feature_names()[i] for i in topic.argsort()[-10:]])
    print('\n')
# these are the top 10 topics which the machine will use 
# in order to classify the paragraphs we have in the file
topicSet = []
for index, topic in enumerate(LDA.components_):
    miniSet =[]
    for i in topic.argsort()[-10:]:
        miniSet.append(cVector.get_feature_names()[i])
    topicSet.append(miniSet)    

topic_results = LDA.transform(vector)



#we have to create a CSV file
dataFrame = {'Text':doc.split('\n\n')}
df = pd.DataFrame(dataFrame)
df["Topic"] = topic_results.argmax(axis=1)
df.to_csv("NewCSV.tsv", sep='\t', index=True, header=False, encoding='utf-8')

file.close()