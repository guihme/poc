from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from database import SessionLocal, engine
from models import Base
from repositories import DocenteRepository, DisciplinaRepository, InteresseDocenteRepository, HistoricoRepository
from sqlalchemy import text
import os

# Cria as tabelas no banco de dados, se não existirem
Base.metadata.create_all(bind=engine)

# Função para executar script SQL
def execute_sql_script(filename, session):
    with open(filename, 'r') as sql_file:
        sql_commands = sql_file.read().split(';')
        for command in sql_commands:
            if command.strip():
                sql_statement = text(command.strip() + ';')
                session.execute(sql_statement)
        session.commit()

# Caminho para o arquivo SQL de seed
sql_file_path = os.path.join(os.path.dirname(__file__), 'seed.sql')

# Criação da aplicação FastAPI
app = FastAPI()

# Dependência para obter a sessão do banco de dados
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Rota /start
@app.post("/start")
def start(db: Session = Depends(get_db)):
    # Executar script de seed para popular o banco de dados
    execute_sql_script(sql_file_path, db)

    # Consultar dados do banco de dados
    historicos = HistoricoRepository.find_all(db)
    docentes = DocenteRepository.find_all(db)
    disciplinas = DisciplinaRepository.find_all(db)
    interesses_docente = InteresseDocenteRepository.find_all(db)

    # Mapear cod_disc para disciplinas para facilitar a consulta
    cod_disc_to_disciplina = {disciplina.cod_disc: disciplina.id for disciplina in disciplinas}


    # Montar resposta JSON
    historico_dict = {}
    for historico in historicos:
        ano = historico.ano
        if ano not in historico_dict:
            historico_dict[ano] = []
        historico_dict[ano].append({
            "idDisc": cod_disc_to_disciplina.get(historico.codDisc),
            "idProfessor": historico.idProfessor
        })
    docente_dict = {}
    for docente in docentes:
        docente_dict[docente.id] = {
            "nome": docente.nome,
            "nucleoId": docente.nucleoId,
            "dataNucleo": docente.dataNucleo.isoformat(),
            "dataInf": docente.dataInf.isoformat()
        }

# Agrupar interesses do docente por idProfessor
    interesses_do_docente_dict = {}
    for interesse in interesses_docente:
        if interesse.idProfessor not in interesses_do_docente_dict:
            interesses_do_docente_dict[interesse.idProfessor] = {
                "idProfessor": interesse.idProfessor,
                "interresseDisciplina": []
            }
        interesses_do_docente_dict[interesse.idProfessor]["interresseDisciplina"].append(interesse.interesse_disciplina)

    interesses_do_docente_list = list(interesses_do_docente_dict.values())

    disciplinas_list = []
    for disciplina in disciplinas:
        disciplinas_list.append({
            "id": disciplina.id,
            "codDisc": disciplina.cod_disc,
            "nucleoId": disciplina.nucleoId
        })

    # Limpar o banco de dados após montar a resposta JSON
    db.execute(text("DELETE FROM historicos"))
    db.execute(text("DELETE FROM docentes"))
    db.execute(text("DELETE FROM disciplinas"))
    db.execute(text("DELETE FROM interesses_docentes"))
    db.commit()

    # Construir resposta final
    response = {
        "idProblema": 1,
        "historico": historico_dict,
        "docente": docente_dict,
        "interessesDoDocente": interesses_do_docente_list,
        "disciplinas": disciplinas_list
    }

    return response

# Inicialização da aplicação
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
