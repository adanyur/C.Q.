CREATE OR REPLACE FUNCTION public.cq_c_disponibilidad_salas(fecha date, sala text)
 RETURNS SETOF ty_disponibilidad_salas
 LANGUAGE plpgsql
AS $function$
DECLARE data ty_disponibilidad_salas;	  
BEGIN

	FOR DATA IN 
		WITH horaInicioFinal AS (
			SELECT    (SELECT string_agg(a::TIME::TEXT, ' ') FROM 
					   	generate_series( (cq_fecha::date||' '||cq_hoinpr::TIME)::TIMESTAMP,
				   		(cq_fecha::date||' '||cq_hofipr::TIME)::TIMESTAMP,'30 minute') AS s(a)
					   ) AS descripcion
			FROM programacion_cq a 
			WHERE  cq_estado <> '3' 
			AND  sa_codsal = sala
			AND cq_fecha::DATE = fecha
		), disponibilidad  AS (
		SELECT 
				(ROW_NUMBER () OVER (PARTITION BY ''))::TEXT,
				horas::TIME AS horas,
				CASE 
				WHEN ocupado.hora IS NULL THEN 
				'DISPONIBLE'
				ELSE 
				'OCUPADO' 
				END AS descripcion,
				COALESCE(ocupado.hora=horas::TIME,FALSE) AS estaOcupado
		FROM generate_series( (CURRENT_DATE||' 07:00:00')::TIMESTAMP, 
			    (CURRENT_DATE + 1||' 06:30:00')::TIMESTAMP, '30 minute') AS s(horas)
		LEFT JOIN (SELECT DISTINCT regexp_split_to_table(descripcion,'\s+')::TIME  AS hora
					FROM horaInicioFinal) AS ocupado ON (horas::time=ocupado.hora)	    
		)SELECT * FROM disponibilidad
	LOOP
	RETURN NEXT DATA;
	END LOOP;

	
END;
$function$
;
