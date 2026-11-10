
from controle_saldo import buscar_usuario, atualizar_saldo


def realizar_deposito():
    nome = input("Digite seu nome: ")

    usuario = buscar_usuario(nome)

    if usuario is None:
        print("Usuário não encontrado!")
        return

    try:
        valor = float(input("Digite o valor do depósito: R$ "))

        if valor <= 0:
            print("O valor precisa ser maior que zero!")
            return

        atualizar_saldo(nome, valor)

        print("\nDepósito realizado com sucesso!")
        print(f"Valor depositado: R$ {valor:.2f}")
        print(f"Novo saldo: R$ {usuario['saldo'] + valor:.2f}")

    except ValueError:
        print("Digite um valor numérico válido!")
