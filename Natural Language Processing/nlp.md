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
In linguistic morphology and information retrieval, stemming is the process of reducing inflected (or sometimes derived) words to their word stem, base or root form—generally a written word form. The stem need not be identical to the morphological root of the word; it is usually sufficient that related words map to the same stem, even if this stem is not in itself a valid root. Algorithms for stemming have been studied in computer science since the 1960s. Many search engines treat words with the same stem as synonyms as a kind of query expansion, a process called conflation.

Example:
I was eating an Apple.
I ate an Apple.
Both mean the same and the word eating ate should be mapped to a single root.


```python
from nltk.stem import PorterStemmer
from nltk.tokenize import word_tokenize

ps = PorterStemmer()

words = ["python", "pythoner", "pythoning", "pythoned", "pythonly"]

for w in words:
  print(ps.stem(w))

new_text = "it is very important to be pythonly, while you are pythoning with python. All pythoners have pythoned for long time"

words = word_tokenize(new_text)

for w in words:
  print(ps.stem(w))
```

## Part of Speech Tagging

```python
import nltk
from nltk.corpus import state_union
from nltk.tokenize import PunktSentenceTokenizer



```
