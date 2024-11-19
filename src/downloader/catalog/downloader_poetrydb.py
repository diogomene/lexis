import requests
import os
import sys

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from util.http_requester import getFromUrl
from util.file_manager import save_json_file
BASE_URL = "https://poetrydb.org"

def get_catalog(count: int):
    url = f"{BASE_URL}/random/{count}"
    catalog = []
    
    try:
        res = getFromUrl(url)
        catalog.extend(res)
    except (KeyError, requests.HTTPError) as e:
        print(f"Um erro ocorreu ao baixar o catalogo de poesias: {e}")
        return []
    
    return catalog

def download_catalog():
    catalog = get_catalog(100)
    current_dir = os.path.dirname(os.path.abspath(__file__))
    catalog_path = os.path.join(current_dir, "../../../data/catalog/poetrydb_catalog.json")
    catalog_path = os.path.abspath(catalog_path)
    save_json_file(catalog, catalog_path)
