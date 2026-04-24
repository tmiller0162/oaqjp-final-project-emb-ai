from emotion_detection import emotion_detector
from flask import Flask, render_template, request

app = Flask("Emotion Detection")

@app.route("/")
def load_page():
    return render_template("index.html")

@app.route("/emotionDetector")
def pass_input():
    text = request.args.get("textToAnalyze")
    return emotion_detector(text)

if __name__=="__main__":
    app.run()
