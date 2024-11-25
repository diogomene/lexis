import json
import os

# Função para salvar conteúdo em um arquivo JSON.
def save_json_file(content, filePath):

    # Garante que o caminho tenha a extensão ".json".
    try:
        if not filePath.endswith(".json"):
            filePath += ".json"
        os.makedirs(os.path.dirname(filePath), exist_ok=True)

        # Abre o arquivo no modo de escrita e salva os dados em formato JSON.
        with open(filePath, "w") as f:
            json.dump(content, f, indent=4, ensure_ascii=False)

    # Captura erros de entrada/saída ou problemas de conversão para JSON.
    except (IOError, json.JSONDecodeError) as e:
        print(f"Um erro ocorreu ao salvar arquivo json: {e}")

# Função para salvar conteúdo em um arquivo de texto.
def save_text_file(content, filePath):
    try:
        if not filePath.endswith(".txt"):
            filePath += ".txt"
        os.makedirs(os.path.dirname(filePath), exist_ok=True)
        with open(filePath, "w") as f:
            f.write(content)
    except IOError as e:
        print(f"Um erro ocorreu ao salvar arquivo de texto: {e}")