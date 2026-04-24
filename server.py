from flask import Flask, render_template, request
from emotion_detection import emotion_detector

app = Flask("Emotion Detection")

@app.route("/")
def load_page():
    """Loads initial page where the user can input their text"""
    return render_template("index.html")

@app.route("/emotionDetector")
def pass_input():
    """Processes the user's text and returns the analyzed emotions"""
    text = request.args.get("textToAnalyze")
    emotions = emotion_detector(text)
    if emotions['dominant_emotion'] is None:
        return "Invalid text! Please try again!"
    return_str = (
            "For the given statement, the system response is "
            f"'anger': {emotions['anger']}, "
            f"'disgust': {emotions['disgust']}, "
            f"'fear': {emotions['fear']}, "
            f"'joy': {emotions['joy']}, and "
            f"'sadness': {emotions['sadness']}. "
            f"The dominant emotion is {emotions['dominant_emotion']}."
            )
    return return_str


if __name__=="__main__":
    app.run()
