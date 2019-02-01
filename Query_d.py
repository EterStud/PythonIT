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
cursor.execute("""SELECT ID, Code_name, Agency, Full_Name_Rus, Full_Name_Eng, For_Instrument, For_Company INTO [dbo].[Query_d] FROM [dbo].[Ratings] WHERE For_Company = '1'""") #выбираем поля в отдельную таблицу
connection.commit() #сохраняем изменения
cursor.close() #удаляем специальный объект
connection.close() #закрываем соединение