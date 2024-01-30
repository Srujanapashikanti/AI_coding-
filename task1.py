import tkinter as tk
from tkinter import scrolledtext, messagebox
import random

class ChatBotApp:
    def __init__(self, master):
        self.master = master
        master.title("ChatBot")

        self.responses = {
            "hello": ["Hey!", "Hello!", "Hi there!"],
            "how are you": ["I am fine, what about you?", "I am just a programmer, but I am fine. How about you?", "I don't have feelings!"],
            "goodbye": ["Goodbye!", "See you later, take care", "Take care"],
            "default": ["Sorry, I am not sure", "Can you please provide more information", "Sorry, I don't understand that"],
        }

        self.create_widgets()

    def get_response(self, user_input):
        user_input = user_input.lower()
        for key in self.responses:
            if key in user_input:
                return random.choice(self.responses[key])
        return random.choice(self.responses["default"])

    def send_message(self):
        user_input = self.user_input.get("1.0", "end").strip()
        if user_input:
            response = self.get_response(user_input)
            self.conversation.config(state=tk.NORMAL)
            self.conversation.insert(tk.END, "You: " + user_input + "\n", "user")
            self.conversation.insert(tk.END, "Chatbot: " + response + "\n", "chatbot")
            self.conversation.see(tk.END)
            self.conversation.config(state=tk.DISABLED)
            self.user_input.delete("1.0", "end")

    def create_widgets(self):
        self.conversation = scrolledtext.ScrolledText(self.master, wrap=tk.WORD, state=tk.DISABLED)
        self.conversation.grid(row=0, column=0, columnspan=2, padx=10, pady=10)

        self.user_input = tk.Text(self.master, height=3)
        self.user_input.grid(row=1, column=0, padx=10, pady=(0, 10))

        self.send_button = tk.Button(self.master, text="Send", command=self.send_message)
        self.send_button.grid(row=1, column=1, padx=10, pady=(0, 10))

        self.conversation.tag_config("user", foreground="blue")
        self.conversation.tag_config("chatbot", foreground="green")

        self.user_input.focus_set()


root = tk.Tk()
app = ChatBotApp(root)
root.mainloop()
