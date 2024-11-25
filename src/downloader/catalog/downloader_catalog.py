from typing import Literal
from .downloader_gutenberg import download_catalog as download_catalog_gutenberg
from .downloader_poetrydb import download_catalog as download_catalog_poetrydb

CATALOG_LITERALS = Literal["gutenberg", "poetrydb", "all"]

# Define uma função para baixar catálogos de livros ou poesias de fontes específicas.
# A função recebe `font` (a fonte do catálogo) e `books_count` (quantidade de livros a baixar).
def download_catalog(font: CATALOG_LITERALS, books_count:int) -> None:
    
    # Verifica qual fonte foi especificada e chama a função apropriada.
    if(font == "gutenberg"):
        download_catalog_gutenberg(books_count)  
    elif (font == "poetrydb"):
        download_catalog_poetrydb(books_count)
    elif (font == "all"):
        download_catalog_poetrydb(books_count)
        download_catalog_gutenberg(books_count)

    # Caso o valor de `font` não esteja entre os esperados, lança uma exceção.
    else:
        raise ValueError("Fonte de catalogo invalida")
