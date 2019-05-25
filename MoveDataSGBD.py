#!/usr/bin/env python3


# Esse script visa buscar informações em um sistema Windows com MSSQL,
# para um sistema Linux com MySQL ou Mariadb.
# O objetivo é usar determinados campos para usuário e senha 
# em um Freeradius.

# Criei várias versões desse escript porque 
# conforme o projeto avançava, vi a necessidade
# de tratar a importação de algumas informações ao 
# inserir os dados no banco do Freeradius.

import pyodbc
import mysql.connector as mariadb

#Conexão windows mssql
connection_mssql=pyodbc.connect('DRIVER=FreeTDS;'\
                                'SERVER=192.168.0.175;'\
                                'PORT=1433;'\
                                'DATABASE=mydatabase;'\
                                'UID=sa;PWD=senha@123;'\
                                'TDS_Version=8.0;')
conn_mssql=connection_mssql.cursor()

#Conexão  linux mariadb                              
connection_mysql=mariadb.connect(host="localhost",
                                 user="root",
                                 passwd="senha@123",
                                 db="radius")

# Deletando todas as linhas
# O famoso delete sem where
conn_mysql=connection_mysql.cursor()
sql = ("delete from radcheck")
conn_mysql.execute(sql)
connection_mysql.commit()

#Ajustando o campo data
def ajusta(data):
	l = ''
	d1 = data.split('-')
	for i in d1[::-1]:
		l = l + i
	return l

for i in conn_mssql.execute("select username, birthday from client"):  
        cpf = i[0]
        data = i[1]
        data_nasc = ajusta(data)
        conn_mysql=connection_mysql.cursor()
        sql= ("insert into radcheck (username, value) values (%s,%s)")
        conn_mysql.execute(sql, (cpf, data_nasc))
        connection_mysql.commit()
      
conn_mssql.close()
a = conn_mysql.close()
connection_mssql.close()
connection_mysql.close()



