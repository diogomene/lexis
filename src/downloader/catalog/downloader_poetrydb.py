import requests
import os

from util.http_requester import getFromUrl
from util.file_manager import save_json_file, save_text_file
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
def get_books(catalog):
    current_dir = os.path.dirname(os.path.abspath(__file__))
    for book in catalog:
        book_file_name = ''.join(e for e in book.get("title").lower() if e.isalnum())[:35]
        output_path = os.path.abspath(os.path.join(current_dir, f"../../../data/books/poetry/{book_file_name}.txt"))
        save_text_file('\n'.join(book.get("lines")), output_path)
def download_catalog():
    catalog = get_catalog(100)
    current_dir = os.path.dirname(os.path.abspath(__file__))
    catalog_path = os.path.join(current_dir, "../../../data/catalog/poetrydb_catalog.json")
    catalog_path = os.path.abspath(catalog_path)
    save_json_file(catalog, catalog_path)
    get_books(catalog)
