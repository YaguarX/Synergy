
show databases;
use synergy;
create table genress (id int, film_name varchar(20), genre varchar(20));
insert into genress (id, film_name, genre) values ('1', 'pervyi', 'boevik'),('2', 'ukrowenie', 'komedia'),('3', 'sila', 'boevik'),('4', 'mosh', 'boevik'),('5', 'drama', 'drama');
select * from genress;
