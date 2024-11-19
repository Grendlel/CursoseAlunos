from flask import Blueprint, render_template, request, redirect, flash
from models import Cursos, Alunos
from database import db

bp_curso = Blueprint('cursos', __name__, template_folder="templates")

@bp_curso.route('/')
def index():
    dados = Cursos.query.all()
    return render_template('curso.html', cursos = dados)
    
@bp_curso.route('/add')
def add():
    a = Alunos.query.all()
    return render_template('curso_add.html', alunos = a)

@bp_curso.route('/save', methods=['POST'])
def save():
    nome = request.form.get('nome')
    duracao = request.form.get('duracao')
    id_aluno = request.form.get('id_aluno')
    if nome and duracao and id_aluno:
        bd_curso = Cursos(nome, duracao, id_aluno)
        db.session.add(bd_curso)
        db.session.commit()
        flash('Curso salvo com sucesso!!!')
        return redirect('/cursos')
    else:
        flash('Preencha todos os campos!!!')
        return redirect('/cursos/add')

@bp_curso.route("/remove/<int:id>")
def remove(id):
    dados = Cursos.query.get(id)
    if id > 0:
        db.session.delete(dados)
        db.session.commit()
        flash('Curso removido com sucesso!')
        return redirect("/cursos")
    else:
        flash("Caminho incorreto!")
        return redirect("/cursos")

@bp_curso.route("/edita/<int:id>")
def edita(id):
    curso = Cursos.query.get(id)
    aluno = Alunos.query.all()
    return render_template("curso_edita.html", dados=curso, aluno=aluno)

@bp_curso.route("/editasave", methods=['POST'])
def editasave():
    id = request.form.get('id')
    nome = request.form.get('nome')
    duracao = request.form.get('duracao')
    id_aluno = request.form.get('id_aluno')
    if id and nome and duracao and id_aluno:
        curso = Cursos.query.get(id)
        curso.nome = nome
        curso.duracao = duracao
        curso.id_aluno = id_aluno
        db.session.commit()
        flash('Dados atualizados com sucesso!')
        return redirect('/cursos')
    else:
        flash('Dados incompletos.')
        return redirect("/cursos")