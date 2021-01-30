from models import Users, Messages
import hashing_password

def login():
    username = input('Username: ')
    password = input('Password: ')
    user = Users.load_user_by_username(username)
    try:
        if user and hashing_password.check_password(password, user.hashed_password):
            return user
        else:
            raise Exception
    except Exception:
        print('Wrong username or password')

#-Lr(O7M)ePo0!S4ac08c14916cc7d5af7dd48fb0c040e2b4771530317d6ef79557de037c60cd83
#YlOuANkay>nX}\Q177030fee1d85f15217290f8236d1154c6979936c5c908c823995f7289ebfa3c
while True:
    try:
        option = int(input(
            'What you want to do?\n1: Create User\n2: Edit password\n3: Delete user\n4: See all users\nYour choice: '))
    except ValueError:
        print('Try again')
        continue
    if option == 1:
        username = input('Username: ')
        password = input('Password: ')
        new_user = Users(username, password)
        new_user.save_to_db()

    elif option == 2:
        user = login()
        if user:
            new_pass = input('New password: ')
            user.set_password(new_pass)
            user.save_to_db()

    elif option == 3:
        user = login()
        if user:
            user.delete()

    elif option == 4:
        users = Users.load_all_users()
        for item in users:
            print(f'Username: {item.username}')
