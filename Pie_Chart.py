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
user_input = input('Enter date in numeric value (since 01.01.1900)\n')
date = [user_input]
cursor.execute("""SELECT Ag_name, Rat_name, Grade, Outlook, Change, Date_str, 
               Ent_name, Okpo, Ogrn, Inn, Finst, Ag_id, 
               Rat_Sctr, Rat_type, Horizon, Scale_Typer,
               Currency, Backed_flag INTO [dbo].[Query_{0}] 
               FROM [dbo].[Query_All]
               WHERE Date_str = '{0}'""".format(*date))
connection.commit()
cursor.execute("""Select Ag_name, COUNT(*) as Count INTO [dbo].[Pie_data_{0}] FROM [dbo].[Query_{0}] GROUP BY Ag_name""".format(*date))
connection.commit()

Query = """SELECT * FROM [dbo].[Pie_data_{0}]""".format(*date)
data = pd.read_sql(Query,connection)
cursor.execute(Query)

df = pd.DataFrame.from_records(cursor.fetchall(), columns = [desc[0] for desc in cursor.description])
Data = pd.DataFrame(data)

plt.figure(figsize=plt.figaspect(1))
labels=df['Ag_name']
sizes=df['Count']

def make_autopct(sizes):
    def my_autopct(pct):
        total = sum(sizes)
        val = int(round(pct*total/100.0))
        return '{p:.2f}%  ({v:d})'.format(p=pct,v=val)
    return my_autopct

plt.pie(sizes, labels=labels, autopct=make_autopct(sizes))
plt.show()

cursor.close() #удаляем специальный объект
connection.close() #закрываем соединение