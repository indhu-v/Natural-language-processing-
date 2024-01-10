import nltk

# Define a Probabilistic Context-Free Grammar
pcfg_grammar = nltk.PCFG.fromstring("""
    S -> NP VP [1.0]
    NP -> Det N [0.5] | N [0.3] | N PP [0.2]
    VP -> V NP [0.9] | VP PP [0.1]
    Det -> 'the' [0.8] | 'a' [0.2]
    N -> 'dog' [0.4] | 'cat' [0.3] | 'park' [0.3]
    V -> 'chased' [0.7] | 'caught' [0.3]
    PP -> P NP [1.0]
    P -> 'in' [0.6] | 'on' [0.4]
""")

# Create a PCFG parser
pcfg_parser = nltk.ViterbiParser(pcfg_grammar)

# Example sentence
sentence = "the dog chased the cat in the park"

# Tokenize the sentence
tokens = nltk.word_tokenize(sentence)

# Parse the sentence using the PCFG parser
for tree in pcfg_parser.parse(tokens):
    tree.pretty_print()
    print("Probability:", tree.prob())
