import requests
import os
import sys
import json

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from util.http_requester import getFromUrl
from util.file_manager import save_json_file
from util.filter_humor_fiction import filtrar_livros

BASE_URL = "https://gutendex.com"

def get_catalog(mime_type="text", languages=["en"]):
    url = f"{BASE_URL}/books?mime_type={mime_type}&languages={','.join(languages)}"
    catalog = []
    book_count = 0

    while url and book_count < 20:
        try:
            res = getFromUrl(url)

            # Filtrando para considerar apenas livros do tipo "Fiction" ou "Philosophy".
            # O terceiro tipo (Poetry) já está sendo incluso pelo "poetrydb_catalog"
            livros_filtrados = filtrar_livros(res.get("results", []))
            catalog.extend(livros_filtrados)

            url = res["next"]
            book_count += len(res["results"])
        except (KeyError, requests.HTTPError):
            break

    return catalog

def get_books(catalog):
    current_dir = os.path.dirname(os.path.abspath(__file__))
    output_path = os.path.abspath(os.path.join(current_dir, "../../../data/catalog/books_gutenberg.json"))

    new_books = []
    next_id = 1

    for book in catalog:
        formats = book.get("formats", {})
        text_plain_link = formats.get("text/plain; charset=us-ascii")

        if not text_plain_link:
            continue

        try:
            response = requests.get(text_plain_link)
            response.raise_for_status()
            content = response.text

            new_book = {
                "id": next_id,
                "content": content
            }
            new_books.append(new_book)
            next_id += 1

        except requests.RequestException as e:
            print(f"Erro ao acessar o link {text_plain_link}: {e}")
            continue

    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    with open(output_path, "w", encoding="utf-8") as file:
        json.dump(new_books, file, indent=4, ensure_ascii=False)

def download_catalog():
    catalog = get_catalog()
    current_dir = os.path.dirname(os.path.abspath(__file__))
    catalog_path = os.path.join(current_dir, "../../../data/catalog/gutenberg_catalog.json")
    catalog_path = os.path.abspath(catalog_path)
    save_json_file(catalog, catalog_path)
    get_books(catalog)