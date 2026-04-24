from emotion_detection import emotion_detector
from flask import Flask, render_template, request

app = Flask("Emotion Detection")

@app.route("/")
def load_page():
    return render_template("index.html")

@app.route("/emotionDetector")
def pass_input():
    text = request.args.get("textToAnalyze")
    emotions = emotion_detector(text)
    if emotions['dominant_emotion'] == None:
        return "Invalid text! Please try again!", 400
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
