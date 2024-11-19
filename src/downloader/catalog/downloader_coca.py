import requests
import os
import sys

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from util.http_requester import getFromUrl
from util.file_manager import save_json_file
BASE_URL = "https://gutendex.com"

def get_catalog(mime_type="application/pdf", languages=["en"]):
    return []

def download_catalog():
    catalog = get_catalog()
    current_dir = os.path.dirname(os.path.abspath(__file__))
    catalog_path = os.path.join(current_dir, "../../../data/catalog/coca_catalog.json")
    catalog_path = os.path.abspath(catalog_path)
    save_json_file(catalog, catalog_path)
