import openai

# Set your OpenAI GPT-3 API key
openai.api_key = 'YOUR_API_KEY'

def generate_text(prompt, max_tokens=100):
    response = openai.Completion.create(
        engine="text-davinci-003",  # You can choose other engines as well
        prompt=prompt,
        max_tokens=max_tokens
    )

    generated_text = response['choices'][0]['text']
    return generated_text

def main():
    prompt = input("Enter a prompt: ")
    generated_text = generate_text(prompt)

    print("\nGenerated Text:")
    print(generated_text)

if __name__ == "__main__":
    main()
