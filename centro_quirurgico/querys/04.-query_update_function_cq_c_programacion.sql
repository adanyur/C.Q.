CREATE OR REPLACE FUNCTION public.cq_c_programacion(p_fecha character varying)
 RETURNS SETOF tpy_cqprog
 LANGUAGE plpgsql
AS $function$
DECLARE
data tpy_cqprog;
BEGIN
  for data in
	select
	right('00'||RTRIM(cast(date_part('hour',p.cq_hoinpr) as char(2))),2)||':'|| 	-- hora
	right('00'||RTRIM(cast(date_part('minute',p.cq_hoinpr) as char(2))),2)||' a '||	-- minuto
	right('00'||RTRIM(cast(date_part('hour',p.cq_hofipr) as char(2))),2)||':'||
	right('00'||RTRIM(cast(date_part('minute',p.cq_hofipr) as char(2))),2) as diahora,
	p.sa_codsal as sala,
	coalesce(rtrim(h.hc_apepat)||' '||rtrim(h.hc_apemat)||' '||', '||rtrim(hc_nombre),p.cq_paciente) as paciente,
	i.cq_nomint as intervencion, 
	coalesce(coalesce(rtrim(c.pl_nombre)||' '||c.pl_apepat||' '||c.pl_apemat,RTRIM(m.me_nombres)),'*NO SELECCIONADO*') as cirujano,
	t.an_nombre as anestesia,coalesce(ch.ch_numcam,'') as cama,coalesce(p.cq_pedido,'') as pedido,d.ar_codare||d.pl_codper as codmed,
	p.cq_numope,p.cq_fecha,p.cq_hoinpr,p.cq_hofipr,p.cq_hoinej,p.cq_hofiej,p.cq_indrep,p.cq_hoinre,p.cq_hofire,
	p.se_codigo,p.cq_codiqx as cq_codiqx,p.an_tipane,p.cq_cuenta,p.cq_numhis,p.cq_tipcon,p.cq_cama,p.cq_estado,p.cq_indfac,
	p.cq_edad as edad,
	p.cq_glosa_repro as glosa,
	p.cq_num_petito as npeti,
	coalesce(p.cq_es_emer,'0') as emer,
	coalesce(p.cq_orden_cq,'0') as ordecq,
	coalesce(p.cq_orden_rqx,'0') as orden_rqx,
	coalesce(p.cq_numsema,'') as semanas,
	coalesce(p.cq_areapre,'SD') as area,
	p.cq_codiqx2 as cq_codiqx2,
	(case when p.cq_areapre = 'SD' then 'X' else '' end)  as sd,
	(case when p.cq_areapre = 'RE' then 'X' else '' end)  as re,
	(case when p.cq_areapre = 'HO' then 'X' else '' end)  as ho,	
	(case when p.cq_orden_cq = '1' then 'SI' else 'NO' end)  as oiqx,
	(case when p.cq_orden_rqx = '1' then 'SI' else 'NO' end)  as rqx,
	coalesce(ii.cq_nomint,'') as intervencion2,
	coalesce(
	(
		select coalesce(rtrim(c.pl_nombre)||' '||c.pl_apepat||' '||c.pl_apemat,RTRIM(m.me_nombres))
		from programacion_cq_d x 
		left outer join personal c on x.pl_codper = c.pl_codper
		left outer join medicos m on x.pl_codper = m.me_codigo
		where x.cq_codpar = '05' and x.cq_numope = p.cq_numope
	),'    (Sin Asignar)') as anestesiologo,  
	coalesce(p.cq_es_adelan,'0') as adelantado,
	(case when p.cq_areapre = 'EM' then 'X' else '' end)  as em,
	coalesce(cq_enfer,'0') as enfer,
	coalesce(cq_antibio,'') as antibio,
	coalesce(cq_kg,'0') as kg,
	coalesce(cq_btb,'0') as btb,
	coalesce(cq_reing,'0') as reing,
	coalesce(cq_estancia,'0') as estancia,
	p.cq_codiqx3 as cq_codiqx3,
	coalesce(iii.cq_nomint,'') as intervencion3,
	coalesce(cq_motivo_suspen,'') as motivo_suspen,m.cmdco,coalesce(cq_hg,'0') as hg,h.hc_sexo as sexo,
	intervencion.tiempo AS tiempo,
	informeOperatorio.isInfoOperatorio AS inf_ope
	from programacion_cq p
	left outer join historias h on p.cq_numhis = h.hc_numhis
	left outer join intervenciones_cq i on p.cq_codiqx = i.cq_codiqx
	left outer join intervenciones_cq ii on p.cq_codiqx2 = ii.cq_codiqx
	left outer join intervenciones_cq iii on p.cq_codiqx3 = iii.cq_codiqx
	left outer join tipo_anestesia t on p.an_tipane = t.an_tipane
	inner join programacion_cq_d d on p.sa_codsal||p.cq_numope = d.sa_codsal||d.cq_numope
	left outer join personal c on d.pl_codper = c.pl_codper
	left outer join medicos m on d.pl_codper = m.me_codigo
	left outer join camas_hosp ch on p.cq_cama=ch.ch_codigo,
	LATERAL(SELECT cq_tiempo AS tiempo FROM intervenciones_cq a WHERE a.cq_codiqx=p.cq_codiqx) AS intervencion,
	LATERAL(SELECT COUNT(*) > 0 AS isInfoOperatorio FROM informe_operatorio b WHERE b.cq_numope =p.cq_numope) AS informeOperatorio
	where p.cq_estado <> '3' and d.cq_codpar = '01'
	and extract(year from p.cq_hoinpr) = extract(year from to_date(p_fecha,'dd/mm/yyyy'))
	and extract(month from p.cq_hoinpr) = extract(month from to_date(p_fecha,'dd/mm/yyyy'))
	and extract(day from p.cq_hoinpr) = extract(day from to_date(p_fecha,'dd/mm/yyyy'))
	order by p.cq_hoinpr,p.sa_codsal 
  loop
  return next data;
  end loop;
END;
$function$
;
