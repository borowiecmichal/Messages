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
            user.password = new_pass
            user.save_to_db()

    elif option == 3:
        user = login()
        if user:
            user.delete()

    elif option == 4:
        users = Users.load_all_users()
        for item in users:
            print(f'Username: {item.username}')
