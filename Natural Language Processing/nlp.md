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

train_text = state_union.raw("2005-GWBush.txt")
sample_text = state_union.raw("2006-GWBush.txt")

custom_sent_tokenizer = PunktSentenceTokenizer(train_text)

tokenized = custom_sent_tokenizer.tokenize(sample_text)

def process_content():
  try:
    for i in tokenized:
      words = nltk.word_tokenize(i)
      tagged = nltk.pos_tag(words)
      print(tagged)
  except Exception as e:
    print(str(e))


process_content()

```

## Chunking

Chunking in Natural Language Processing (NLP) is the process by which we group various words together by their part of speech tags.

In chunking we will be using a lot of modifier from the regex in python.

```python
import nltk
from nltk.corpus import state_union
from nltk.tokenize import PunktSentenceTokenizer

train_text = state_union.raw("2005-GWBush.txt")
sample_text = state_union.raw("2006-GWBush.txt")

custom_sent_tokenizer = PunktSentenceTokenizer(train_text)

tokenized = custom_sent_tokenizer.tokenize(sample_text)

def process_content():
  try:
    for i in tokenized:
      words = nltk.word_tokenize(i)
      tagged = nltk.pos_tag(words)

      # RB is any adverb, we got tagging from the part  of speech tagging, using regular expression below for any adverb
      # NNp is proper noun, VB is verb, NN is noun
      chunkGram = """Chunk: {<RB.?>*<VB.?>*<NNP><NN>?} """

      chunkParser = nltk.RegexpParser(chunkGram)
      chunked = chunkParser.parse(tagged)
      print(chunked)
  except Exception as e:
    print(str(e))


process_content()

```

## Chinking
It is a part of the chunking process with natural language processing with NLTK. A chink is what we wish to remove from the chunk. We define a chink in a very similar fashion compared to how we defined the chunk.

```python
# }<VB.?|IN>{  line says remove all the verbs and prepositions
chunkGram = """Chunk: {<RB.?>*<NNP><NN>?} }<VB.?|IN>{ """
```
## Named Entity Recognition
