"""Module providing functions for emotion detection."""
import requests
import json

def emotion_detector(text_to_analyze):
    # URL of the emotion predictor service
    url = 'https://sn-watson-emotion.labs.skills.network/v1/' \
    'watson.runtime.nlp.v1/NlpService/EmotionPredict'

    # Create a dictionary with the text to be analyzed
    myobj = { "raw_document": { "text": text_to_analyze } }

    # Set the headers required for the API request
    header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}

    # Send a POST request to the API with the text and headers
    response = requests.post(url, json = myobj, headers=header)

    if response.status_code == 200:
        formatted_response = json.loads(response.text)
        emotion_scores_json = formatted_response['emotionPredictions'][0]['emotion']

        dominant_emotion = "anger"

        for emotion in emotion_scores_json:
            if emotion_scores_json[emotion] > emotion_scores_json[dominant_emotion]:
                dominant_emotion = emotion

        emotion_scores_json['dominant_emotion'] = dominant_emotion

        # return json.dumps(emotion_scores_json, indent=4)
        return emotion_scores_json
    elif response.status_code == 400:
        error_scores = {'anger':None,
                        'disgust':None,
                        'fear':None,
                        'joy':None,
                        'sadness':None,
                        'dominant_emotion':None
                        }
        return error_scores
    else:
        error_scores = {'anger':None,
                        'disgust':None,
                        'fear':None,
                        'joy':None,
                        'sadness':None,
                        'dominant_emotion':None
                        }
        return error_scores
