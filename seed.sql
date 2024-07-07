INSERT INTO docentes (nome, nucleoId, dataNucleo, dataInf) VALUES
('Eliomar Araújo de Lima', '2.1', '2015-12-01', '2010-01-01'),
('Maria', '2.1', '1980-05-20', '2005-06-15'),
('José', '2.1', '1975-07-30', '2000-08-10'),
('Renato Bulcão', '2.1', '2008-09-15', '2013-02-28'),
('Jacson Rodrigues Barbosa', '2.1', '2011-03-05', '2016-07-20'),
('Plínio de Sá Leitão Júnior', '2.1', '2003-12-10', '2008-11-15');

INSERT INTO disciplinas (cod_disc, nucleoId) VALUES
('INF0287', '2.1'),
('INF0018', '2.1'),
('INF0283', '2.1'),
('INF0291', '2.1'),
('INF0294', '2.1'),
('INF0056', '2.1');

INSERT INTO interesses_docentes (idProfessor, interesse_disciplina) VALUES
(1, 1),
(1, 2),
(2, 2),
(2, 3),
(3, 4),
(3, 5);

INSERT INTO historicos (ano, codDisc, idProfessor) VALUES
(2022, 'INF0287', 6),
(2022, 'INF0018', 1),
(2022, 'INF0283', 5),
(2022, 'INF0291', 2),
(2022, 'INF0294', 3),
(2022, 'INF0056', 4),
(2023, 'INF0287', 4),
(2023, 'INF0018', 6),
(2023, 'INF0283', 5),
(2023, 'INF0291', 1),
(2023, 'INF0294', 2),
(2023, 'INF0056', 3);
