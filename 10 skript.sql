
show databases;
use synergy;
create table user (
id int primary key auto_increment,
FIO varchar(150),
password_hash varchar(20),
tel_number int);

alter table user modify column fio varchar(200);

create table history (
id int primary key,
service varchar(50),
date date,
master varchar(150),
foreign key (id) references user(id));

create index indx on history (id, master);


create table services (
id int primary key,
manik boolean,
pedik boolean,
haircut boolean,
haircoloring boolean,
master varchar (150),
foreign key (id) references history(id));

create index indx on services (master);

create table salary(
master varchar(150) ,
id int primary key,
diffic_kef float,
foreign key (id) references services (id)); 

