from textblob import TextBlob
#import nlkt
#nlkt.download('punkt')

wiki = TextBlob("Python is a high level, general purpose programming language.")
print(wiki.tags)
print(wiki.noun_phrases)

# sentiment analysis

testimonial = TextBlob("textblob is very simple to use. It is a great tool")

print(testimonial.sentiment)
