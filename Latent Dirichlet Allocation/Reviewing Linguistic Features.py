import spacy
import os
os.system('clear')
nlp = spacy.load('en_core_web_sm')
doc = nlp(u"This is a small sample sentene.")
Text = "Text"
Pos = "Pos"
Tag = "Tag"
Stop = "Is Stop"
Dep = "DEP"
print(f"{Text:{10}} {Pos:{10}} {Tag :{10}} {Dep:{10}}{Stop:{10}}")
for Text in doc:
    print(f'{Text.text:{10}} {Text.pos_:{10}} {Text.tag_ :{10}} {Text.dep_:{10}} {Text.is_stop}')
print('\n')

Text = "Text"
Pos = "Pos"
Tag = "Tag"
Stop = "Is Stop"
print(f"{Text:{10}} {Pos:{20}} {Tag :{35}} {Stop :{20}}")
for Text in doc:
    print(f'{Text.text:{10}} {spacy.explain(Text.pos_):{20}} {spacy.explain(Text.tag_) :{35}} {spacy.explain(Text.is_stop)}')


print('\n')
print('\n')


from nltk.corpus import words
import enchant
dictionary = enchant.Dict("en_US")
# checking the word in the dictionary
print(dictionary.check("Hello"))