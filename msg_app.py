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
        option = int(input('What you want to do?\n1: See your messages\n2: Send message\nYour choice: '))
    except:
        print('Try again')
        continue

    if option == 1:
        user = login()
        if user:
            a = Messages.load_all_messages(to_id = user.id)
            for item in a:
                user_from = Users.load_user_by_id(item.from_id)
                print(f'\nMessage from {user_from.username}:\n{item.msg}\nSent {item.creation_date}\n')
            if len(a) == 0:
                print('No messages for you')
    elif option == 2:
        user = login()
        if user:
            receiver = input('To whom you want to send your message')
            receiver = Users.load_user_by_username(receiver)
            msg = input('Write your message: ')
            new_msg = Messages(user.id, receiver.id, msg)
            new_msg.save_to_db()
