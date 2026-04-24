from flask import Flask
import requests

app = Flask("Emotion Detection")

@app.route("/emotionDetector")
def pass_input():
    text = requests.args.get("textToAnalyze")
    print(text)
    return

if __name__=="__main__":
    app.run()
