create database eventos;

/*tablas sin fk */
create table IF NOT EXISTS Categorias(
id  int  auto_increment NOT NULL,
descripcion VARCHAR(30) NOT NULL,
primary key (id) 
);

create table IF NOT EXISTS Tarifas(
id  INT  auto_increment NOT NULL,
descripcion VARCHAR(30) NOT NULL,
precio DECIMAL(7,2) NOT NULL,
primary key (id) 
);

create table IF NOT EXISTS Usuarios(
id int auto_increment  NOT NULL,
nombre VARCHAR (30) NOT NULL,
correo  VARCHAR (50) NOT NULL,
usuario VARCHAR (30) NOT NULL,
contraseña VARCHAR (30) NOT NULL,
crearEvento VARCHAR (1) NOT NULL,
programacion VARCHAR (1) NOT NULL,
inscripciones VARCHAR (1) NOT NULL,
configuracion VARCHAR (1) NOT NULL,
tickets VARCHAR (1) NOT NULL,
primary key (id) 
);
create table IF NOT EXISTS Estadios(
id int auto_increment  NOT NULL,
nombre VARCHAR(50) NOT NULL,
direccion VARCHAR(50) not null,
correo varchar(50) not null,
telefono bigint not null,
capTotal int not null,
primary key (id) 
);


/*con FK de menos a mas*/


create table IF NOT EXISTS Sectores(
id int auto_increment  NOT NULL,
color VARCHAR(30) NOT NULL,
nombre VARCHAR(50),
fila_inicio int not null,
fila_fin int not null,
precio decimal (7,2) not null,
butacas int not null,
estadio int not null,
eliminado varchar(10) not null,
primary key (id) ,
FOREIGN KEY (estadio) REFERENCES estadios(id) 
);

create table IF NOT EXISTS Inscripciones(
id int auto_increment  NOT NULL,
categoria varchar(50) NOT NULL,
nombre varchar(50) not null,
detalle  varchar(100) not null,
correo  varchar(50)  not null,
eliminado varchar(10) not null,
primary key (id)
);

create table IF NOT EXISTS Eventos(
id int auto_increment  NOT NULL,
nombre  varchar(50) NOT NULL,
lugar varchar(50) not null,
categoria varchar(50) not null,
fecha date not null,
hora time not null,
fechaFinal date not null, 
eliminado varchar(10) not null,
primary key (id)

);

create table IF NOT EXISTS Programacion(
id int auto_increment  NOT NULL,
evento varchar(50) NOT NULL,
fecha  date not  null,
categoria varchar(50) not null,
nombre varchar (50) not null,
horaInicio time not null,
eliminado varchar(10) not null, 
primary key (id)
);


create table IF NOT EXISTS Tickets(
id int auto_increment  NOT NULL,
evento varchar(50) NOT NULL,
fecha    datetime not  null,
categoria varchar(50) not null,
nombre varchar(50) not null,
sector varchar(10) not null,
fila int not null,
butaca int not null,
precioSector decimal(7,2) not null,
tipoEntrada varchar(50) not null,
precioEntrada decimal (7,2) not null,
cantidad int not null,
precioTotal decimal(7,2) not null,
eliminado varchar(10) not null,
primary key (id)

);




