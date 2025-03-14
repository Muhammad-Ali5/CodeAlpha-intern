def chatbot():
    print("Hello! I'm your chatbot. Type 'quit' to exit.")
    
    # Expanded response dictionary with more commands
    responses = {
        "hi": "Hey there! What’s up?",
        "hello": "Hi! How can I brighten your day?",
        "how are you": "I’m fantastic, thanks for asking! How are you holding up?",
        "what’s your name": "I’m Grok, your friendly AI companion. What’s yours?",
        "bye": "Catch you later! Have a good one!",
        "what can you do": "I can chat, answer questions, tell jokes, or just keep you company. What do you want to try?",
        "tell me a joke": "Why don’t skeletons fight each other? Because they don’t have the guts!",
        "how’s the weather": "I don’t have a window, but I bet it’s nicer where you are! What’s it like outside?",
        "what’s the time": "I’m timeless, but if you tell me your timezone, I can guess! What’s your local time?",
        "i’m bored": "Let’s fix that! Want a story, a joke, or maybe a fun fact?",
        "fun fact": "Did you know octopuses have three hearts and can change color to blend in? Cool, right?",
        "thanks": "You’re welcome! Anything else I can do for you?"
    }
    
    while True:
        user_input = input("You: ").lower().strip()
        
        if user_input == "quit":
            print("Chatbot: Goodbye for now!")
            break
        
        # Check if user input matches any key in responses
        response = responses.get(user_input, "Hmm, I’m not sure what you mean. Try something like 'hi', 'tell me a joke', or 'fun fact'!")
        print(f"Chatbot: {response}")

# Run the chatbot
if __name__ == "__main__":
    chatbot()