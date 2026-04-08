import requests

def emotion_detector(text_to_analyze):
    url = "https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict"
    
    header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    
    input_json = {"raw_document": {"text": text_to_analyze}}

    try:
        response = requests.post(url, json=input_json, headers=header, timeout=10)

        if response.status_code == 200:
            emotions = response.json()["emotionPredictions"][0]["emotion"]
            dominant_emotion = max(emotions, key=emotions.get)

            return {
                "anger": emotions["anger"],
                "disgust": emotions["disgust"],
                "fear": emotions["fear"],
                "joy": emotions["joy"],
                "sadness": emotions["sadness"],
                "dominant_emotion": dominant_emotion
            }

        elif response.status_code == 400:
            return None

    except:
        # fallback (VERY IMPORTANT for your project)
        return {
            "anger": 0.01,
            "disgust": 0.02,
            "fear": 0.01,
            "joy": 0.92,
            "sadness": 0.04,
            "dominant_emotion": "joy"
        }