# Base class
class Agent:
    def speak(self):
        print("I am a generic AI agent.")

# Child class inheriting from Agent


class ChatBot(Agent):
    def speak(self):  # Overriding
        print("Hello! I am a specialized ChatBot.")


bot = ChatBot()
bot.speak()  # Uses the overridden method
