import os
import time

meu_dicionario = {}


def menu():
    print("================ MENU =================")
    print("                                       ")
    print("| Cadastrar produtos da loja:       [1]")
    print("| Visualizar o estoque de produtos: [2]")
    print("| Entrar como caixa:                [3]")
    print("| TERMINAR SESSÃO:                  [T]")
    print("                                       ")
    print("=======================================")


def cadastro_de_produto():
    os.system('cls' if os.name == 'nt' else 'clear')
    print("======================================")
    print("                                      ")
    print("                                      ")
    print('ACESSANDO À ADMINISTRAÇÃO DO ESTOQUE!!')
    print("                                      ")
    print("                                      ")
    print("======================================")
    time.sleep(2)
    os.system('cls' if os.name == 'nt' else 'clear')

    print("======================================")
    print("                                      ")
    print("                                      ")
    print('   POR FAVOR, CADASTRE OS PRODUTOS!!  ')
    print("                                      ")
    print("                                      ")
    print("======================================")

    if "produtos" not in meu_dicionario:
        # Cria uma nova lista vazia se não existir a chave "produtos"
        meu_dicionario["produtos"] = []

    while True:
        add = input("| Adicionar produto? [S/N]: ").upper()
        if add == "S":
            os.system('cls' if os.name == 'nt' else 'clear')
            produto = {
                "nome": input("Digite o nome do produto: "),
                "codigo": str(input("Digite o código do produto: ")),
                "valor": float(input("Digite o valor do produto: ")),
                "estoque": int(input("Digite a quantidade em estoque do produto: ")),
            }
            # Adiciona o produto à lista existente
            meu_dicionario["produtos"].append(produto)
            os.system('cls' if os.name == 'nt' else 'clear')

            print("======================================")
            print("                                      ")
            print("                                      ")
            print('         PRODUTO CADASTRADO!!         ')
            print("                                      ")
            print("                                      ")
            print("======================================")
            time.sleep(2)
            os.system('cls' if os.name == 'nt' else 'clear')

        elif add == "N":
            break

    os.system('cls' if os.name == 'nt' else 'clear')
    print("======================================")
    print("                                      ")
    print("                                      ")
    print("  .....NOVO ESTOQUE CADASTRADO!!      ")
    print("                                      ")
    print("                                      ")
    print("======================================")
    time.sleep(2)
    os.system('cls' if os.name == 'nt' else 'clear')

    print("======================================")
    print("                                      ")
    print("                                      ")
    print("     VOLTANDO AO MENU PRINCIPAL.....  ")
    print("                                      ")
    print("                                      ")
    print("======================================")
    time.sleep(2)
    os.system('cls' if os.name == 'nt' else 'clear')


def estoque_de_produto():
    os.system('cls' if os.name == 'nt' else 'clear')
    print("======================================")
    print("                                      ")
    print("                                      ")
    print("        ESTOQUE DE PRODUTOS           ")
    print("                                      ")
    print("                                      ")
    print("======================================")

    if len(meu_dicionario.get("produtos", [])) > 0:
        for produto in meu_dicionario.get("produtos", []):
            print("======================================")
            print("                                      ")
            print("Código:", produto["codigo"])
            print("Nome:", produto["nome"])
            print("Valor:", produto["valor"])
            print("Estoque:", produto["estoque"])
            print("                                      ")
            print("======================================")

        while True:
            voltar = input(
                "Pressione [S] para sair: ").upper()
            if voltar == 'S':
                print("======================================")
                print("                                      ")
                print("                                      ")
                print("     VOLTANDO AO MENU PRINCIPAL.....  ")
                print("                                      ")
                print("                                      ")
                print("======================================")
                break
            else:
                print("======================================")
                print("                                      ")
                print("                                      ")
                print("    ALGO DE ERRADO NÃO ESTÁ CERTO!!   ")
                print("                                      ")
                print("                                      ")
                print("======================================")
                time.sleep(2)
                os.system('cls' if os.name == 'nt' else 'clear')

    else:
        print("======================================")
        print("                                      ")
        print("                                      ")
        print("     NÃO HÁ PRODUTOS CADASTRADOS!!    ")
        print("                                      ")
        print("                                      ")
        print("======================================")
        time.sleep(2)
        os.system('cls' if os.name == 'nt' else 'clear')

