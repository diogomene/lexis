import requests
import os

from util.http_requester import getFromUrl
from util.file_manager import save_json_file, save_text_file
from util.filter_philosophy_fiction import filtrar_livros

# URL base da API do Projeto Gutenberg.
BASE_URL = "https://gutendex.com"

# Função para obter o catálogo de livros, com filtros por tipo de arquivo e idioma.
def get_catalog(books_count, mime_type="text", languages=["en"]):
    # Constrói a URL inicial para consulta de livros com os filtros especificados.
    url = f"{BASE_URL}/books?mime_type={mime_type}&languages={','.join(languages)}"
    catalog = []
    book_count = {
        "philosophy": 0,
        "fiction": 0
    }

    # Faz requisições paginadas até atingir o limite de livros requisitados para cada gênero.
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

            # Atualiza a URL para a próxima página (paginação).
            url = res["next"]
        except (KeyError, requests.HTTPError):
            break

    return catalog

# Função para baixar o conteúdo dos livros listados no catálogo.
def get_books(catalog):
    # Obtém o diretório atual do arquivo em execução.
    current_dir = os.path.dirname(os.path.abspath(__file__))
    for book in catalog:
        print(book.get("validated_subject"))
        formats = book.get("formats", {})
        text_plain_link = formats.get("text/plain; charset=us-ascii")

        # Se o link não existir, pula para o próximo livro.
        if not text_plain_link:
            continue

        # Faz a requisição para obter o conteúdo do livro.
        try:
            response = requests.get(text_plain_link)
            response.raise_for_status()
            content = response.text

            # Cria um dicionário representando o livro com título, gênero e conteúdo.
            new_book = {
                "title": book.get("title"),
                "subject": book.get("validated_subject"),
                "content": content
            }
            book_file_name = ''.join(e for e in new_book.get("title").lower() if e.isalnum())[:35]

            # Define o caminho de saída do arquivo, com base no gênero.
            output_path = os.path.abspath(os.path.join(current_dir, f"../../../data/books/{new_book.get('subject')}/{book_file_name}.txt"))
            save_text_file(new_book.get("content"), output_path)

        # Em caso de erro na requisição, exibe uma mensagem de erro e continua.
        except requests.RequestException as e:
            print(f"Erro ao acessar o link {text_plain_link}: {e}")
            continue

# Função principal para baixar o catálogo e os livros correspondentes.
def download_catalog(books_count):
    catalog = get_catalog(books_count)
    current_dir = os.path.dirname(os.path.abspath(__file__))
    catalog_path = os.path.join(current_dir, "../../../data/catalog/gutenberg_catalog.json")
    catalog_path = os.path.abspath(catalog_path)
    save_json_file(catalog, catalog_path)
    get_books(catalog)