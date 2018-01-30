## Natural Language Processing

NLTK - Natural Language Toolkit
popular python package

Tokenizing
* by word tokenizers
* by sentence tokenizers

Lexicon and corpora

Corpora: body of text example: medical
lexicon: words and their meanings
example: normal english speak vs investors speaking
like bullish means positive about the markets and in plain english it means animal.

```python
from nltk.tokenize import sent_tokenize, word_tokenize

example = "Hi, there. I am writing some text. I love tea in rainy weather."

print(sent_tokenize(example))

print(word_tokenize(example))
```

## Stop words


```python
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

example = "this is a random sentence we are about to test"

my_stop_words = set(stopwords.words("english"))

words = word_tokenize(example)

filtered_sentence = []

for w in words:
  if w not in my_stop_words:
    filtered_sentence.append(w)

print(filtered_sentence)

```

## Stemming
