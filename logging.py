#!/usr/bin/env python3
flag = True
print("SignIn")
print("Enter Your Name: ")
sName = input()
print("Enter Your Password")
sPasswd = input()
print("Congrats! Your account is created.\n")
print("Please login to use our resources...")
if(sName!='' and sPasswd !=''):
    while flag:
        print("Enter Your Name:")
        lName = input()
        print("Enter Your Passwd")
        lpasswd = input()
        if(lName == sName and lpasswd==sPasswd):
            print("Glad to see you onboard sir")
            flag = False
        else:
            print("Wrong credentials")
    
