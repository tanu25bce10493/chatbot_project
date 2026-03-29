from flask import Flask, render_template, request, jsonify
import pickle
import json
import random

app = Flask(__name__)

# Load model and vectorizer
model = pickle.load(open("model.pkl", "rb"))
vectorizer = pickle.load(open("vectorizer.pkl", "rb"))

# Load intents
with open("intents.json") as file:
    data = json.load(file)

# Get response based on tag
def get_response(tag):
    for intent in data["intents"]:
        if intent["tag"] == tag:
            return random.choice(intent["responses"])

# Home route
@app.route("/")
def home():
    return render_template("index.html")

# Chat route
@app.route("/chat", methods=["POST"])
def chat():
    user_input = request.json["message"]

    # Convert text to vector
    text_vec = vectorizer.transform([user_input])

    # Get probabilities
    probs = model.predict_proba(text_vec)[0]
    max_prob = max(probs)

    # Predict intent
    tag = model.predict(text_vec)[0]

    # Fallback if low confidence
    if max_prob < 0.5:
        return jsonify({
            "response": "I’m not sure about that yet 🤔. Try asking about AI, ML, search algorithms, or exam topics."
        })

    # Get response
    response = get_response(tag)

    return jsonify({"response": response})

# Run app
if __name__ == "__main__":
    app.run(debug=True)
