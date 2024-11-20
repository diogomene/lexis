import requests
import os
import sys

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from util.http_requester import getFromUrl
from util.file_manager import save_json_file

BASE_URL = "https://gutendex.com"

def get_catalog(mime_type="text", languages=["en"]):
    url = f"{BASE_URL}/books?mime_type={mime_type}&languages={','.join(languages)}"
    catalog = []
    while True:
        try:
            res = getFromUrl(url)
            catalog.extend(res["results"])
            url = res["next"]
        except (KeyError, requests.HTTPError):
            break
        if not url:
            break
    return catalog

def download_catalog():
    catalog = get_catalog()
    current_dir = os.path.dirname(os.path.abspath(__file__))
    catalog_path = os.path.join(current_dir, "../../../data/catalog/gutenberg_catalog.json")
    catalog_path = os.path.abspath(catalog_path)
    save_json_file(catalog, catalog_path)
