create table post_office_1 (
address varchar(50),
work_time varchar(50),
post_off_number tinyint primary key);

create table post_workers_1 (
FIO varchar(150),
address varchar(150),
passports_stats varchar(150),
wo_boo_num tinyint,
post_off_wor_place tinyint primary key,
foreign key (post_off_wor_place) references post_office_1 (post_off_number)
);

create table gifts (
category varchar(50),
veight float(50),
track_number tinyint,
post_off_wor_place_gift tinyint primary key,
foreign key (post_off_wor_place_gift) references post_office_1 (post_off_number)
);