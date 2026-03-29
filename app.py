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

def send_message(event=None):
    user_input = entry.get()
    if user_input.strip() == "":
        return

    chat_box.config(state=tk.NORMAL)

    chat_box.insert(tk.END, "You: " + user_input + "\n", "user")
    
    text_vec = vectorizer.transform([user_input])
    tag = model.predict(text_vec)[0]
    response = get_response(tag)

    chat_box.insert(tk.END, "Bot: " + response + "\n\n", "bot")

    chat_box.config(state=tk.DISABLED)
    chat_box.yview(tk.END)

    entry.delete(0, tk.END)

def insert_suggestion(text):
    entry.delete(0, tk.END)
    entry.insert(0, text)

# GUI setup
root = tk.Tk()
root.title("AI Student Assistant")
root.geometry("500x600")
root.configure(bg="#1e1e2f")

# Title
title = tk.Label(root, text="🤖 AI Student Chatbot", font=("Arial", 16, "bold"), bg="#1e1e2f", fg="white")
title.pack(pady=10)

# Chat box
chat_box = tk.Text(root, bg="#2c2c3e", fg="white", font=("Arial", 12), wrap=tk.WORD)
chat_box.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)
chat_box.config(state=tk.DISABLED)

# Tag styles
chat_box.tag_config("user", foreground="#00ffcc")
chat_box.tag_config("bot", foreground="#ffcc00")

# Entry field
entry = tk.Entry(root, font=("Arial", 12))
entry.pack(padx=10, pady=5, fill=tk.X)
entry.bind("<Return>", send_message)

# Send button
send_btn = tk.Button(root, text="Send", command=send_message, bg="#4CAF50", fg="white")
send_btn.pack(pady=5)

# Suggestions
suggestion_frame = tk.Frame(root, bg="#1e1e2f")
suggestion_frame.pack(pady=10)

tk.Label(suggestion_frame, text="Try asking:", bg="#1e1e2f", fg="white").pack()

suggestions = [
    "What is AI?",
    "Explain machine learning",
    "What subjects do I have?",
    "How to prepare for exam?",
    "Hello"
]

for s in suggestions:
    tk.Button(
        suggestion_frame,
        text=s,
        command=lambda x=s: insert_suggestion(x),
        bg="#3a3a5c",
        fg="white",
        relief="flat"
    ).pack(pady=2, fill=tk.X)

root.mainloop()
