import requests
import os

from util.http_requester import getFromUrl
from util.file_manager import save_json_file, save_text_file
BASE_URL = "https://poetrydb.org"

# Função para obter o catálogo de poesias.
def get_catalog(count: int):
    url = f"{BASE_URL}/random/{count}"
    catalog = []
    
    # Faz a requisição usando a função utilitária e obtém os dados retornados.
    try:
        res = getFromUrl(url)
        catalog.extend(res)

    # Em caso de erro, exibe uma mensagem e retorna uma lista vazia.
    except (KeyError, requests.HTTPError) as e:
        print(f"Um erro ocorreu ao baixar o catalogo de poesias: {e}")
        return []
    
    return catalog

# Função para salvar os conteúdos das poesias como arquivos de texto.
def get_books(catalog):
    current_dir = os.path.dirname(os.path.abspath(__file__))
    for book in catalog:
        book_file_name = ''.join(e for e in book.get("title").lower() if e.isalnum())[:35]
        output_path = os.path.abspath(os.path.join(current_dir, f"../../../data/books/poetry/{book_file_name}.txt"))
        save_text_file('\n'.join(book.get("lines")), output_path)

# Função principal para baixar o catálogo e salvar os conteúdos das poesias.
def download_catalog(books_count:int):
    catalog = get_catalog(books_count)
    current_dir = os.path.dirname(os.path.abspath(__file__))
    catalog_path = os.path.join(current_dir, "../../../data/catalog/poetrydb_catalog.json")
    catalog_path = os.path.abspath(catalog_path)
    save_json_file(catalog, catalog_path)
    get_books(catalog)
