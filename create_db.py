from connection import connect
import psycopg2


def create_table_users():
    sql = '''
    CREATE TABLE users(
        id serial,
        username varchar(255),
        password varchar(80),
        PRIMARY KEY(id)
    );
    '''
    try:
        conn = connect()
        cursor = conn.cursor()
        cursor.execute(sql)
    except psycopg2.errors.DuplicateTable:
        print('Table users already exists')
    conn.close()


def create_table_messages():
    sql = '''
    CREATE TABLE messages(
        id serial,
        from_id integer,
        to_id integer,
        creation_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
        msg varchar(255),
        PRIMARY KEY(id),
        FOREIGN KEY(from_id) REFERENCES users(id) ON DELETE CASCADE,
        FOREIGN KEY(to_id) REFERENCES users(id) ON DELETE CASCADE
    );
    '''
    try:
        conn = connect()
        cursor = conn.cursor()
        cursor.execute(sql)
    except psycopg2.errors.DuplicateTable:
        print('Table messages already exists')
    conn.close()




if __name__ == '__main__':
    create_table_users()
    create_table_messages()
