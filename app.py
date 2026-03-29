import tkinter as tk
import pickle
import json
import random

# Load model
model = pickle.load(open("model.pkl", "rb"))
vectorizer = pickle.load(open("vectorizer.pkl", "rb"))

# Load intents
with open("intents.json") as file:
    data = json.load(file)

def get_response(tag):
    for intent in data["intents"]:
        if intent["tag"] == tag:
            return random.choice(intent["responses"])

def send():
    user_input = entry.get()
    chat.insert(tk.END, "You: " + user_input + "\n")

    text_vec = vectorizer.transform([user_input])
    tag = model.predict(text_vec)[0]

    response = get_response(tag)
    chat.insert(tk.END, "Bot: " + response + "\n\n")

    entry.delete(0, tk.END)

# GUI
root = tk.Tk()
root.title("AI Student Chatbot")

chat = tk.Text(root, height=20, width=50)
chat.pack()

entry = tk.Entry(root, width=40)
entry.pack()

button = tk.Button(root, text="Send", command=send)
button.pack()

root.mainloop()
