
from controle_saldo import buscar_usuario, atualizar_saldo


def realizar_resgate():
    nome = input("Digite seu nome: ")

    usuario = buscar_usuario(nome)

    if usuario is None:
        print("Usuário não encontrado!")
        return

    try:
        valor = float(input("Digite o valor do resgate: R$ "))

        if valor <= 0:
            print("O valor precisa ser maior que zero!")
            return

        if valor > usuario["saldo"]:
            print("Saldo insuficiente!")
            return

        atualizar_saldo(nome, -valor)

        print("\nResgate realizado com sucesso!")
        print(f"Valor resgatado: R$ {valor:.2f}")
        print(f"Saldo restante: R$ {usuario['saldo'] - valor:.2f}")

    except ValueError:
        print("Digite um valor numérico válido!")
