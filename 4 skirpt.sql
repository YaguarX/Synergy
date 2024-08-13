use synergy;
create table passport (
id int primary key auto_increment, 
number tinyint,
series tinyint,
how_were varchar(150),
when_was varchar(20),
pod_code varchar(10));


create table cityzen (
id int primary key auto_increment,
second_name varchar(50),
first_name varchar(50),
third_name varchar(50),
birth_date varchar(20),
foreign key (id) references passport(id));


create table flat (
id int primary key auto_increment,
full_adress varchar(150),
owner_name varchar(150),
foreign key (id) references cityzen(id));


create table pets (
id int primary key auto_increment,
klichka varchar(50),
poroda varchar(50),
animal_type varchar(50),
owner_name varchar(120),
foreign key (id) references cityzen(id));
