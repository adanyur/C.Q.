CREATE TABLE iea_involucrados(
	id serial PRIMARY KEY,
	descripcion VARCHAR(50),
	estado BOOLEAN,
	usuario VARCHAR(50),
	fecha TIMESTAMP 
)

CREATE TABLE iea_invulucrados_d(
	id serial,
	idinvolucrados INTEGER REFERENCES iea_involucrados (id),
	descripcion VARCHAR(50),
	estado BOOLEAN,
	usuario VARCHAR(50),
	fecha TIMESTAMP
)