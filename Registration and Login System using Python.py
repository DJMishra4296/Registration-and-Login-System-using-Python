import string


def validate_email(email):
    if '@' in email and '@' != email[-1] and '@' != email[0] and email.count('@') == 1 and len(email) > 1:
        first_part = email.split('@')[0]
        second_part = email.split('@')[1]

        if '.' in second_part and '.' != second_part[0] and len(second_part) > 1 and '.' != second_part[-1]:
            return True
        else:
            return False
    else:
        return False


def validate_password(password):
    is_special = False
    is_digit = False
    is_upper = False
    is_lower = False
    is_alpha = False

    # pass@123

    if len(password) > 5 and len(password) < 16:
        for i in password:

            if i in string.punctuation:
                is_special = True

            if i.isnumeric():
                is_digit = True

            if i.isalpha():
                is_alpha = True

            if i.islower():
                is_lower = True

            if i.isupper():
                is_upper = True

        if is_special and is_digit and is_lower and is_upper and is_alpha:
            return True
        else:
            return False


def validate_credentials(email, password):
    return validate_email(email) and validate_password(password)


def store_password(email, password):
    with open('credential_store.txt', 'a+') as f:
        f.write(f'{email} {password}\n')


def get_credentials(filename='credential_store.txt'):
    credentials = []
    with open(filename, 'a+') as f:
        f.seek(0)
        lines = f.readlines()
        for i in lines:
            i_id = i.split()[0]
            i_pass = i.split()[1]
            credentials.append([i_id, i_pass])


    return credentials


def login(email, password):
    credentials = get_credentials()

    for i in credentials:
        if email == i[0]:
            if password == i[1]:
                return True

    return False


def forgot_password(email):
    credentials = get_credentials()

    for i in credentials:
        if email == i[0]:
            return i[1]

    return False


def interface():
    ask = True
    email = None
    password = None

    while ask:
        print('Please Enter details for login - ')
        email = input('Enter Username: ')
        password = input('Enter Password: ')

        is_valid = validate_credentials(email, password)

        if is_valid:
            ask = False
        else:
            print('\nUsername or password is invalid, please enter them again')

    check_login = login(email, password)

    if check_login:
        print('You have successfully completed your login!')
        return
    else:
        user_choice = input('Cant find your details in the database: '
                            '\n Press 1. if you want to register\n Press 2. if you want to retrive your password'
                            '\n Your Choice:')
        if user_choice == '1':
            store_password(email, password)
            print('We have successfully registered you in the database!')
        elif user_choice == '2':
            f_email = input('Enter your email address again: ')
            forgotten_password = forgot_password(f_email)
            if forgotten_password:
                print(f'Your password is: {forgotten_password}')
            else:
                print('Cant find the password matching to the username in the database, please try again.')

        else:
            print('Invalid choice! Please try again later')


interface()
