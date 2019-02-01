# -*- coding: utf-8 -*-
import pyodbc #подключаем библиотеку для работы с ODBC
import pandas as pd
import matplotlib.pyplot as plt

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
date = input('Enter date in numeric value (since 01.01.1900)\n')
name = input('Agency name\n')

cursor.execute("""SELECT Ag_name, Rat_name, Grade, Outlook, Change, Date_str, 
               Ent_name, Okpo, Ogrn, Inn, Finst, Ag_id, 
               Rat_Sctr, Rat_type, Horizon, Scale_Typer,
               Currency, Backed_flag INTO [dbo].[Query_{1}] 
               FROM [dbo].[Query_All]
               WHERE Date_str = '{0}' AND Ag_name = '{1}'""".format(date, name))
connection.commit()

Query = """SELECT * FROM [dbo].[Query_{1}]""".format(date, name)
data = pd.read_sql(Query,connection)
cursor.execute(Query)

df = pd.DataFrame.from_records(cursor.fetchall(), columns = [desc[0] for desc in cursor.description])
Data = pd.DataFrame(data)
print(data)
cursor.close() #удаляем специальный объект
connection.close() #закрываем соединение