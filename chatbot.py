def chatbot_response(user_input):
    user_input = user_input.lower()
    
    if "hello" in user_input or "hi" in user_input:
        return "Hello! How can I assist you today?"
    elif "how are you" in user_input:
        return "I'm just a program, but I'm doing great! How about you?"
    elif "what is your name" in user_input:
        return "I'm a chatbot created by OpenAI. You can call me Chatbot."
    elif "bye" in user_input or "exit" in user_input:
        return "Goodbye! Have a great day!"
    else:
        return "Sorry, I didn't understand that. Can you ask something else?"

def main():
    print("Chatbot: Hi there! Type 'exit' to end the conversation.")
    while True:
        user_input = input("You: ")
        if user_input.lower() in ["exit", "bye"]:
            print("Chatbot: Goodbye!")
            break
        response = chatbot_response(user_input)
        print("Chatbot:", response)

if __name__ == "__main__":
    main()

