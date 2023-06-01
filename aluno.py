class Aluno:
    def __init__(self, nome, idade, matricula):
        self.nome = nome
        self.idade = idade
        self.matricula = matricula

    def criar_no(self, database):
        query = """
        CREATE (aluno:Aluno {nome: $nome, idade: $idade, matricula: $matricula})
        """
        parameters = {"nome": self.nome, "idade": self.idade, "matricula": self.matricula}
        database.execute_query(query, parameters)

    def excluir(self, database):
        query = """
        MATCH (aluno:Aluno {matricula: $matricula})
        DETACH DELETE aluno
        """
        parameters = {"matricula": self.matricula}
        database.execute_query(query, parameters)

    def atualizar(self, database):
        query = """
        MATCH (aluno:Aluno {matricula: $matricula})
        SET aluno.nome = $nome, aluno.idade = $idade
        """
        parameters = {"matricula": self.matricula, "nome": self.nome, "idade": self.idade}
        database.execute_query(query, parameters)

    @staticmethod
    def buscar_por_matricula(database, matricula):
        query = """
        MATCH (aluno:Aluno {matricula: $matricula})
        RETURN aluno.nome AS nome, aluno.idade AS idade, aluno.matricula AS matricula
        """
        parameters = {"matricula": matricula}
        result = database.execute_query(query, parameters)

        if result:
            aluno_data = result[0]
            aluno = Aluno(aluno_data["nome"], aluno_data["idade"], aluno_data["matricula"])
            return aluno

        return None
