from typing import Literal
from .downloader_gutenberg import download_catalog as download_catalog_gutenberg
from .downloader_poetrydb import download_catalog as download_catalog_poetrydb

CATALOG_LITERALS = Literal["gutenberg", "poetrydb", "all"]

def download_catalog(font: CATALOG_LITERALS, books_count:int) -> None:
    if(font == "gutenberg"):
        download_catalog_gutenberg(books_count)  
    elif (font == "poetrydb"):
        download_catalog_poetrydb(books_count)
    elif (font == "all"):
        download_catalog_poetrydb(books_count)
        download_catalog_gutenberg(books_count)
    else:
        raise ValueError("Fonte de catalogo invalida")
