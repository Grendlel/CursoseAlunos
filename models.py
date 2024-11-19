from database import db

class Alunos(db.Model):
    __tablename__ = 'aluno'
    id = db.Column(db.Integer, primary_key = True)
    nome = db.Column(db.String(100))
    matricula = db.Column(db.String(50))

    def __init__(self, nome, matricula):
        self.nome = nome
        self.matricula = matricula

    def __repr__(self):
        return "<Aluno {}>".format(self.nome)

class Cursos(db.Model):
    __tablename__ = 'curso'
    id = db.Column(db.Integer, primary_key = True)
    nome = db.Column(db.String(100))
    duracao = db.Column(db.String(50))
    id_aluno = db.Column(db.Integer, db.ForeignKey('aluno.id'))
    
    aluno = db.relationship('Alunos', foreign_keys=id_aluno)

    def __init__(self, nome, duracao, id_aluno):
        self.nome = nome
        self.duracao = duracao
        self.id_aluno = id_aluno

    def __repr__(self):
        return "<Curso do Aluno {}>".format(self.nome)