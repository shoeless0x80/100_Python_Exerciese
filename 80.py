#Create a script that lets the user submit a password until they have satisfied three conditions:
#1. Password contails at least one number
#2. Contains one uppercase letter
#3. It is at least 5 chars long
#Give the exact reason why the user has not created a correct Password

while True:
    psw = input("Enter new password: ")
    if not any(i.isdigit() for i in psw):
        print("Does not contain a digit!")
        print("Password is not fine")
    elif not any(i.isupper() for i in psw):
        print("Done not contain an uppercase character!")
        print("Password is not fine")
    elif len(psw) < 5:
        print("Not greater than 5 characters!")
        print("Password is not fine")
    else:
        print("Password is fine")
        break

'''
while True:
    notes = []
    psw = input("Enter password: ")
    if not any(i.isdigit() for i in psw):
        notes.append("You need at least one number")
    if not any(i.isupper() for i in psw):
        notes.append("You need at least one uppercase letter")
    if len(psw) < 5:
        notes.append("You need at least 5 characters")
    if len(notes) == 0:
        print("Password is fine")
        break
    else:
        print("Please check the following: ")
        for note in notes:
            print(note)
'''
