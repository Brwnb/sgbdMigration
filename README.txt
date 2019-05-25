###############################
# Informações sobre o Projeto #
###############################

O Linux utilizado nesse projeto foi CentOS 7


Esse projeto tem por objetivo mover informações
de um banco de dados MSSQL em um sistema Windows
para um sistema Linux em uma base de dados MySQL/Mariadb,
para a utilização de um freeradius como gerenciador
de senhas em uma determinada rede wifi.

Importante ressaltar que a senha desse projeto
é a data de nascimento do usuário. Por esse motivo
criei a função ajusta.

Outro ponto importante é que 
A priori tinha criado um banco para não aceitar dados repetidos e 
sem linhas vazias. Mas por motivos de força maior acabei tendo 
que criar um tratamento para essas sitauções.

Por esse motivo Pode haver várias versões desse código
nesse repositório.

----------------------------------------------

Drivers utilizados no Linux para conexão no MSSQL:
FreeDTS
UnixODBC
pyodbc

Drivers utilizados no Linux para conexão no Mysql/mariadb
mysql.connector
pymysql
