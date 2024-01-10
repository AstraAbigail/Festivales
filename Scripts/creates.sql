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
precio DECIMAL(5,2) NOT NULL,
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

create table IF NOT EXISTS Sectores(
id int auto_increment  NOT NULL,
color VARCHAR(30) NOT NULL,
nombre VARCHAR(30),
fecha_inico datetime not null,
fecha_fin date not null,
butacas int not null,
primary key (id) 
);

/*con FK de menos a mas*/

create table IF NOT EXISTS Estadios(
id int auto_increment  NOT NULL,
nombre VARCHAR(50) NOT NULL,
direccion VARCHAR(50) not null,
correo varchar(50) not null,
telefono int not null,
capTotal int not null,
sectores int not null,
primary key (id),
FOREIGN KEY (sectores) REFERENCES Sectores(id) 
);

create table IF NOT EXISTS Inscripciones(
id int auto_increment  NOT NULL,
categoria int NOT NULL,
fecha    datetime not  null,
nombre varchar(50) not null,
detalle  varchar(100) not null,
correo  varchar(50)  not null,
primary key (id),
FOREIGN KEY (categoria) REFERENCES categorias(id) 
);

create table IF NOT EXISTS Eventos(
id int auto_increment  NOT NULL,
nombre  varchar(50) NOT NULL,
fecha    datetime not  null,
lugar int not null,
categoria int not null,
fechaHorarioInicio datetime not null,
fechaFinal date not null, 
primary key (id),
FOREIGN KEY (lugar) REFERENCES  estadios(id),
FOREIGN KEY (categoria) REFERENCES categorias(id)
);

create table IF NOT EXISTS Programacion(
id int auto_increment  NOT NULL,
evento int NOT NULL,
fecha   datetime not  null,
categoria int not null,
nombre int not null,
horaInicio time not null, 
primary key (id),
FOREIGN KEY (evento) REFERENCES eventos(id),
FOREIGN KEY (nombre) REFERENCES inscripciones(id)
);


create table IF NOT EXISTS Tickets(
id int auto_increment  NOT NULL,
cod int not null,
festival int not null ,
evento int NOT NULL,
fecha    date not  null,
categoria int not null,
nombre int not null,
sector int not null,
fila int not null,
butaca int not null,
precioSector decimal(7,2) not null,
tipoEntrada int not null,
precioEntrada decimal (7,2) not null,
cantidad int not null,
precioTotal decimal(7,2) not null,
eliminado varchar(10)not null,
primary key (id),
foreign KEY (festival) references eventos(id),
FOREIGN KEY (evento) REFERENCES estadios(id),
FOREIGN KEY (nombre) REFERENCES inscripciones(id),
FOREIGN KEY (sector) REFERENCES sectores(id),
FOREIGN KEY (tipoEntrada) REFERENCES tarifas(id)
);




