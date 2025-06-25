import statistics


notas = []


def cadastrar_notas():
    while True:
        try:
            nota = float(input("Digite a nota do aluno (ou -1 para parar): "))
            if nota == -1:
                break
            elif 0 <= nota <= 10:
                notas.append(nota)
            else:
                print("Nota inválida! Digite uma nota entre 0 e 10.")
        except ValueError:
            print("Entrada inválida! Digite um número válido.")


def visualizar_notas():
    if notas:
        print("\nNotas cadastradas:")
        for i, nota in enumerate(notas, start=1):
            print(f"Aluno {i}: {nota}")
        print(f"Total de alunos cadastrados: {len(notas)}\n")
    else:
        print("Nenhuma nota cadastrada.\n")


def calcular_estatisticas():
    if notas:
        media = statistics.mean(notas)
        maior = max(notas)
        menor = min(notas)
        print(f"\nMédia das notas: {media:.2f}")
        print(f"Maior nota: {maior}")
        print(f"Menor nota: {menor}\n")
    else:
        print("Nenhuma nota cadastrada para calcular estatísticas.\n")


def buscar_abaixo_da_media():
    if notas:
        media = statistics.mean(notas)
        abaixo = [nota for nota in notas if nota < media]
        print(f"\nNotas abaixo da média ({media:.2f}): {abaixo}\n")
    else:
        print("Nenhuma nota cadastrada.\n")


def filtrar_aprovados_reprovados():
    if notas:
        aprovados = [nota for nota in notas if nota >= 6]
        reprovados = [nota for nota in notas if nota < 6]
        print(f"\nAprovados (nota >= 6): {aprovados}")
        print(f"Reprovados (nota < 6): {reprovados}\n")
    else:
        print("Nenhuma nota cadastrada.\n")


def menu():
    while True:
        print("\n--- Sistema de Gerenciamento de Notas ---")
        print("1. Cadastrar notas")
        print("2. Visualizar todas as notas")
        print("3. Calcular estatísticas")
        print("4. Buscar notas abaixo da média")
        print("5. Filtrar aprovados e reprovados")
        print("6. Sair")
        opcao = input("Escolha uma opção: ")

        if opcao == '1':
            cadastrar_notas()
        elif opcao == '2':
            visualizar_notas()
        elif opcao == '3':
            calcular_estatisticas()
        elif opcao == '4':
            buscar_abaixo_da_media()
        elif opcao == '5':
            filtrar_aprovados_reprovados()
        elif opcao == '6':
            print("Saindo do sistema. Até logo!")
            break
        else:
            print("Opção inválida. Tente novamente.")


menu()
