
print("Hello! I am ChatBot 🤖. Type 'bye' to exit.\n")

while True:
    user_input = input("You: ").lower()  

    if user_input == "hi" or user_input == "hello":
        print("Bot: Hello there! How can I help you today?")
    elif "how are you" in user_input:
        print("Bot: I'm just a program, but I'm feeling smart today!")
    elif "your name" in user_input:
        print("Bot: I'm a simple rule-based chatbot.")
    elif "bye" in user_input:
        print("Bot: Goodbye! Have a nice day.")
        break
    else:
        print("Bot: Sorry, I don't understand that.")