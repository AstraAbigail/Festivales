/*inset tablas prefijadas*/

INSERT INTO categorias (descripcion)
VALUES 
("Musicales");

INSERT INTO categorias (descripcion)
VALUES 
("Gastronomicos"),
("Feriantes"),
("Todas");

DELETE FROM categorias;
select * from categorias;

/*-------------------------------------------*/

INSERT INTO tarifas (descripcion,precio)
VALUES 
("Menores",1200.00),
("Mayores",1500.00),
("Jubilados",500.00),
("Estudiantes",700.00);

select descripcion from tarifas where descripcion = "Estudiantes";
UPDATE tarifas SET descripcion = 'General_X', precio = 1200.00  WHERE id =13;
select * from tarifas;
DELETE FROM tarifas;

/*----------------------------------------*/

select * from estadios;
delete from estadios;

/*INSERT DE ESTADIO*/
INSERT INTO estadios (nombre,direccion,correo,telefono,capTotal)
VALUES
("Monumental","Av.Figueroa Alcorta 7597","monumentaltickets@gmail.com",2914444875,2000),
("La Estrella Predio","Av. Alem 1452","laestrella_@gmail.com",1122700647,100),
("Movistar Arena","Av.Figueroa Alcorta 140","arena@tickets.com",2914785487,500),
("Luna Park Vip","Callao 1450","callao_espectaculos@gmail.com",2915874587,1000);
select * from estadios;
select id from estadios where nombre = "Monumental" and  direccion = "Av.Figueroa Alcorta 7597" and correo="monumentaltickets@gmail.com";

/*INSERT DE SECTORES*/
INSERT INTO sectores(color,nombre,fila_inicio,fila_fin,precio,butacas,estadio,eliminado)
VALUES 
("Amarillo","A",1,21,1000,25,5,"No"),
("Verde","B",22,42,500,25,5,"No"),
("Violeta","C",43,63,250,25,5,"No"),
("Naranja","D",64,84,100,25,5,"No");


select id from sectores where nombre = "A";
SELECT fila_inicio,fila_fin  FROM Sectores WHERE estadio = 4;
select * FROM sectores;
DELETE  FROM SECTORES where estadio = 6;
/*mostrar estadio y sectores */
SELECT sectores.nombre as  Sector,sectores.color as Color,sectores.fila_inicio as FilaInicio ,sectores.fila_fin as FilaFin,sectores.butacas as Butacas
FROM sectores
INNER JOIN estadios ON sectores.estadio = estadios.id;

SELECT id from sectores where estadio = 6 and nombre = "A" and eliminado = 'No';

/**/
insert into usuarios (nombre,correo,usuario,contraseña,crearEvento,programacion,inscripciones,configuracion,tickets)
values("Abigail","astrabigail@gmail.com","Abigail","Abigail17&",1,1,1,1,1);
select * from usuarios;


/*EVENTOS*/
select *from eventos;
delete from eventos;

/*INSCRIPCIONES*/
INSERT INTO inscripciones(categoria,nombre,detalle,correo,eliminado)
VALUES 
("Musicales","Soledad","","presentaciones@soledad.com.ar","No"),
("Musicales","Los Pericos","","info@pericos.com","No"),
("Musicales","Alfonsina","","contrataciones_alfonsina@alfonsina.com","No"),
("Musicales","Una Mas","","info@unaMas.com.ar","No");

select *from  inscripciones;
delete from  inscripciones;

/*PROGRAMACION*/

select *from  programacion;
delete from  programacion;

/*TICKETS*/
select *from  tickets;
delete from  tickets where id = 3;
delete from tickets;
SELECT cod,fecha,sector,fila,butaca,cantidad,tipoEntrada,precioEntrada,precioSector,nombre,evento,festival FROM tickets  WHERE   eliminado = 'No' ;
select * from inscripciones where id=13;
SELECT id FROM tickets  WHERE nombre=13  and  festival= 22 and  eliminado = "No" and fecha="2023-11-26";
select * from eventos;
select * from inscripciones;

select id from tickets where  festival =22 and categoria = 17 and nombre=13 and fecha = "2023-11-26" and eliminado = 'No';
select * from categorias;


