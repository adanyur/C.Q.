CREATE TABLE incidencia (
	id serial4 NOT NULL,
	fecha_incidencia date NULL,
	historia varchar(10) NULL,
	glosa text NULL,
	turno bpchar(1) NULL,
	estado char(1) NOT NULL,
	reporta_area varchar(50) NOT NULL,
	usuario_registro varchar(50) NULL,
	fecha_registro timestamp NULL,
	usuario_actualizado varchar(50) NULL,
	fecha_actualizado timestamp NULL,
	CONSTRAINT incidencia_pkey PRIMARY KEY (id)
);


CREATE TABLE public.incidencia_d (
	id serial4 NOT NULL,
	idincidencia int4 NULL,
	tipo int4 NULL,
	value int4 NULL,
	usuario_registro varchar(50) NULL,
	fecha_registro timestamp NULL,
	CONSTRAINT incidencia_d_pkey PRIMARY KEY (id),
	CONSTRAINT incidencia_d_idincidencia_fkey FOREIGN KEY (idincidencia) REFERENCES public.incidencia(id)
);

CREATE TABLE turno(
	id serial,
	descripcion,
	estado,
	fecha_registro,
	usuario
)





