# Newspaper Data Abstraction and word Vectorization
In this project I have collected the data from the Indian news paper site<hr>
[Hindustan Times](https://www.hindustantimes.com/opinion)
<br>

Steps followed in the over all project : 
- open the newspaper's saved html file in the from of a file buffer
- **abstract** all the titles of the news in the from of list using **Regular Expression**
```python
Title_List =re.findall("(?<=\"name\":\").*(?=\",\n)",RawText.read())
#Find all the set for Text which is in between=> "name": and "\n
```
- **import** all the necessary gensim models 
```python
from gensim.models.callbacks import CallbackAny2Vec
from gensim.models import Word2Vec
```
  - Here CallbackAny2Vec is used to find the **loss and retrieved after every epoch**
  - For this I have also **added a class** to get latest training loss after every epoch
  - After that I have **initialized the Word2Vector**
```python
w2v = Word2Vec(vector_size=100, # size of the w2v is allocated to be 300
               window = 5,      # window size assigned is assumed to be 5
               min_count =1,    # words must come atleast 1 time in the entire corpus
               workers = 4,     # maximum 4 threads are required to run in parallel
               sg =1,           # we are using Skip gram model
               negative = 5,    # atmost 5 negative words are acceptable
               sample = 1e-5)   # Sampling rate = 10^-5
```
  - After initializing the Word2Vector I **build the Vocabulary**
  - After building up the vocabulary to a model we have to **train the model**
  - For Training I have considered these following conditions :-
```python
w2v.train(Title_List,
          total_examples=w2v.corpus_count,
          epochs =1001,
          report_delay=1,
          compute_loss=True,
          callbacks=[callback()])
```
  - After Training the model I am **saving the model**
  
