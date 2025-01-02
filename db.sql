create database if no exits employes;
use employes;
create table if not exits employes(
    id int primary key auto_increment,
    name varchar(100),
    email varchar(100),
    phone varchar(100),
    address varchar(100),
    created_at timestamp default current_timestamp
);