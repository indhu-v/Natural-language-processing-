import nltk
from nltk import pos_tag, ne_chunk
from nltk.tokenize import word_tokenize
from nltk.chunk import conlltags2tree, tree2conlltags

nltk.download('punkt')
nltk.download('maxent_ne_chunker')
nltk.download('words')

def extract_noun_phrases(sentence):
    words = word_tokenize(sentence)
    tagged_words = pos_tag(words)
    chunk_tree = ne_chunk(tagged_words)
    iob_tags = tree2conlltags(chunk_tree)
    
    noun_phrases = []
    for tag in iob_tags:
        if tag[1] == 'NN' or tag[1] == 'NNS' or tag[1] == 'NNP' or tag[1] == 'NNPS':
            noun_phrases.append(tag[0])
    
    return noun_phrases

def main():
    sentence = input("Enter a sentence: ")
    noun_phrases = extract_noun_phrases(sentence)
    
    print("\nNoun Phrases:")
    for phrase in noun_phrases:
        print("-", phrase)

if __name__ == "__main__":
    main()
