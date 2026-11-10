
from cadastro import cadastrar_usuario
from controle_saldo import consultar_saldo
from deposito import realizar_deposito
from resgate import realizar_resgate
from aposta import realizar_aposta


def menu():

    print("\n================================")
    print("         ROLETA UNIRPIX")
    print("================================")

    while True:

        print("\n1 - Cadastrar usuário")
        print("2 - Consultar saldo")
        print("3 - Depositar dinheiro")
        print("4 - Realizar aposta")
        print("5 - Resgatar dinheiro")
        print("0 - Sair")

        opcao = input("\nEscolha uma opção: ")

        if opcao == "1":
            cadastrar_usuario()

        elif opcao == "2":
            consultar_saldo()

        elif opcao == "3":
            realizar_deposito()

        elif opcao == "4":
            realizar_aposta()

        elif opcao == "5":
            realizar_resgate()

        elif opcao == "0":
            print("\nObrigado por utilizar o UNIRPIX!")
            break

        else:
            print("\nOpção inválida!")


menu()
