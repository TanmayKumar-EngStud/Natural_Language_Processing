import gensim
from gensim.models import Word2Vec, word2vec
from gensim.models.callbacks import CallbackAny2Vec
import os

os.system('clear')
# Creating a class to fetch loss after every epoch
class callback(CallbackAny2Vec):
    def __init__(self) -> None:
        self.epoch= 0
    def on_epoch_end(self, model):
        loss = model.get_latest_training_loss()

w2v = Word2Vec(vector_size=100, # size of the w2v is allocated to be 300
                        window = 5, # window size assigned is assumed to be 5
                        min_count =1, # words must come atleast 1 time in the entire corpus
                        workers = 4, # maximum 4 threads are required to run in parallel
                        sg =1, # we are using Skip gram model
                        negative = 5, # atmost 5 negative words are acceptable
                        sample = 1e-5) # Sampling rate = 10^-5

#Building up the vocbulary
data = open('/home/tanmay/Desktop/NLP Workflow/Working with a big data/collected_data.txt', mode = 'r')
data = data.readline()
w2v.build_vocab(data)
print(data)

#now we have to train the model
w2v.train(data,
          total_examples=w2v.corpus_count,
          epochs= 1001,
          report_delay=1,
          compute_loss=True,
          callbacks= [callback()])
w2v.save('/home/tanmay/Desktop/NLP Workflow/Word2vector modeling/w2v_model.h5')
