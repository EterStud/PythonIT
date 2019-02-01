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
                            +' ;Trusted_Connection=yes') #создание нового подключения
cursor = connection.cursor() #создаем специальный объект для выполнения запросов к БД			  
cursor.execute('SELECT * FROM dbo.Table_1') #создаем запрос всех строк
for row in cursor:
    print('row = %r' % (row,)) #выводим все строки таблицы
cursor.close() #удаляем специальный объект
connection.close() #закрываем соединение