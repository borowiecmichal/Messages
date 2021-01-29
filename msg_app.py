from models import Users, Messages

while True:
    try:
        option = int(input('What you want to do?\n1: See your messages\n2: Send message\nYour choice: '))
    except:
        print('Try again')
        continue

    if option == 1:
        username = input('Username: ')
        password = input('Password: ')
        user = Users.load_user_by_username(username)
        if password == user._password:
            Messages.load_all_messages()
            ###################

    elif option == 2:
        username = input('Username: ')
        password = input('Password: ')
        user = Users.load_user_by_username(username)
        if password == user._password:
            adresat = input('To whom you want to send your message')
            adresat = Users.load_user_by_username(adresat)
            msg = input('Write your message: ')
            new_msg = Messages(user._id, adresat._id, msg)
            new_msg.save_to_db()
