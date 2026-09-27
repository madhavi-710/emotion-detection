from flask import Flask, render_template, request, jsonify
from transformers import pipeline

app = Flask(__name__)

# Load trained emotion detection model
MODEL_PATH = "./models/emotion_model"

print("Loading emotion detection model...")

emotion_classifier = pipeline(
    "text-classification",
    model=MODEL_PATH,
    tokenizer=MODEL_PATH
)

# Convert model labels to actual emotion names
emotion_labels = {
    "LABEL_0": "sadness",
    "LABEL_1": "joy",
    "LABEL_2": "love",
    "LABEL_3": "anger",
    "LABEL_4": "fear",
    "LABEL_5": "surprise"
}


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/predict/text", methods=["POST"])
def predict_text():

    data = request.get_json()

    text = data.get("text", "").strip()

    if not text:
        return jsonify({
            "error": "Please enter some text."
        }), 400

    # Predict emotion
    result = emotion_classifier(text)[0]

    model_label = result["label"]
    confidence = result["score"]

    emotion = emotion_labels.get(model_label, model_label)

    return jsonify({
        "text": text,
        "emotion": emotion,
        "confidence": round(confidence, 4)
    })


if __name__ == "__main__":
    app.run(debug=True)