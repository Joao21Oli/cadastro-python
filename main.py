def mostrar_menu():
    print("\n=== Sistema de Cadastro ===")
    print("1 - Cadastrar pessoa")
    print("2 - Listar pessoas")
    print("3 - Buscar pessoa")
    print("4 - Sair")


pessoas = []

while True:
    mostrar_menu()
    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        nome = input("Nome: ")
        idade = input("Idade: ")
        pessoas.append({"nome": nome, "idade": idade})
        print("Pessoa cadastrada com sucesso!")

    elif opcao == "2":
        if not pessoas:
            print("Nenhuma pessoa cadastrada.")
        else:
            for p in pessoas:
                print(f"Nome: {p['nome']} | Idade: {p['idade']}")

    elif opcao == "3":
        busca = input("Digite o nome para buscar: ")
        encontrada = False
        for p in pessoas:
            if p["nome"].lower() == busca.lower():
                print(f"Encontrado: {p['nome']} - {p['idade']} anos")
                encontrada = True
                break
        if not encontrada:
            print("Pessoa não encontrada.")

    elif opcao == "4":
        print("Encerrando o sistema...")
        break

    else:
        print("Opção inválida!")
