
from Login.Funções_Login import *
from Core.Funções_Estoque import *
from Core.Codigo_Estoque import Estoque
from datetime import datetime
import Login.Codigo_Login as Codigo_Login


def main1():
    while True:
        print('\nCadastre dentro do nosso sistema de estoque !!')
        try:
            opcao = int(input(
                "\n[=== MENU DE OPÇÕES ===]\n [1]-> Cadastrar cliente\n [2]-> Cadastrar Colaborador\n [3]-> Cadastrar Cargo\n [4]-> Login \n [5]-> Sair\n -> "))
        except ValueError:
            print("\nEntrada inválida. Por favor, digite um número.")
            registrar_logs(
                f"erro", "Entrada inválida. Por favor, digite um número.")
            continue

        registrar_logs(f'info', f"Opção escolhida com sucesso: [{opcao}]")

        match opcao:
            case 1:
                print("\n--- Preencha os dados cadastrais ---")
                nome_cli = nome()
                doc = input("Digite o CPF ou CNPJ: ")
                uf = input("Digite a UF (ex: SP, MG): ")
                rua = input("Digite a Rua: ")
                cidade = input("Digite a Cidade: ")
                bairro = input("Digite o Bairro: ")
                while True:
                    try:
                        num = int(input("Digite o Número: "))
                        break
                    except ValueError:
                        registrar_logs("erro", 'Digite apenas numeros.')

                email_cliente = verificar_email()
                senha_cliente = verificar_senha()

                cadastro = Codigo_Login.Cadastro(
                    nome_cli, doc, uf, rua, cidade, bairro, num, email_cliente, senha_cliente)
                cadastro.salvar_dados()

            case 2:
                print("CADASTRAR FUNCIONARIO \n")

                nome_colaborador = input(
                    'Nome do colaborador: ').strip().capitalize()
                documento = input('Digite o seu cpf: ').strip()
                email_colaborador = verificar_email()
                senha_colaborador = verificar_senha()
                data_admissao = datetime.now().strftime("%d/%m/%Y")
                try:
                    buscar_cargos()
                    cargo_do_funcionario = int(
                        input("Digite o numero do cargo: "))
                except ValueError:
                    registrar_logs("erro", "Digite apenas numeros!")

                funcionario_criado = Codigo_Login.Colaborador(
                    nome_colaborador, documento, data_admissao, cargo_do_funcionario, email_colaborador, senha_colaborador)
                funcionario_criado.adicionar_colaborador()

            case 3:
                print('\n Cadastre um cargo\n')

                cargo_nome = input(
                    'Digite o nome do cargo: ').strip().capitalize()
                cargo_criado = Codigo_Login.Cargo(cargo_nome)
                cargo_criado.criar_cargo()

            case 4:

                email_input = input("Digite seu email: ")
                senha_input = input("Digite sua senha: ")

                cargo_retornado = verificar_login(email_input, senha_input)

                if cargo_retornado == "Administrador":
                    main2()
                elif cargo_retornado == "Estoquista":
                    main2()
                elif cargo_retornado == "Caixa":
                    main3()
                else:
                    registrar_logs("erro", "Perfil não encontrado.")

            case 5:
                print("\nSaindo do sistema. Até logo!")
                registrar_logs("info", "Saindo do sistema.")
                break


def main2():
    while True:

        try:
            opcao = int(input(
                "\n[1]-> Cadastra produto no estoque\n[2]-> Lista produtos\n[3]-> Ver a quantidade dos itens no estoque\n[4]-> Volta ao menu principal\n Selecione -> \n"))
        except ValueError:
            print("Entrada invalida.\n")
            registrar_logs("erro", "string ao invés de um número inteiro. ")
            continue
        registrar_logs("info", "menu de estoque acessado. ")
        match opcao:
            case 1:
                print('[=== MENU DE CADASTRO DE PRODUTO ===]\n')
                nome_prod = nome_produto()
                descricao_prod = descricao()
                preco_prod = adicionar_preco()
                quantidade_prod = adicionar_quantidade()
                codigo_de_barras = input("Codigo de Barras: ")
                data_de_entrada = datetime.now().strftime('%d/%m/%Y - %H:%M')

                salvar_estoque = Estoque(
                    nome_prod, descricao_prod, preco_prod, quantidade_prod, codigo_de_barras, data_de_entrada)
                salvar_estoque.salvar_produto()

            case 2:
                Estoque.listar_produtos()

            case 3:
                Estoque.calcular_quantidade()

            case 4:
                break


def main3():
    ...


main1()
