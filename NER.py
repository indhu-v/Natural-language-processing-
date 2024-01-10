import spacy

def perform_ner(text):
    # Load the English language model
    nlp = spacy.load("en_core_web_sm")

    # Process the text
    doc = nlp(text)

    # Extract named entities
    entities = [(ent.text, ent.label_) for ent in doc.ents]

    return entities

# Example text
sample_text = "Apple Inc. is a technology company headquartered in Cupertino, California. Steve Jobs co-founded Apple in 1976."

# Perform NER
named_entities = perform_ner(sample_text)

# Display the results
print("Named Entities:")
for entity, label in named_entities:
    print(f"{entity} - {label}")
