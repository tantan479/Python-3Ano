create schema ptk

CREATE TABLE ptk.usuario(
	id SERIAL NOT NULL,
	nome VARCHAR(255) NOT NULL,
	email VARCHAR(255) NOT NULL,
	senha VARCHAR(255) NOT NULL,
	CONSTRAINT pk_usuario PRIMARY KEY(id)
);

INSERT INTO ptk.usuario (nome,email,senha)
VALUES
  ('Oprah Sanchez','arcu@protonmail.org','SPR86NGP8WK'),
  ('Kiona William','dis.parturient@icloud.edu','BGS43OSA8BT'),
  ('Winifred May','nunc.interdum@protonmail.couk','WHW13OVW7BS'),
  ('Iona Franks','consequat.dolor@protonmail.edu','VYB72TNE2ES'),
  ('Daria Rowe','augue@aol.com','XSR54JVK5JR'),
  ('Amal Klein','nec.eleifend.non@google.ca','WJN73NMN2BC'),
  ('Maya Schultz','lorem.ac@google.ca','LCF87NYS7QD'),
  ('Brenden Whitehead','nec.metus@outlook.ca','DVD54NXU5EV'),
  ('Paul Patrick','ligula.nullam.feugiat@outlook.org','MCW25KVD3HV'),
  ('Abdul Parker','cum.sociis@outlook.org','RXO85OYG8WI');

INSERT INTO ptk.usuario (nome,email,senha)
VALUES
  ('Karleigh Daniels','nisi.aenean@hotmail.ca','TIN17ZIR2SL'),
  ('Orlando Sweeney','velit.eu.sem@outlook.edu','EWP55VBA1NR'),
  ('Zelda Carter','laoreet@yahoo.edu','PIB46FKV0BU'),
  ('Colorado Hoffman','cubilia@hotmail.edu','SIN52HRW2NT'),
  ('Charissa Hancock','pede.praesent.eu@yahoo.org','WBI81LPX4CA'),
  ('Roth Hendricks','sed.hendrerit@icloud.couk','AUF75BEX0VD'),
  ('Kasimir Lawson','fermentum.arcu@icloud.org','DHY66OGE4AJ'),
  ('Ali Talley','class.aptent.taciti@aol.edu','SFD19KMM1OE'),
  ('Florence Love','nisl.arcu@hotmail.net','LKH24GFT6MB'),
  ('Duncan Snow','sed.hendrerit@outlook.net','MKD47ALO8GJ');