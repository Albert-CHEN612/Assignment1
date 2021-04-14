## Part B Task 1
import re
import pandas as pd
import os
import argparse

def main():
    parser = argparse.ArgumentParser(description='Process a csv file name.')
    parser.add_argument('filename', type=str)
    args = parser.parse_args()

    filenames = []
    ids = []
    for root, dirs, files in os.walk("./cricket"):
        #walk all text files
        for name in files:
            path = os.path.join(root, name)
            f = open(path, 'r')
            text = f.read()
            #use re to seach id
            pattern = r"[A-Z]{4}-[0-9]{3}[A-Z]{0,1}"
            result = re.search(pattern, text)
            filenames.append(name)
            ids.append(result.group())
    df = pd.DataFrame(columns=['filename', 'documentID'])
    df['filename'] = filenames
    df['documentID'] = ids
    df.to_csv(args.filename)
    
main()