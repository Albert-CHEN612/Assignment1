## Part B Task 5
import re
import os
import sys
import pandas as pd
import nltk


import argparse

def preprocessing(text):
    # Remove all non-alphabetic characters
    text = re.sub(r"[^a-zA-Z \n\t]", '', text)
    # Convert all spacing characters such as tabs and newlines to whitespace
    text = text.replace("\t", " ")
    text = text.replace("\n", " ")
    # ensure that only one whitespace character exists between each word
    text = " ".join(text.split())
    # Change all uppercase characters to lower case
    text = text.lower()
    return text

def main():
    parser = argparse.ArgumentParser(description='Process a text file name.')
    parser.add_argument('keywords', type=str, nargs='+')
    args = parser.parse_args()
    #read csv file
    df = pd.read_csv("partb1.csv")
    filename = df['filename']
    docID = df['documentID']
    res_ID = []
    
    #porter stemmer
    porter_stemmer = nltk.stem.porter.PorterStemmer()
    #articles
    articles = []
    for i in range(len(docID)):
        #open file and preprocessing text
        text = open("./cricket/" + filename[i]).read()
        text = preprocessing(text)
        words = text.split()
        # stemmer sentence words
        words = [porter_stemmer.stem(w) for w in words]
        #match keywords
        flag = True
        for key_word in args.keywords:
            # stemmer key word
            key_word = porter_stemmer.stem(key_word.lower())
            if key_word not in words:
                flag = False
                break
        if flag:
            res_ID.append(docID[i])
            articles.append(words)
    
    # enable documents to be ranked
    all_word_lst = [w for text in articles for w in text]
    tc = nltk.TextCollection(all_word_lst)
    scores = []
    for i in range(len(articles)):
        score = 0.0
        for word in [porter_stemmer.stem(w.lower()) for w in args.keywords]:
            score += tc.tf_idf(word, articles[i])
        scores.append(score)
    
    #sort
    res_lst = []
    for i in range(len(scores)):
        res_lst.append((scores[i], res_ID[i]))
    res_lst = sorted(res_lst, key=lambda x: x[0], reverse=True)
    #print result
    print("documentID score")
    for i in range(len(scores)):
        print("{} {:.4f}".format(res_lst[i][1],res_lst[i][0]))
main()
