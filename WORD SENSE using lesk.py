from nltk.corpus import wordnet
from nltk.tokenize import word_tokenize
from nltk.wsd import lesk

def perform_word_sense_disambiguation(sentence, target_word):
    # Tokenize the sentence
    words = word_tokenize(sentence)

    # Perform word sense disambiguation using the Lesk algorithm
    sense = lesk(words, target_word)

    if sense:
        return sense.name(), sense.definition()
    else:
        return None

# Example sentence and target word
example_sentence = "He went to the bank to deposit some money."
target_word = "bank"

# Perform word sense disambiguation
result = perform_word_sense_disambiguation(example_sentence, target_word)

# Display the result
if result:
    sense_name, sense_definition = result
    print(f"Sense Name: {sense_name}")
    print(f"Sense Definition: {sense_definition}")
else:
    print(f"No sense found for the word '{target_word}' in the given context.")
