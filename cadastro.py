
import json
from pathlib import Path

ARQUIVO = Path(__file__).with_name("usuarios.json")


def carregar_usuarios():
    try:
        with open(ARQUIVO, "r", encoding="utf-8") as arquivo:
            return json.load(arquivo)

    except (FileNotFoundError, json.JSONDecodeError):
        return []


def salvar_usuarios(usuarios):
    with open(ARQUIVO, "w", encoding="utf-8") as arquivo:
        json.dump(usuarios, arquivo, indent=4, ensure_ascii=False)


def cadastrar_usuario():
    usuarios = carregar_usuarios()

    nome = input("Digite seu nome: ").strip()

    if not nome:
        print("O nome não pode ficar vazio!")
        return

    for usuario in usuarios:
        if usuario["nome"].lower() == nome.lower():
            print("Este usuário já está cadastrado!")
            return

    novo_usuario = {
        "nome": nome,
        "saldo": 0.0
    }

    usuarios.append(novo_usuario)

    salvar_usuarios(usuarios)

    print("\nCadastro realizado com sucesso!")
    print(f"Bem-vindo, {nome}!")
