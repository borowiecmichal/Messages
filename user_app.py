from models import Users, Messages

while True:
    try:
        option = int(input('What you want to do?\n1: Create User\n2: Edit password\n3: Delete user\n4: See all users\nYour choice: '))
    except:
        print('Try again')
        continue
    if option == 1:
        try:
            username = input('Username: ')
            password = input('Password: ')
        except:
            print('Try again')
            continue
        new_user = Users(username, password)
        new_user.save_to_db()

    elif option == 2:
        username = input('Username: ')
        password = input('Old password: ')
        new_pass = input('New password: ')

        user = Users.load_user_by_username(username)
        if password == user._password:
            user.set_password(new_pass)
            user.save_to_db()


    elif option == 3:
        username = input('Username: ')
        password = input('Old password: ')

        user = Users.load_user_by_username(username)
        if password == user._password:
            user.delete()

    elif option == 4:
        users = Users.load_all_users()
        for item in users:
            print(f'Username: {item}')