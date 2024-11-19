import requests

def getFromUrl(url: str) -> any:
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        response.raise_for_status()