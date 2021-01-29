from connection import connect


class Users:
    def __init__(self, username, password):
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

    def load_user_by_username(self):
        pass

    def load_user_by_id(self):
        pass

    def load_all_users(self):
        pass

    def delete(self):
        pass


if __name__ == '__main__':
    a = Users('ted', 'poiuytr')
    print(a.save_to_db())
