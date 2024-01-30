#Q.1 Make a simple login application using Decision making statements with login success & fail message
def login():
    correct_username = "webdev"
    correct_password = "pass123"

    input_username = input("Enter your username: ")
    input_password = input("Enter your password: ")

    if input_username == correct_username and input_password == correct_password:
        print("Login successful! Welcome, {}".format(correct_username))
    else:
        print("Login failed. Incorrect username or password.")

print("Simple Login Application")

login()
