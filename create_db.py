import psycopg2

data = {
    'user': 'postgres',
    'password': 'coderslab',
    'host': "localhost"
}

def connect(connection_data=None):
    if connection_data is None:
        connection_data = data
    connection = psycopg2.connect(**connection_data)
    connection.autocommit = True
    return connection

def create_db():
    try:
        conn = connect()
        sql = '''
        CREATE DATABASE messages_app
        '''
        cursor = conn.cursor()
        cursor.execute(sql)
        conn.close()
    except psycopg2.errors.DuplicateDatabase:
        print('Database already exists')

if __name__ == '__main__':
    create_db()