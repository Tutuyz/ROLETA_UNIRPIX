
import random

from controle_saldo import buscar_usuario, atualizar_saldo


def realizar_aposta():
    nome = input("Digite seu nome: ")

    usuario = buscar_usuario(nome)

    if usuario is None:
        print("Usuário não encontrado!")
        return

    print("\n===== ROLETA UNIRPIX =====")
    print("Escolha um número:")
    print("0")
    print("1")

    try:
        palpite = int(input("Seu palpite: "))

        if palpite not in [0, 1]:
            print("Escolha apenas 0 ou 1!")
            return

        valor = float(input("Valor da aposta: R$ "))

        if valor <= 0:
            print("A aposta precisa ser maior que zero!")
            return

        if valor > usuario["saldo"]:
            print("Saldo insuficiente!")
            return

        resultado = random.randint(0, 1)

        print("\nGirando a roleta...")
        print(f"Resultado: {resultado}")

        if resultado == palpite:
            atualizar_saldo(nome, valor)

            print("Parabéns! Você ganhou!")
            print(f"Prêmio: R$ {valor * 2:.2f}")

        else:
            atualizar_saldo(nome, -valor)

            print("Que pena! Você perdeu!")
            print(f"Valor perdido: R$ {valor:.2f}")

        usuario_atualizado = buscar_usuario(nome)

        print(
            f"Saldo atual: R$ "
            f"{usuario_atualizado['saldo']:.2f}"
        )

    except ValueError:
        print("Digite valores válidos!")
