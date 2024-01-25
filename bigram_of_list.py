''' Question No. 72 (Practise set-3) '''
from nltk import ngrams as ng
from nltk.tokenize import word_tokenize
li=input("Enter the word-\t").split(",")
# li=['Sum all the items in a list','Find the second smallest number in a list']
nli=[]
for i in li:
    for j in ng(word_tokenize(i), 2):
        nli.append(j)

print(nli)
