from textblob import TextBlob
import nltk
nltk.download('punkt_tab')

text = """
bad is better than good
"""


# text = """
# The titular threat of The Blob has always struck me as the ultimate movie
# monster: an insatiably hungry, amoeba-like mass able to penetrate
# virtually any safeguard, capable of--as a doomed doctor chillingly
# describes it--"assimilating flesh on contact.
# Snide comparisons to gelatin be damned, it's a concept with the most
# devastating of potential consequences, not unlike the grey goo scenario
# proposed by technological theorists fearful of
# artificial intelligence run rampant.
# """

blob = TextBlob(text)

# Part-of-speech tags
print(blob.tags)

# Noun phrases
print(blob.noun_phrases)

# Sentiment analysis for each sentence
for sentence in blob.sentences:
    print(f"Sentence: {sentence}")
    print(f"Sentiment Polarity: {sentence.sentiment.polarity}")
