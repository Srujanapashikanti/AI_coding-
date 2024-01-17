import random

responses = {
    "hello": ["Hey!", "Hello!", "Hi there!"],
    "how are you": ["I am fine, what about you?", "I am just a programmer, but I am fine. How about you?", "I don't have feelings!"],
    "goodbye": ["Goodbye!", "See you later, take care", "Take care"],
    "default": ["Sorry, I am not sure", "Can you please provide more information", "Sorry, I don't understand that"],
}

def get_response(user_input):
    user_input = user_input.lower()
    for key in responses:
        if key in user_input:
            return random.choice(responses[key])
    return random.choice(responses["default"])

print("Chatbot: Hi! How can I help you today? (type exit to end)")

while True:
    user_input = input("You: ")
    if user_input.lower() == "exit":
        print("Chatbot: Goodbye!")
        break
    response = get_response(user_input)
    print("Chatbot:", response)