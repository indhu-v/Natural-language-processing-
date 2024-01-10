class EarleyItem:
    def __init__(self, production, dot_position, start_position, end_position):
        self.production = production
        self.dot_position = dot_position
        self.start_position = start_position
        self.end_position = end_position

    def __eq__(self, other):
        return (
            self.production == other.production and
            self.dot_position == other.dot_position and
            self.start_position == other.start_position and
            self.end_position == other.end_position
        )

    def __repr__(self):
        return f"{self.production} ({self.start_position}, {self.end_position})"


def predict(grammar, item, chart):
    for production in grammar:
        if production[0] == item.production[item.dot_position]:
            new_item = EarleyItem(production, 0, item.end_position, item.end_position)
            chart[item.end_position].append(new_item)


def scan(word, item, chart):
    if item.dot_position < len(item.production) and item.production[item.dot_position] == word:
        new_item = EarleyItem(item.production, item.dot_position + 1, item.start_position, item.end_position + 1)
        chart[item.end_position + 1].append(new_item)


def complete(item, chart):
    for other_item in chart[item.start_position]:
        if other_item.dot_position < len(other_item.production) and \
                other_item.production[other_item.dot_position] == item.production[0]:
            new_item = EarleyItem(other_item.production, other_item.dot_position + 1, other_item.start_position,
                                  item.end_position)
            if new_item not in chart[item.end_position]:
                chart[item.end_position].append(new_item)


def earley_parse(sentence, grammar):
    chart = [[] for _ in range(len(sentence) + 1)]
    start_production = grammar[0]
    start_item = EarleyItem(start_production, 0, 0, 0)
    chart[0].append(start_item)

    for i in range(len(sentence) + 1):
        for item in chart[i]:
            if item.dot_position < len(item.production) and isinstance(item.production[item.dot_position], str):
                scan(sentence[i], item, chart)
            elif item.dot_position < len(item.production):
                predict(grammar, item, chart)
            else:
                complete(item, chart)

    for item in chart[len(sentence)]:
        if item.production == start_production and item.dot_position == len(start_production):
            return True

    return False


# Example grammar and sentence
example_grammar = [
    ('S', ['NP', 'VP']),
    ('NP', ['Det', 'N']),
    ('VP', ['V', 'NP']),
    ('Det', ['the']),
    ('N', ['dog', 'cat']),
    ('V', ['chased', 'caught']),
]

example_sentence = "the dog chased a cat"

# Run the Earley parser
result = earley_parse(example_sentence.split(), example_grammar)

# Display the result
if result:
    print("Parsing successful!")
else:
    print("Parsing failed.")
