from database import Database
from aluno import Aluno
from Turmas import Turma


def criar_aluno(database):
    nome = input("Digite o nome do aluno: ")
    idade = int(input("Digite a idade do aluno: "))
    matricula = input("Digite a matrícula do aluno: ")

    aluno = Aluno(nome, idade, matricula)
    aluno.criar_no(database)

    print("Aluno criado com sucesso!")


def criar_turma(database):
    professor = input("Digite o nome do professor: ")
    horario = input("Digite o horário da turma: ")
    tag = input("Digite a tag da turma: ")

    turma = Turma(professor, horario, tag)
    turma.criar_no(database)

    print("Turma criada com sucesso!")


def adicionar_aluno_turma(database):
    matricula_aluno = input("Digite a matrícula do aluno: ")
    tag_turma = input("Digite a tag da turma: ")

    aluno = Aluno.buscar_por_matricula(database, matricula_aluno)
    turma = Turma.buscar_por_tag(database, tag_turma)

    if aluno is None:
        print("Aluno não encontrado.")
        return

    if turma is None:
        print("Turma não encontrada.")
        return

    turma.adicionar_aluno(aluno, database)

    print("Aluno adicionado à turma com sucesso!")


def devincular_aluno_turma(database):
    matricula_aluno = input("Digite a matrícula do aluno: ")
    tag_turma = input("Digite a tag da turma: ")

    aluno = Aluno.buscar_por_matricula(database, matricula_aluno)
    turma = Turma.buscar_por_tag(database, tag_turma)

    if aluno is None:
        print("Aluno não encontrado.")
        return

    if turma is None:
        print("Turma não encontrada.")
        return

    turma.devincular_aluno(aluno, database)

    print("Aluno desvinculado da turma com sucesso!")


def excluir_aluno(database):
    matricula = input("Digite a matrícula do aluno a ser excluído: ")

    aluno = Aluno.buscar_por_matricula(database, matricula)

    if aluno is None:
        print("Aluno não encontrado.")
        return

    aluno.excluir(database)

    print("Aluno excluído com sucesso!")


def excluir_turma(database):
    tag = input("Digite a tag da turma a ser excluída: ")

    turma = Turma.buscar_por_tag(database, tag)

    if turma is None:
        print("Turma não encontrada.")
        return

    turma.excluir(database)

    print("Turma excluída com sucesso!")


def atualizar_aluno(database):
    matricula = input("Digite a matrícula do aluno a ser atualizado: ")
    idade = int(input("Digite a nova idade do aluno: "))

    aluno = Aluno.buscar_por_matricula(database, matricula)

    if aluno is None:
        print("Aluno não encontrado.")
        return

    aluno.idade = idade
    aluno.atualizar(database)

    print("Aluno atualizado com sucesso!")


def atualizar_turma(database):
    tag = input("Digite a tag da turma a ser atualizada: ")
    novo_horario = input("Digite o novo horário da turma: ")

    turma = Turma.buscar_por_tag(database, tag)

    if turma is None:
        print("Turma não encontrada.")
        return

    turma.horario = novo_horario
    turma.atualizar(database)

    print("Turma atualizada com sucesso!")


def listar_alunos_turma(database):
    tag = input("Digite a tag da turma: ")

    turma = Turma.buscar_por_tag(database, tag)

    if turma is None:
        print("Turma não encontrada.")
        return

    alunos = turma.listar_alunos(database)

    print("Alunos na turma:")
    for aluno in alunos:
        print(f"Nome: {aluno.nome}")
        print(f"Idade: {aluno.idade}")
        print(f"Matrícula: {aluno.matricula}")
        print()


def menu(database):
    while True:
        print("----- MENU -----")
        print("1. Criar aluno")
        print("2. Criar turma")
        print("3. Adicionar aluno a uma turma")
        print("4. Devincular aluno de uma turma")
        print("5. Excluir aluno")
        print("6. Excluir turma")
        print("7. Atualizar aluno")
        print("8. Atualizar turma")
        print("9. Listar alunos de uma turma")
        print("0. Sair")

        opcao = input("Digite a opção desejada: ")

        if opcao == "1":
            criar_aluno(database)
        elif opcao == "2":
            criar_turma(database)
        elif opcao == "3":
            adicionar_aluno_turma(database)
        elif opcao == "4":
            devincular_aluno_turma(database)
        elif opcao == "5":
            excluir_aluno(database)
        elif opcao == "6":
            excluir_turma(database)
        elif opcao == "7":
            atualizar_aluno(database)
        elif opcao == "8":
            atualizar_turma(database)
        elif opcao == "9":
            listar_alunos_turma(database)
        elif opcao == "0":
            break
        else:
            print("Opção inválida. Tente novamente.")

        print()


# Configurações do banco de dados Neo4j
uri = "bolt://34.234.172.137:7687"
user = "neo4j"
password = "asterisks-expiration-kilometers"

# Criar instância da classe Database
database = Database(uri, user, password)

# Chamar o menu de interação
menu(database)

# Fechar a conexão com o banco de dados
database.close()
