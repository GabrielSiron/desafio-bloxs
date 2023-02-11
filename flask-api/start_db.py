import pymysql

conn = pymysql.connect(host='localhost',
                       port=3306,
                       user='root',
                       password='password')
try:
    with conn.cursor() as cursor:
        cursor.execute('DROP DATABASE IF EXISTS desafio;')
        cursor.execute('CREATE DATABASE desafio;')
        

finally:
    conn.close()