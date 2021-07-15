import re
import os

os.system('clear')

RawText = open("/home/tanmay/Desktop/NLP Workflow/Working with newspaper/Hindustan Times.txt", 'r')

# Now we are going to select the text that is the title of the story
'''
Things to observe for the title of the story 
1. It is in the form of a hyperlink <a>
2. It has some article ID for Example :-> data-articleid="101626259319808" in the a hyper tag
3. Words selected have meanings
'''
#Thus we will use this as a resource in order to detect what is the title of that perticular article
#We are going to store this as a form of list.

Title_List =re.findall("(?<=\"name\":\").*(?=\",\n)",RawText.read())

print("Here is the list of Headlines...\n")
for title in Title_List:
    print(title)

#Now the list is being retrieved 
#We have to use this retrieved Data for creating a vectors
from gensim.models.callbacks import CallbackAny2Vec
from gensim.models import Word2Vec
class callback(CallbackAny2Vec):
    def __init__(self):
        self.epoch = 1
    def on_epoch_end(self,model):
        loss = model.get_latest_training_loss()

        if self.epoch == 0:
            print(f"Loss after epoch {self.epoch}: {loss}")
        elif self.epoch%100 == 0:
            print(f"Loss after epoch {self.epoch}: {loss - self.loss_previous_step}")
        self.epoch+=1
        self.loss_previous_step = loss

w2v = Word2Vec(vector_size=100, # size of the w2v is allocated to be 300
                        window = 5, # window size assigned is assumed to be 5
                        min_count =1, # words must come atleast 1 time in the entire corpus
                        workers = 4, # maximum 4 threads are required to run in parallel
                        sg =1, # we are using Skip gram model
                        negative = 5, # atmost 5 negative words are acceptable
                        sample = 1e-5) # Sampling rate = 10^-5
print("Word2Vec model is instantiated.")

print("\n\nNow Building the model's Vocabulary so that \nVocabulary is used while training the model.")
w2v.build_vocab(Title_List)
print("\nVocabulary building is complete")


import time

print("\n\nNow training the model...\n")
start = time.time()
w2v.train(Title_List,
          total_examples=w2v.corpus_count,
          epochs =1001,
          report_delay=1,
          compute_loss=True,
          callbacks=[callback()])
end = time.time()
total_time = start - end
print("\n\nTraining completed!!")
print(f"Total time taken is : {total_time}sec")

w2v.save('w2v_model.h5')