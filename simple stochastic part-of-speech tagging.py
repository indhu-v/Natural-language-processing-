import random

class StochasticPOSTagger:
    def __init__(self, training_corpus):
        self.word_tag_probabilities = self.calculate_probabilities(training_corpus)

    def calculate_probabilities(self, training_corpus):
        word_tag_counts = {}
        tag_counts = {}

        for sentence in training_corpus:
            for word, tag in sentence:
                # Count occurrences of word-tag pairs
                word_tag_counts[(word, tag)] = word_tag_counts.get((word, tag), 0) + 1
                # Count occurrences of tags
                tag_counts[tag] = tag_counts.get(tag, 0) + 1

        # Calculate probabilities
        word_tag_probabilities = {pair: count / tag_counts[pair[1]] for pair, count in word_tag_counts.items()}

        return word_tag_probabilities

    def tag_sentence(self, sentence):
        tagged_sentence = []
        for word in sentence:
            possible_tags = [tag for (w, tag) in self.word_tag_probabilities.keys() if w == word]
            if possible_tags:
                selected_tag = random.choice(possible_tags)
            else:
                # If the word is unseen, assign a default tag (e.g., 'NOUN')
                selected_tag = 'NOUN'
            tagged_sentence.append((word, selected_tag))
        return tagged_sentence

# Example usage
training_corpus = [
    [('The', 'DET'), ('cat', 'NOUN'), ('is', 'VERB'), ('on', 'PREP'), ('the', 'DET'), ('mat', 'NOUN')],
    [('A', 'DET'), ('dog', 'NOUN'), ('is', 'VERB'), ('running', 'VERB')]
]

tagger = StochasticPOSTagger(training_corpus)

# Example sentence to tag
new_sentence = ['The', 'dog', 'is', 'running']

# Tag the sentence
tagged_sentence = tagger.tag_sentence(new_sentence)

# Display the result
print(tagged_sentence)
