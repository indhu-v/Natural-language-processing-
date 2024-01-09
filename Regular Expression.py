import re

def find_emails(text):
    # Define a regular expression pattern for matching email addresses
    email_pattern = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'

    # Use re.findall to find all matches in the text
    matches = re.findall(email_pattern, text)

    return matches

def main():
    # Example text containing email addresses
    sample_text = """
    Here are some email addresses:
    john.doe@example.com
    alice_smith123@gmail.com
    support@company.com
    """

    # Find and print email addresses in the text
    email_addresses = find_emails(sample_text)
    
    if email_addresses:
        print("Found email addresses:")
        for email in email_addresses:
            print(email)
    else:
        print("No email addresses found in the text.")

if __name__ == "__main__":
    main()
