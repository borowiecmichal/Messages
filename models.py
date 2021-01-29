from connection import connect


class Users:
    def __init__(self, username='', password=''):
        self._id = None
        self.username = username
        self._password = password

    def set_password(self, password):
        self._password = password

    def save_to_db(self):
        if self._id == None:
            sql = f'''
            INSERT INTO users(username, password) VALUES ('{self.username}', '{self._password}') RETURNING id
            '''
            try:
                conn = connect()
                cursor = conn.cursor()
                cursor.execute(sql)
                self._id = cursor.fetchone()[0]
                conn.close()
                return True
            except Exception as e:
                conn.close()
                print('saving wasn\'t done')
                return False

        else:
            sql = f'''
            UPDATE users SET username = '{self.username}', password = '{self._password}' WHERE id={self._id}
            '''
            try:
                conn = connect()
                cursor = conn.cursor()
                cursor.execute(sql)
                conn.close()
                return True
            except Exception as e:
                conn.close()
                print('saving wasn\'t done')
                return False

    @staticmethod
    def load_user_by_username(username):
        sql = f"""
        SELECT * FROM users WHERE username='{username}';
        """
        try:
            conn = connect()
            cursor = conn.cursor()
            cursor.execute(sql)
            data = cursor.fetchone()
            conn.close()
            if data:
                loaded_user = Users()
                loaded_user._id = data[0]
                loaded_user.username = data[1]
                loaded_user._password = data[2]
                return loaded_user
        except Exception as e:
            print('searching failed')
            conn.close()
            return

    @staticmethod
    def load_user_by_id(id):
        sql = f'''
        SELECT * FROM users WHERE id={id}
        '''
        try:
            conn = connect()
            cursor = conn.cursor()
            cursor.execute(sql)
            data = cursor.fetchone()
            conn.close()
            if data:
                loaded_user = Users()
                loaded_user._id = data[0]
                loaded_user.username = data[1]
                loaded_user._password = data[2]
                return loaded_user
        except Exception as e:
            print('searcihng failed')
            conn.close()
            return None

    @staticmethod
    def load_all_users():
        sql = f'''
        SELECT * FROM users
        '''
        try:
            conn = connect()
            cursor = conn.cursor()
            cursor.execute(sql)
            result = cursor.fetchall()
            conn.close()
            users = []
            for user in result:
                loaded_user = Users()
                loaded_user._id = user[0]
                loaded_user.username = user[1]
                loaded_user._password = user[2]
                users.append(loaded_user)
            return users
        except Exception as e:
            conn.close()
            print('searcihng failed')
            return None

    def delete(self):
        sql = f'''
        DELETE FROM users WHERE id={self._id};
        '''
        try:
            conn = connect()
            cursor = conn.cursor()
            cursor.execute(sql)
            self._id = None
            conn.close()
            return True
        except:
            print('delating failed')
            conn.close()
            return False

    def __str__(self):
        return f'{self._id, self.username}'


class Messages:
    def __init__(self, from_id='', to_id='', msg=''):
        self._id = None
        self.from_id = from_id
        self.to_id = to_id
        self.msg = msg
        self.creation_date = None

    @property
    def id(self):
        return self._id

    def save_to_db(self):
        if self._id == None:
            sql = f'''
            INSERT INTO messages(from_id, to_id, msg) VALUES ({self.from_id},{self.to_id},'{self.msg}') RETURNING id, creation_date
            '''
            try:
                conn = connect()
                cursor = conn.cursor()
                cursor.execute(sql)
                data = cursor.fetchone()
                self._id = data[0]
                self.creation_date = data[1]
                conn.close()
                return True
            except Exception as e:
                print('saving failed')
                conn.close()
                return False
        else:
            sql = f'''
            UPDATE messages 
            SET from_id={self.from_id}, to_id={self.to_id}, creation_date='{self.creation_date}', msg='{self.msg}'
            WHERE id = {self.id}
            '''
            try:
                conn = connect()
                cursor = conn.cursor()
                cursor.execute(sql)
                conn.close()
                return True
            except Exception as e:
                conn.close()
                print('saving wasn\'t done')
                return False

    @staticmethod
    def load_all_messages():
        sql = '''
        SELECT * FROM messages
        '''
        try:
            conn = connect()
            cursor = conn.cursor()
            cursor.execute(sql)
            data = cursor.fetchall()
            msg_list = []
            for msg in data:
                message = Messages()
                message._id = msg[0]
                message.from_id = msg[1]
                message.to_id = msg[2]
                message.creation_date = msg[3]
                message.msg = msg[4]
                msg_list.append(message)
            conn.close()
            return msg_list

        except:
            conn.close()
            print('loading failed')

    def __str__(self):
        return f'from {self.from_id} to {self.to_id}: {self.msg}, {self.creation_date}'


if __name__ == '__main__':
    print(Messages.load_all_messages())
