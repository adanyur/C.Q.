ALTER TABLE det_prog_equi_cq ADD COLUMN id integer
ALTER TABLE programacion_cq_d DROP CONSTRAINT xpkprogramacion_cq_d
ALTER TABLE participantes_cq ADD COLUMN  id integer
ALTER TABLE tipo_participantes_cq ADD COLUMN id integer 
ALTER TABLE programacion_cq_d ALTER COLUMN pl_codper TYPE varchar(8)
ALTER TABLE programacion_cq ALTER COLUMN cq_cama TYPE varchar(6)