original_sentence = "Hi Jimmy, If the time is right, I was looking to reach out for an introduction to ServiceNow for you/WesTrac and to share how we're promoting innovation and automation in organisations throughout Australia and around the world. For some context, ServiceNow provides a service-automation platform designed to consolidate all service, asset and operational applications on to a single system of record, to reduce cost and complexity across the business whilst improving user experiencea and visibility.We are continuously recognised as industry leaders in this space by independent assements such as The Gartner Magic Quadrant. We had been engaged with your colleague Dale Wright before he moved to APM. Not sure if you have ever had an introduction to ServiceNow and are familiar with the architecture, platform features and modules that go beyond the traditional ITSM? I’ve included a case study on Knorr-Bremse here; there’s also around 100 enterprise grade customer case stud"
import nltk
nltk.download()

from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

example = "this is a random sentence we are about to test"

my_stop_words = set(stopwords.words("english"))

words = word_tokenize(original_sentence)

filtered_sentence = []

for w in words:
  if w not in my_stop_words:
    filtered_sentence.append(w)

print(filtered_sentence)
