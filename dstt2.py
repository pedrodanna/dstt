#Importing NLTK methods 
import nltk

#Importing sample text
with open('data\data.txt', 'r') as file:
    text = file.read().replace('\n', '')
    
#Sentence Tokenization
sentences = nltk.tokenize.sent_tokenize(text)

#Word Tokenization
words = nltk.tokenize.word_tokenize(text)

#Frequency Distribution
freq = nltk.probability.FreqDist(words)
    
print(freq.most_common(7))