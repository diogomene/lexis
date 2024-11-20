import requests
import os
import sys

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from util.http_requester import getFromUrl
from util.file_manager import save_json_file
from util.filter_humor_fiction import validate_json_rules

BASE_URL = "https://gutendex.com"

def get_catalog(mime_type="text", languages=["en"], max_requests=1):
    url = f"{BASE_URL}/books?mime_type={mime_type}&languages={','.join(languages)}"
    catalog = []
    request_count = 0
    book_count = 0

    # while url and request_count < max_requests and book_count < 2000:
    while url and book_count < 2000:
        try:
            res = getFromUrl(url)
            validate_json_rules(res)
            url = res["next"]
            # request_count += 1
            book_count += len(res["results"])
        except (KeyError, requests.HTTPError):
            break

    return catalog

def download_catalog():
    catalog = get_catalog()
    current_dir = os.path.dirname(os.path.abspath(__file__))
    catalog_path = os.path.join(current_dir, "../../../data/catalog/gutenberg_catalog.json")
    catalog_path = os.path.abspath(catalog_path)
    save_json_file(catalog, catalog_path)