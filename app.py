from flask import Flask, render_template, request, jsonify
import pickle
import json
import random

app = Flask(__name__)

model = pickle.load(open("model.pkl", "rb"))
vectorizer = pickle.load(open("vectorizer.pkl", "rb"))

with open("intents.json") as file:
    data = json.load(file)

def get_response(tag):
    for intent in data["intents"]:
        if intent["tag"] == tag:
            return random.choice(intent["responses"])

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/chat", methods=["POST"])
def chat():
    user_input = request.json["message"]

    text_vec = vectorizer.transform([user_input])
    tag = model.predict(text_vec)[0]

    response = get_response(tag)

    return jsonify({"response": response})

if __name__ == "__main__":
    app.run(debug=True)
