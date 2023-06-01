from aluno import Aluno
class Turma:
    def __init__(self, professor, horario, tag):
        self.professor = professor
        self.horario = horario
        self.tag = tag

    def criar_no(self, database):
        query = """
        CREATE (turma:Turma {professor: $professor, horario: $horario, tag: $tag})
        """
        parameters = {"professor": self.professor, "horario": self.horario, "tag": self.tag}
        database.execute_query(query, parameters)

    def excluir(self, database):
        query = """
        MATCH (turma:Turma {tag: $tag})
        DETACH DELETE turma
        """
        parameters = {"tag": self.tag}
        database.execute_query(query, parameters)

    def atualizar(self, database):
        query = """
        MATCH (turma:Turma {tag: $tag})
        SET turma.professor = $professor, turma.horario = $horario
        """
        parameters = {"tag": self.tag, "professor": self.professor, "horario": self.horario}
        database.execute_query(query, parameters)

    @staticmethod
    def buscar_por_tag(database, tag):
        query = """
        MATCH (turma:Turma {tag: $tag})
        RETURN turma.professor AS professor, turma.horario AS horario, turma.tag AS tag
        """
        parameters = {"tag": tag}
        result = database.execute_query(query, parameters)

        if result:
            turma_data = result[0]
            turma = Turma(turma_data["professor"], turma_data["horario"], turma_data["tag"])
            return turma

        return None

    def adicionar_aluno(self, aluno, database):
        query = """
        MATCH (turma:Turma {tag: $tag}), (aluno:Aluno {matricula: $matricula})
        CREATE (turma)-[:INSCRICAO]->(aluno)
        """
        parameters = {"tag": self.tag, "matricula": aluno.matricula}
        database.execute_query(query, parameters)

    def devincular_aluno(self, aluno, database):
        query = """
        MATCH (turma:Turma {tag: $tag})-[r:INSCRICAO]->(aluno:Aluno {matricula: $matricula})
        DELETE r
        """
        parameters = {"tag": self.tag, "matricula": aluno.matricula}
        database.execute_query(query, parameters)

    def listar_alunos(self, database):
        query = """
        MATCH (turma:Turma {tag: $tag})-[:INSCRICAO]->(aluno:Aluno)
        RETURN aluno.nome AS nome, aluno.idade AS idade, aluno.matricula AS matricula
        """
        parameters = {"tag": self.tag}
        result = database.execute_query(query, parameters)

        alunos = []
        for record in result:
            aluno = Aluno(record["nome"], record["idade"], record["matricula"])
            alunos.append(aluno)

        return alunos
