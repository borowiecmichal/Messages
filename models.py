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

    @staticmethod
    def load_user_by_username(username):
        sql = f"""
        SELECT * FROM users WHERE username='{username}';
        """
        try:
            conn = connect()
            cursor = conn.cursor()
            cursor.execute(sql)
            usr = cursor.fetchone()
            conn.close()
            return usr
        except Exception as e:
            print('searching failed')
            conn.close()
            return


    def load_user_by_id(self):
        pass

    def load_all_users(self):
        pass

    def delete(self):
        pass


if __name__ == '__main__':
    print(Users.load_user_by_username('xd'))
