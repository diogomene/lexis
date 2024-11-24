import requests
import os

from util.http_requester import getFromUrl
from util.file_manager import save_json_file, save_text_file
from util.filter_philosophy_fiction import filtrar_livros

BASE_URL = "https://gutendex.com"

def get_catalog(books_count, mime_type="text", languages=["en"]):
    url = f"{BASE_URL}/books?mime_type={mime_type}&languages={','.join(languages)}"
    catalog = []
    book_count = {
        "philosophy": 0,
        "fiction": 0
    }

    while url and (book_count["philosophy"] < books_count or book_count["fiction"] < books_count):
        try:
            res = getFromUrl(url)

            # Filtrando para considerar apenas livros do tipo "Fiction" ou "Philosophy".
            # O terceiro tipo (Poetry) já está sendo incluso pelo "poetrydb_catalog"
            livros_filtrados = filtrar_livros(res.get("results", []), book_count, books_count)
            catalog.extend(livros_filtrados)
            print("===REQUEST===")
            print(book_count)
            print("=============")
            url = res["next"]
        except (KeyError, requests.HTTPError):
            break

    return catalog

def get_books(catalog):
    current_dir = os.path.dirname(os.path.abspath(__file__))
    for book in catalog:
        print(book.get("validated_subject"))
        formats = book.get("formats", {})
        text_plain_link = formats.get("text/plain; charset=us-ascii")

        if not text_plain_link:
            continue

        try:
            response = requests.get(text_plain_link)
            response.raise_for_status()
            content = response.text

            new_book = {
                "title": book.get("title"),
                "subject": book.get("validated_subject"),
                "content": content
            }
            book_file_name = ''.join(e for e in new_book.get("title").lower() if e.isalnum())[:35]
            output_path = os.path.abspath(os.path.join(current_dir, f"../../../data/books/{new_book.get('subject')}/{book_file_name}.txt"))
            save_text_file(new_book.get("content"), output_path)
        except requests.RequestException as e:
            print(f"Erro ao acessar o link {text_plain_link}: {e}")
            continue

def download_catalog(books_count):
    catalog = get_catalog(books_count)
    current_dir = os.path.dirname(os.path.abspath(__file__))
    catalog_path = os.path.join(current_dir, "../../../data/catalog/gutenberg_catalog.json")
    catalog_path = os.path.abspath(catalog_path)
    save_json_file(catalog, catalog_path)
    get_books(catalog)