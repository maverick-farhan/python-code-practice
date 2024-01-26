def validate_age():
    while True:
        print("Enter your age man: ")
        age = input()
        if age.isdecimal:
            print("Your age: "+ age)
            break
        print("Please enter a number for your age")

def validate_passwd():
    while True:
        print("Enter password with numbers and alphabets only: ")
        passwd = input()
        if passwd.isalnum():
            print("Your password saved gracefully")
            break
        print("Use only alphabets and numbers only")

validate_age()
validate_passwd()
