show databases;
create database datarep;
use datarep;
create table student ( id int NOT NULL auto_increment, 
firstname varchar(100),  age int(3), PRIMARY KEY(id) );
insert into student (firstname, age) values ("joe",56); 
insert into student (firstname) values (’joe’); 
Delete from student where id = 1;
select * from student;
update student set firstname="mary" where id = 1;
create table book ( id int NOT NULL auto_increment, 
title varchar(100),  author varchar(100), price int(3), PRIMARY KEY(id) );
select * from book;
insert into book (title, author, price) values ("The Birds","seamus", 15); 
insert into book (title, author, price) values ("The Best of Luck","sally", 18); 