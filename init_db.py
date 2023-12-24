from app.config import settings

import psycopg2

table_query = 'CREATE TABLE visited_link (id INT PRIMARY KEY, link VARCHAR NOT NULL, domain VARCHAR NOT NULL, visited_at BIGINT)'


server_connection = psycopg2.connect(host=settings.db_host,
                                     port=settings.db_port,
                                     user=settings.db_user, 
                                     password=settings.db_password)
server_cursor = server_connection.cursor()
server_connection.autocommit = True
try:
    server_cursor.execute(f'CREATE DATABASE {settings.db_name}')
    server_cursor.execute(f'CREATE DATABASE {settings.test_db_name}')
except psycopg2.errors.DuplicateDatabase:
    pass

server_cursor.close()
server_connection.close()
