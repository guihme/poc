from sqlalchemy.orm import Session
from models import Docente, Disciplina, InteresseDocente, Historico

class DocenteRepository:
    @staticmethod
    def find_all(db: Session) -> list[Docente]:
        return db.query(Docente).all()

    @staticmethod
    def save(db: Session, docente: Docente) -> Docente:
        if docente.id:
            db.merge(docente)
        else:
            db.add(docente)
        db.commit()
        return docente

    @staticmethod
    def find_by_id(db: Session, id: int) -> Docente:
        return db.query(Docente).filter(Docente.id == id).first()

    @staticmethod
    def exists_by_id(db: Session, id: int) -> bool:
        return db.query(Docente).filter(Docente.id == id).first() is not None

    @staticmethod
    def delete_by_id(db: Session, id: int) -> None:
        docente = db.query(Docente).filter(Docente.id == id).first()
        if docente is not None:
            db.delete(docente)
            db.commit()

class DisciplinaRepository:
    @staticmethod
    def find_all(db: Session) -> list[Disciplina]:
        return db.query(Disciplina).all()

    @staticmethod
    def save(db: Session, disciplina: Disciplina) -> Disciplina:
        if disciplina.id:
            db.merge(disciplina)
        else:
            db.add(disciplina)
        db.commit()
        return disciplina

    @staticmethod
    def find_by_id(db: Session, id: int) -> Disciplina:
        return db.query(Disciplina).filter(Disciplina.id == id).first()

    @staticmethod
    def exists_by_id(db: Session, id: int) -> bool:
        return db.query(Disciplina).filter(Disciplina.id == id).first() is not None

    @staticmethod
    def delete_by_id(db: Session, id: int) -> None:
        disciplina = db.query(Disciplina).filter(Disciplina.id == id).first()
        if disciplina is not None:
            db.delete(disciplina)
            db.commit()

class InteresseDocenteRepository:
    @staticmethod
    def find_all(db: Session) -> list[InteresseDocente]:
        return db.query(InteresseDocente).all()

    @staticmethod
    def save(db: Session, interesse_docente: InteresseDocente) -> InteresseDocente:
        if interesse_docente.id:
            db.merge(interesse_docente)
        else:
            db.add(interesse_docente)
        db.commit()
        return interesse_docente

    @staticmethod
    def find_by_id(db: Session, id: int) -> InteresseDocente:
        return db.query(InteresseDocente).filter(InteresseDocente.id == id).first()

    @staticmethod
    def exists_by_id(db: Session, id: int) -> bool:
        return db.query(InteresseDocente).filter(InteresseDocente.id == id).first() is not None

    @staticmethod
    def delete_by_id(db: Session, id: int) -> None:
        interesse_docente = db.query(InteresseDocente).filter(InteresseDocente.id == id).first()
        if interesse_docente is not None:
            db.delete(interesse_docente)
            db.commit()

class HistoricoRepository:
    @staticmethod
    def find_all(db: Session) -> list[Historico]:
        return db.query(Historico).all()

    @staticmethod
    def save(db: Session, historico: Historico) -> Historico:
        if historico.id:
            db.merge(historico)
        else:
            db.add(historico)
        db.commit()
        return historico

    @staticmethod
    def find_by_id(db: Session, id: int) -> Historico:
        return db.query(Historico).filter(Historico.id == id).first()

    @staticmethod
    def exists_by_id(db: Session, id: int) -> bool:
        return db.query(Historico).filter(Historico.id == id).first() is not None

    @staticmethod
    def delete_by_id(db: Session, id: int) -> None:
        historico = db.query(Historico).filter(Historico.id == id).first()
        if historico is not None:
            db.delete(historico)
            db.commit()