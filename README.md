# emotion-detection
AI-powered emotion detection from text or speech using NLP and speech processing.
# 🎭 Emotion Detection from Text or Speech

An AI-powered **Emotion Detection System** that analyzes human input and identifies the underlying emotion. The system is designed to accept **text input** and can also support **speech input**, making emotion analysis more interactive and accessible.

The project combines **Natural Language Processing (NLP)**, **Machine Learning**, and **Speech Processing** to recognize emotions from user input.

---

## 🚀 Features

* 📝 **Text Emotion Detection** – Enter a sentence or message and detect its emotion.
* 🎙️ **Speech Input** – Record speech and use the recognized text for emotion detection.
* 🤖 **AI-Powered Prediction** – Uses a trained NLP emotion classification model.
* 📊 **Confidence Score** – Displays the model's confidence for the predicted emotion.
* ⚡ **Real-Time Prediction** – Get emotion predictions directly from the application.
* 🌐 **Web-Based Interface** – Simple interface for interacting with the emotion detection system.
* 🔄 **Start/Stop Recording** – Speech recording can be controlled directly from the interface.

---

## 🧠 Emotions Detected

The model currently identifies the following six emotions:

| Emotion     | Description                                  |
| ----------- | -------------------------------------------- |
| 😊 Joy      | Happiness, excitement, or positive feelings  |
| 😢 Sadness  | Sorrow, disappointment, or negative feelings |
| ❤️ Love     | Affection, care, or emotional attachment     |
| 😠 Anger    | Frustration, irritation, or hostility        |
| 😨 Fear     | Anxiety, worry, or feeling threatened        |
| 😲 Surprise | Unexpected or sudden reactions               |

---

## 🛠️ Technologies Used

* **Python**
* **Flask**
* **Hugging Face Transformers**
* **Natural Language Processing (NLP)**
* **Machine Learning**
* **Speech Recognition**
* **HTML**
* **CSS**
* **JavaScript**

---

## 🏗️ Project Architecture

The system follows this general workflow:

```text
                User Input
                    │
          ┌─────────┴─────────┐
          │                   │
      Text Input         Speech Input
          │                   │
          │            Speech Recognition
          │                   │
          └─────────┬─────────┘
                    │
                    ▼
              Text Processing
                    │
                    ▼
          NLP Emotion Classifier
                    │
                    ▼
           Emotion Prediction
                    │
          ┌─────────┴─────────┐
          │                   │
       Emotion           Confidence
          │                   │
          └─────────┬─────────┘
                    ▼
              Display Result
```

---

## 📂 Project Structure

```text
emotion-detection/
│
├── app.py
├── README.md
├── Emotion_Detection_Project_Formal_Documentation.docx
│
├── models/
│   └── emotion_model/
│       ├── model files
│       └── tokenizer files
│
├── templates/
│   └── index.html
│
└── static/
    ├── css/
    ├── js/
    └── other frontend assets
```

> The exact contents of the `models`, `templates`, and `static` folders may vary depending on the current project version.

---

## ⚙️ How It Works

### 1. Text Input

The user enters a sentence or message into the application.

Example:

```text
I am very happy today!
```

The text is sent to the Flask backend for processing.

### 2. Speech Input

The user can record their voice using the application's recording controls.

The recorded speech is converted into text using speech recognition.

### 3. Emotion Classification

The processed text is passed to the trained emotion classification model.

The model predicts the most likely emotion.

### 4. Result

The application returns:

* Input text
* Detected emotion
* Confidence score

Example:

```text
Input: I am very happy today!

Emotion: Joy

Confidence: 0.98
```

---

## 🔌 API Endpoint

The Flask backend provides an endpoint for text emotion prediction:

```http
POST /predict/text
```

### Request

```json
{
  "text": "I am feeling very happy today"
}
```

### Response

```json
{
  "text": "I am feeling very happy today",
  "emotion": "joy",
  "confidence": 0.98
}
```

If no text is provided, the API returns an appropriate error response.

---

## 💻 Installation

### 1. Clone the Repository

```bash
git clone https://github.com/madhavi-710/emotion-detection.git
```

### 2. Navigate to the Project

```bash
cd emotion-detection
```

### 3. Create a Virtual Environment

```bash
python -m venv venv
```

### 4. Activate the Virtual Environment

**Windows:**

```bash
venv\Scripts\activate
```

**Linux / macOS:**

```bash
source venv/bin/activate
```

### 5. Install Dependencies

If a `requirements.txt` file is available:

```bash
pip install -r requirements.txt
```

Otherwise, install the required packages according to the project's Python dependencies.

---

## ▶️ Running the Application

Start the Flask application:

```bash
python app.py
```

The application will start on the local Flask development server.

Open the displayed local URL in your browser.

For example:

```text
http://127.0.0.1:5000
```

---

## 🧪 Example

### Input

```text
I am so excited about my new project!
```

### Output

```text
Emotion: Joy
Confidence: 0.XX
```

The exact confidence value depends on the model prediction.

---

## 🎯 Project Objectives

The main objectives of this project are:

* To build an AI-based emotion detection system.
* To analyze emotions expressed through natural language.
* To provide both text and speech-based interaction.
* To demonstrate practical applications of NLP and machine learning.
* To create an accessible web interface for emotion analysis.
* To understand the complete workflow from user input to machine-learning prediction.

---

## 🔮 Future Enhancements

Possible improvements include:

* 📱 Responsive mobile-friendly interface
* 🌍 Support for multiple languages
* 🎤 Improved speech recognition
* 📈 Emotion history and analytics
* 📊 Visualization of emotion probabilities
* 🧠 Improved model accuracy through larger datasets
* 💬 Conversation-level emotion analysis
* ☁️ Cloud deployment
* 🔐 User authentication and personalized emotion history

---

## ⚠️ Limitations

Emotion detection is an AI-based prediction task and should not be treated as a definitive measurement of a person's actual emotional state.

Predictions can vary depending on:

* Input wording
* Context
* Speech recognition accuracy
* Model training data
* Ambiguous or mixed emotions

---

## 👩‍💻 Author

**Madhavi**

Computer Science and Engineering Student
Interested in **Artificial Intelligence, Machine Learning, Software Development, and NLP**.

---

## 📌 Project Status

🚧 **Currently under development**

The project is being continuously improved with additional functionality, UI enhancements, and model-related improvements.

---

## ⭐ Acknowledgements

This project uses open-source technologies and libraries from the Python and machine-learning ecosystem, including Flask and Hugging Face Transformers.

---

## 📜 License

This project is intended for educational and development purposes.
