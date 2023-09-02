import random

# Define a dictionary with possible responses
responses = {
    "hello": ["Hi there!", "Hello!", "Hey!"],
    "how are you": ["I'm just a bot, but I'm here to help!", "I don't have feelings, but thanks for asking!", "I'm operational and ready to assist!"],
    "bye": ["Goodbye!", "Farewell!", "Have a great day!"],
    "who is the p.m of india" : ["Mr.Narendra Modi"]
}

def res(message):
    message = message.lower()
    if message in responses:
        return random.choice(responses[message])
    else:
        return "I'm not sure how to respond to that."

# Main loop
while True:
    user_input = input("You: ")
    if user_input.lower() == "exit":
        print("Bot: Goodbye!")
        break
    response = res(user_input)
    print("Bot:", response)
