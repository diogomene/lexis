from typing import Literal
from .downloader_gutenberg import download_catalog as download_catalog_gutenberg
from .downloader_poetrydb import download_catalog as download_catalog_poetrydb

CATALOG_LITERALS = Literal["gutenberg", "poetrydb", "all"]

def download_catalog(font: CATALOG_LITERALS) -> None:
    if(font == "gutenberg"):
        download_catalog_gutenberg()  
    elif (font == "poetrydb"):
        download_catalog_poetrydb()
    elif (font == "all"):
        download_catalog_poetrydb()
        download_catalog_gutenberg()
    else:
        raise ValueError("Fonte de catalogo invalida")
