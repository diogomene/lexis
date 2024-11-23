import json
import os
def save_json_file(content, filePath):
    try:
        if not filePath.endswith(".json"):
            filePath += ".json"
        os.makedirs(os.path.dirname(filePath), exist_ok=True)
        with open(filePath, "w") as f:
            json.dump(content, f, indent=4, ensure_ascii=False)
    except (IOError, json.JSONDecodeError) as e:
        print(f"Um erro ocorreu ao salvar arquivo json: {e}")

def save_text_file(content, filePath):
    try:
        if not filePath.endswith(".txt"):
            filePath += ".txt"
        os.makedirs(os.path.dirname(filePath), exist_ok=True)
        with open(filePath, "w") as f:
            f.write(content)
    except IOError as e:
        print(f"Um erro ocorreu ao salvar arquivo de texto: {e}")