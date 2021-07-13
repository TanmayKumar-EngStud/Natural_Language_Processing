# Topic Modelling
- **Summary** : It is to efficiently analyze large volumes of text by clustering documents into topics.<br>
Large amount of text data is unlabeled.

- **Latent Dirichlet Allocation** : It is a probability distribution (LDA) that performs the following assumptions : <br>

1. Decide on the numbers of words N the document will have.
2. Choose topic mixture for the document 
3. Pick topic according to the multinomial distribution from the previous sample 

<br><br>
## It's practical implementation
- first we have to create a file which will consist of all the text paragraphs in a form of list.
- We have to use CountVectorizer in order to remove all the stop words and to allocate 
max_df and min_df (selecting a random state is optional)
- We have to then initialize LatentDilchletAllocation() with 'n_components = 7' 
which means that total number of list of topics that will be created will be decided. 
- These list of topics created holds the pobability of occurance of every word vector in 
that paragraph.
- After that we just have to fit and transform the LDA instance with our given data.
- After that we just have to create a CSV file which will contain the paragraphs and the allocation of those paragraphs with that particular topic.
