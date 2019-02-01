# -*- coding: utf-8 -*-
import pyodbc #подключаем библиотеку для работы с ODBC

server = 'ENCORE-PC\SQLEXPRESS01' #имя сервера
database = 'Rates' #имя базы данных
user = 'enCore' #имя пользователя
password = 'testpass2' #пароль

connection = pyodbc.connect('Driver={SQL Server Native Client 11.0};SERVER=' + server 
                            + ';DATABASE=' + database
                            + ';UID=' + user 
                            + ';PWD=' + password
                            +' ;Trusted_Connection=yes') #создание нового подключения
cursor = connection.cursor() #создаем специальный объект для выполнения запросов к БД
cursor.execute("""SELECT Ag_name, Rat_name, Grade, Outlook, Change, Date_str, Ent_name, Okpo, Ogrn, Inn, Finst, Ag_id, Rat_Sctr, Rat_type, Horizon, Scale_Typer, Currency, Backed_flag INTO [dbo].[Query_c] FROM [dbo].[Base] WHERE Rat_sctr = 'B'""") #выбираем поля в отдельную таблицу
connection.commit() #сохраняем изменения
cursor.close() #удаляем специальный объект
connection.close() #закрываем соединение
