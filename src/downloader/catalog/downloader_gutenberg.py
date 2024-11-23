import requests
import os

from util.http_requester import getFromUrl
from util.file_manager import save_json_file, save_text_file
from util.filter_philosophy_fiction import filtrar_livros

BASE_URL = "https://gutendex.com"
BOOKS_MINIMUN = 100

def get_catalog(mime_type="text", languages=["en"]):
    url = f"{BASE_URL}/books?mime_type={mime_type}&languages={','.join(languages)}"
    catalog = []
    book_count = {
        "philosophy": 0,
        "fiction": 0
    }

    while url and (book_count["philosophy"] < BOOKS_MINIMUN or book_count["fiction"] < BOOKS_MINIMUN):
        try:
            res = getFromUrl(url)

            # Filtrando para considerar apenas livros do tipo "Fiction" ou "Philosophy".
            # O terceiro tipo (Poetry) já está sendo incluso pelo "poetrydb_catalog"
            livros_filtrados = filtrar_livros(res.get("results", []), book_count, BOOKS_MINIMUN)
            catalog.extend(livros_filtrados)
            print("===REQUEST===")
            print(book_count)
            print("=============")
            url = res["next"]
        except (KeyError, requests.HTTPError):
            break

    return catalog

def get_books(catalog):

    new_books = []
    next_id = 1

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
            new_books.append(new_book)
            next_id += 1

        except requests.RequestException as e:
            print(f"Erro ao acessar o link {text_plain_link}: {e}")
            continue
    current_dir = os.path.dirname(os.path.abspath(__file__))
    for book in new_books:
        book_file_name = ''.join(e for e in book.get("title").lower() if e.isalnum())[:35]
        output_path = os.path.abspath(os.path.join(current_dir, f"../../../data/books/{book.get('subject')}/{book_file_name}.txt"))
        save_text_file(book.get("content"), output_path)

def download_catalog():
    catalog = get_catalog()
    current_dir = os.path.dirname(os.path.abspath(__file__))
    catalog_path = os.path.join(current_dir, "../../../data/catalog/gutenberg_catalog.json")
    catalog_path = os.path.abspath(catalog_path)
    save_json_file(catalog, catalog_path)
    get_books(catalog)