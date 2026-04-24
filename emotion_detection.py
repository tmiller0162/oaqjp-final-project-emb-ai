import requests
import json

def emotion_detector(text_to_analyze):
    url = (
            'https://sn-watson-emotion.labs.skills.network/'
            'v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
            )
    header = {"grpc-metadata-mm-model-id":
              "emotion_aggregated-workflow_lang_en_stock"}
    input_json = { "raw_document": { "text": text_to_analyze } }
    api_get = requests.post(url=url, headers=header, json=input_json)
    raw_output = api_get.text
    emotions = json.loads(raw_output) #['emotionPredictions']['emotion']
    #print(max(emotions, key=emotions.get))
    print(emotions)
    dict_return = {
            'anger': anger_s,
            'disgust': disgust_s,
            'fear' : fear_s,
            'joy': joy_s,
            'sadness': sadness_s,
            'dominant_emotion': 'thing'
            }

print(emotion_detector("I am very happy about this"))
