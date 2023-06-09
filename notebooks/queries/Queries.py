import os
import requests

def __load_token():
    directory = os.path.dirname(__file__)
    access_token = ""
    with open(directory + "/" + "access_token.txt", 'r') as token:
        access_token = token.read()
    return access_token

def run_query(payload={}, model="tiiuae/falcon-7b-instruct"):
    """
    Sample query to HuggingFace API inference, payload may change depending on the model
    """
    API_TOKEN = __load_token()
    assert not "your_HF" in API_TOKEN, "Please remember to provide your HugginFace API token in access_token.txt"
    API_URL = "https://api-inference.huggingface.co/models/" + model
    headers = {"Authorization": f"Bearer {API_TOKEN}"}
    response = requests.post(API_URL, headers=headers, json=payload)
    return response.json()