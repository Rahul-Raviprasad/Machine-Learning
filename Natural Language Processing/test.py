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

     # chunked.draw()
  except Exception as e:
    print(str(e))


process_content()
