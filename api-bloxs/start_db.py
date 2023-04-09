import pymysql

conn = pymysql.connect(host='localhost',
                       port=3306,
                       user='root',
                       password='password')
try:
    with conn.cursor() as cursor:
        cursor.execute('CREATE DATABASE IF NOT EXISTS desafio;')
        

finally:
    conn.close()