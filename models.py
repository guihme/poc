from sqlalchemy import Column, Integer, String, Date, ForeignKey
from sqlalchemy.orm import relationship

from database import Base

class Docente(Base):
    __tablename__ = "docentes"
    
    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String(100), nullable=False)
    nucleoId = Column(String(10), nullable=False)
    dataNucleo = Column(Date, nullable=False)
    dataInf = Column(Date, nullable=False)

class Disciplina(Base):
    __tablename__ = "disciplinas"
    
    id = Column(Integer, primary_key=True, index=True)
    cod_disc = Column(String(10), nullable=False)
    nucleoId = Column(String(10), nullable=False)

class InteresseDocente(Base):
    __tablename__ = "interesses_docentes"
    
    id = Column(Integer, primary_key=True, index=True)
    idProfessor = Column(Integer, ForeignKey('docentes.id'), nullable=False)
    interesse_disciplina = Column(Integer, ForeignKey('disciplinas.id'), nullable=False)
    
    docente = relationship("Docente", back_populates="interesses")
    disciplina = relationship("Disciplina", back_populates="interesses")

Docente.interesses = relationship("InteresseDocente", order_by=InteresseDocente.id, back_populates="docente")
Disciplina.interesses = relationship("InteresseDocente", order_by=InteresseDocente.id, back_populates="disciplina")


class Historico(Base):
    __tablename__ = "historicos"
    
    id = Column(Integer, primary_key=True, index=True)
    ano = Column(Integer, nullable=False)
    codDisc = Column(String(10), nullable=False)
    idProfessor = Column(Integer, nullable=False)