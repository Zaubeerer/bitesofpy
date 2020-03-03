import os
import urllib.request
from collections import Counter

# data provided
tmp = os.getenv("TMP", "/tmp")
stopwords_file = os.path.join(tmp, 'stopwords')
harry_text = os.path.join(tmp, 'harry')
urllib.request.urlretrieve(
    'https://bites-data.s3.us-east-2.amazonaws.com/stopwords.txt',
    stopwords_file
)
urllib.request.urlretrieve(
    'https://bites-data.s3.us-east-2.amazonaws.com/harry.txt',
    harry_text
)


def get_harry_most_common_word():
    
    alphanumeric_word_counter = Counter()

    with open(stopwords_file) as f:
        stopwords = f.read().splitlines()

    stopwords.append("--")

    with open(harry_text) as f:
        harry_sentences = f.readlines()
        # TODO: rewrite this as generator OR with re 

    for sentence in harry_sentences:
        for word in sentence.split():
            word_lowercase = word.lower().strip().strip("!:;.,<>`~'")
            if word_lowercase not in stopwords:
                alphanumeric_word_counter[word_lowercase] += 1

    return alphanumeric_word_counter.most_common(1)[0]