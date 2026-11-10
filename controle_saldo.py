

from cadastro import carregar_usuarios, salvar_usuarios


def buscar_usuario(nome):

    usuarios = carregar_usuarios()

    for usuario in usuarios:
        if usuario["nome"].lower() == nome.strip().lower():
            return usuario

    return None


def consultar_saldo():

    nome = input("Digite seu nome: ")

    usuario = buscar_usuario(nome)

    if usuario is None:
        print("Usuário não encontrado!")
        return

    print("\n===== CONSULTA DE SALDO =====")
    print(f"Usuário: {usuario['nome']}")
    print(f"Saldo disponível: R$ {usuario['saldo']:.2f}")


def atualizar_saldo(nome, valor):

    usuarios = carregar_usuarios()

    for usuario in usuarios:

        if usuario["nome"].lower() == nome.strip().lower():

            novo_saldo = usuario["saldo"] + valor

            if novo_saldo < 0:
                return False

            usuario["saldo"] = round(novo_saldo, 2)

            salvar_usuarios(usuarios)

            return True

    return False
