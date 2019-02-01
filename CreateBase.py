# -*- coding: utf-8 -*-
import pyodbc #подключаем библиотеку для работы с ODBC

server = 'ENCORE-PC\SQLEXPRESS01' #имя сервера
database = 'TestBase' #имя базы данных
user = 'enCore' #имя пользователя
password = 'testpass2' #пароль

connection = pyodbc.connect('Driver={SQL Server Native Client 11.0};SERVER=' + server 
                            + ';DATABASE=' + database
                            + ';UID=' + user 
                            + ';PWD=' + password
                            +' ;Trusted_Connection=yes',
                            autocommit = True) #создание нового подключения
cursor = connection.cursor() #создаем специальный объект для выполнения запросов к БД			  

cursor.execute('CREATE DATABASE Rates') #создаем запрос на создание БД
cursor.commit() #сохраняем изменения

cursor.execute('SELECT name FROM master.dbo.sysdatabases') #выполняем проверку
for db in cursor:
  print(db) #выводим список всех БД на сервере
cursor.close() #удаляем специальный объект
connection.close() #закрываем соединение