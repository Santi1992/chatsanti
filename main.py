

import json 

# me devuelve la mas cercana a mi lista de cosas.
from difflib import get_close_matches


def load_knowledge_base(file_path: str):
    with open(file_path, 'r') as file:
        data: dict = json.load(file)

def save_load_knowledge_base(file_path: str, data:dict):
    with open(file_path, 'w') as file :
        json.dump(data, file, indent=2)


def func_best_match(user_question:str, questions: list[str]):
    pass