## Part B Task 4
import re
import pandas as pd
import os
import sys
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
    print(res_ID)

main()
