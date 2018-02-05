#Create a script that lets the user submit a password until they have satisfied three conditions:
#1. Password contails at least one number
#2. Contains one uppercase letter
#3. It is at least 5 chars long
#Print out a message "Password is not fine" if the user didn't conreate a correct password

password = input("Enter a password: ")

if not any(char.isdigit() for char in password):
    print("Password is not fine")
elif not any(char.isupper() for char in password):
    print("Password is not fine")
elif len(password) < 5:
    print("Password is not fine")

'''
while True:
    psw = input("Enter new password: ")
    if any(i.isdigit() for i in psw) and any(i.isupper() for i in psw) and len(psw) >= 5:
        print("Password is fine")
        break
    else:
        print("Password is not fine")
'''
