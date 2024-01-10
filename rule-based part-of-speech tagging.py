import nltk

patterns = [
    (r'\d+', 'CD'),               # cardinal numbers
    (r'[a-zA-Z]+(ed|ing|es|s)?$', 'VB'),  # verbs
    (r'[a-zA-Z]+(ly|ment)$', 'RB'),       # adverbs
    (r'[a-zA-Z]+(able|ible)$', 'JJ'),     # adjectives
    (r'\b(a|an|the)\b', 'DT'),            # determiners
    (r'[a-zA-Z]+', 'NN')                  # nouns
]

regexp_tagger = nltk.RegexpTagger(patterns)
text = "The quick brown fox jumps over the lazy dog"
tokens = nltk.word_tokenize(text)
tags = regexp_tagger.tag(tokens)
print(tags)
