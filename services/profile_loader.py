import json
from pathlib import Path

#Função para receber o caminho do arquivo de perfil e carregar os dados do perfil a partir do arquivo JSON.
def load_profile(file_path: str | Path) -> dict:
    with open(file_path, "r", encoding="utf-8") as file:
        profile = json.load(file) 
        return profile