CREATE DATABASE IF NOT EXISTS postgres;

CREATE USER 'root' IDENTIFIED BY 'admin';
ALTER USER root with SUPERUSER;

CREATE TABLE IF NOT EXISTS keywords (

     first_keyword character(45),
);