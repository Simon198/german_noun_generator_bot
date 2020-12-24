import pandas as pd
import os

dir_path = os.path.abspath(os.path.dirname(__file__))

df = pd.read_csv(dir_path + '/nouns.csv')
nouns = [noun
    for noun in df['lemma'][177:90194]
    if (
        len(noun) > 1 and
        '-' not in noun and
        not noun.isupper()
    )
]

with open(dir_path + '/nouns.txt', 'wb') as file:
    content = ('\n'.join(nouns))
    file.write(content.encode('utf-8'))