import psycopg2

data = {
    'user': 'postgres',
    'password': 'coderslab',
    'host': "localhost",
    'dbname': 'messages_app'
}
def connect(connection_data=None):
    if connection_data is None:
        connection_data = data
    connection = psycopg2.connect(**connection_data)
    connection.autocommit = True
    return connection

if __name__ == '__main__':
    connection=connect()
    connection.close()