CREATE TABLE incidencia(
	id serial PRIMARY KEY,
	fecha date,
	historia VARCHAR(10),
	glosa text,
	turno char(2)
	usuario VARCHAR(50)
	fecha_registro TIMESTAMP,
	usuario_actualizado VARCHAR(50),
	fecha_actualizado TIMESTAMP
)

CREATE TABLE incidencia_d ( 
	id serial PRIMARY KEY,
	id_cabecera integer REFERENCES incidencia (id),
	tipo char(2),
	value char(2),
	fecha_registro TIMESTAMP,
	usuario varchar(50)
)

CREATE TABLE turno(
	id serial,
	descripcion,
	estado,
	fecha_registro,
	usuario
)





