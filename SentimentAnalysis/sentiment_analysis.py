import requests
import json

def sentiment_analyzer(text_to_analyse):
    url = 'https://sn-watson-sentiment-bert.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/SentimentPredict'
    headers = {"grpc-metadata-mm-model-id": "sentiment_aggregated-bert-workflow_lang_multi_stock"}
    dictObj = { "raw_document": { "text": text_to_analyse } }

    res = requests.post(url, json = dictObj, headers = headers)

    formattedRes = json.loads(res.text)

    if res.status_code == 200:
        label = formattedRes['documentSentiment']['label']
        score = formattedRes['documentSentiment']['score']
    elif res.status_code == 500:
        label = None
        score = None

    return {'label': label, 'score':score}