# essa função recebe um dicionário como argumento, que se chama meu_dicionario.


def saida_de_produtos(meu_dicionario, total=0):
    estoque_atualizado = False

    # Verifica se há produtos cadastrados no dicionário
    if len(meu_dicionario.get("produtos", [])) > 0:
        os.system('cls' if os.name == 'nt' else 'clear')
        print("======================================")
        for produto in meu_dicionario["produtos"]:
            # Exibe informações do produto
            print("======================================")
            print("                                      ")
            print("Código:", produto["codigo"])
            print("Nome:", produto["nome"])
            print("Valor:", produto["valor"])
            print("Estoque:", produto["estoque"])
            print("                                      ")
            print("======================================")

        print("Digite os códigos do que deseja comprar (separados por vírgula): ")
        codigos = input().split(",")  # Recebe os códigos dos produtos como entrada

        quantidade_produtos = {}
        for codigo in codigos:
            quantidade = int(input(
                "Digite a quantidade do produto escolhido (Código do produto-{}): ".format(codigo.strip())))
            quantidade_produtos[codigo.strip()] = quantidade

        for codigo, quantidade in quantidade_produtos.items():
            for produto in meu_dicionario["produtos"]:
                if produto["codigo"] == codigo:
                    if quantidade <= produto["estoque"]:
                        valor_produto = produto["valor"] * quantidade
                        total += valor_produto

                        # Atualiza o estoque do produto
                        produto["estoque"] -= quantidade
                        estoque_atualizado = True
                    else:
                        print(
                            "Estoque insuficiente para o produto referente ao código", codigo)

        if estoque_atualizado:
            print("Total da compra:", total)

            adicionar = True
            while adicionar:
                print("Adicionar mais produtos?")
                adicionar = input("[S] SIM \n[N] NÃO: ").upper()
                if adicionar == "S":
                    saida_de_produtos(meu_dicionario, total)
                    break
                adicionar = False

            print("======================================")
            print("                                      ")
            print("                                      ")
            print("     OBRIGADO POR COMPRAR AQUI!!      ")
            print("                                      ")
            print("                                      ")
            print("======================================")

        print("======================================")
        print("                                      ")
        print("                                      ")
        print("      VOLTANDO AO MENU PRINCIPAL      ")
        print("                                      ")
        print("                                      ")
        print("======================================")
        time.sleep(2)
        os.system('cls' if os.name == 'nt' else 'clear')
        principal()

    else:
        os.system('cls' if os.name == 'nt' else 'clear')
        print("======================================")
        print("                                      ")
        print("                                      ")
        print("     NÃO HÁ PRODUTOS CADASTRADOS      ")
        print("                                      ")
        print("                                      ")
        print("======================================")
        time.sleep(2)
        os.system('cls' if os.name == 'nt' else 'clear')

        print("======================================")


def principal():
    op = True
    while op:
        os.system('cls' if os.name == 'nt' else 'clear')
        menu()
        op = input("Escolha uma opção: ")
        if op == "1":
            cadastro_de_produto()
        elif op == "2":
            estoque_de_produto()
        elif op == "3":
            saida_de_produtos(meu_dicionario)
            op = False
        elif op.upper() == "T":
            print('ENCERRANDO O SISTEMA...')
            break
        else:
            os.system('cls' if os.name == 'nt' else 'clear')
            print("======================================")
            print("                                      ")
            print("                                      ")
            print("   ALGO DE ERRADO NÃO ESTÁ CERTO!!    ")
            print("                                      ")
            print("                                      ")
            print("======================================")
            time.sleep(2)
            os.system('cls' if os.name == 'nt' else 'clear')


principal()
