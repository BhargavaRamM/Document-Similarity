# Document-Similarity
Calculates document similarities between documents.

My code is attached in the other file. I implemented a simple vector space model and use the cosine similarity between the documents. 
I calculated the document value using the words and their frequencies. For a given document d, we can denote it as |d|. Then I considered
calculating the document values for all the other documents in the directory. Now we can use document values to calculate the similarity
between them. I used Cosine similarity between two documents d1 and d2 as follows:
                      Sim = d1*d2/|d1|*|d2|
The d1*d2 is a scalar product of the documents i.e., it checks if the documents have any words in common. 
This is a pretty basic approach to calculate the similarity between any two given documents. We can iterate the given document over the
directory and return all the documents that have a similarity. If there are no common words between two docs, then their scalar product
is going to be zero, hence, they are not similar. We can return a sorted list of the documents by returning the document with highest
similarity. 
Given enough time, we can use different methods which are more reliable and efficient. For example, we can use tf-idf approach. We can
use term frequencies of indexes and inverse document frequencies to implement more refined retrieval algorithms like Pivoted Length or
Okapi BM25 etc. to get the most relevant documents. Also, we can scale the number of documents by using these methods.  Coming to the
evaluation, we can use Precision and recall or F-1 to calculate the relevancy among the documents. 

Also, we can use another simple approach in my implementation by providing weights to terms rather than just using their frequencies. 
We can give less weights to more common words like “the” etc., and provide more “weights” to not so common words for example like
“extinguished” in the Poem 1. Thus, by doing it, we are providing more weightage to more important words.  This is a small optimization
we can use.  

