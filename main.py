import nltk
from nltk.chat.util import Chat, reflections

nltk.download('punkt')

pairs = [
    [
        r"my name is (.*)",
        ["Hello %1, How can I help you today?",]
    ],
    [
        r"hi|hey|hello",
        ["Hello!", "Hey there!",]
    ],
    [
        r"what is your name?",
        ["I am a chatbot .",]
    ],
    [
        r"how are you?",
        ["I'm doing well, thank you! How can I assist you?",]
    ],
    [
        r"tell|joke",
        ["Your Love Life...:-)"]
    ],
    [
        r"sorry (.*)",
        ["It's okay, no need to apologize.",]
    ],
    [
        r"I am (.*) (good|well|okay|ok)",
        ["Nice to hear that! How can I help you today?",]
    ],
    [
        r"quit|bye",
        ["Bye for now. See you soon!",]
    ],
    [
        r"(.*)",
        ["I'm not sure I understand. Can you please clarify?",]
    ]
]

chatbot = Chat(pairs, reflections)

def chatbot_conversation():
    print("Hi! I am your chatbot. Type 'quit' to exit.")
    while True:
        user_input = input("> ")
        if user_input.lower() == "quit":
            print("Bye for now. See you soon!")
            break
        response = chatbot.respond(user_input)
        print(response)

if __name__ == "__main__":
    chatbot_conversation()
