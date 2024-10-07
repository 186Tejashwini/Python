def input_email(email):
    if "@" in email and "." in email.split('@')[-1]:
        print("It is a valid email")
    else:
        print("It is not a valid email")
        return

# Taking input from the user
email = input("Enter your email: ")
input_email(email)
