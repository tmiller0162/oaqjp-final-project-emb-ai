from flask import Flask, render_template, request
import requests

app = Flask("Emotion Detection")

@app.route("/")
def load_page():
    return render_template("index.html")

@app.route("/emotionDetector")
def pass_input():
    text = request.args.get("textToAnalyze")
    print(text)
    return

if __name__=="__main__":
    app.run()
