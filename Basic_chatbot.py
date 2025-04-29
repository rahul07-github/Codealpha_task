import nltk
from nltk.tokenize import word_tokenize
from nltk.stem import PorterStemmer

# Download required tokenizer
nltk.download('punkt')

# Initialize stemmer
stemmer = PorterStemmer()

# Define some basic responses
responses = {
    'hello': 'Hello! How can I help you today?',
    'hi': 'Hi there! What can I do for you?',
    'name': 'I am a chatbot created using Python.',
    'weather': 'I am not sure, but I hope it’s sunny where you are!',
    'bye': 'Goodbye! Have a great day.',
    'thanks': 'You’re welcome!',
}

# Simple keyword matching function
def get_response(user_input):
    tokens = word_tokenize(user_input.lower())
    for word in tokens:
        stemmed = stemmer.stem(word)
        if stemmed in responses:
            return responses[stemmed]
    return "I'm not sure how to respond to that. Can you try something else?"

# Chat loop
def chatbot():
    print("Chatbot: Hi! I'm a simple chatbot. Type 'bye' to exit.")
    while True:
        user_input = input("You: ")
        if 'bye' in user_input.lower():
            print("Chatbot: Goodbye! 👋")
            break
        response = get_response(user_input)
        print("Chatbot:", response)

# Run the chatbot
if __name__ == "__main__":
    chatbot()
