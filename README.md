# Lexis (λέξις)
Lexis (λέξις): estilo ou escolha de palavras em uma comunicação; estilo de discurso.

## Sobre o projeto
Este projeto tem como objetivo testar diferentes métodos de aplicação de IA, a fim
de desenvolver um preditor capaz de distinguir entre os generos de livro:
- Filosofia
- Ficção
- Poesia

Esse projeto foi desenvolvido com textos contidos nos repositórios de:
- PoetryDB
- Gutenberg Project

Devido a grande quantidade de livros em inglês nesses repositórios, os treinamentos
realizados utilizaram como base textos de língua inglesa.

## Como rodar?
Primeiro instale as dependências do projeto
```
pip install -r requirements.txt
```
Posteriormente basta executar o arquivo `src/main.py`
```
python src/main.py
```

## Como baixar novos livros
Basta executar o arquivo `src/downloader/downloadCatalogs.py`
(No mesmo arquivo é possível alterar o número de livros que deverão ser obtidos
de cada categoria)
```
python src/downloader/downloadCatalogs.py
```