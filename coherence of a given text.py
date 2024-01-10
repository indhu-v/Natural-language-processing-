from gensim.summarization import summarize

def evaluate_coherence(text):
    coherence_score = summarize(text, ratio=0.5)  # Adjust the ratio as needed
    print("\nCoherence Score:")
    print(coherence_score)

def main():
    text = input("Enter a text: ")
    evaluate_coherence(text)

if __name__ == "__main__":
    main()
