print("How old are you?")
def call():
    life = int(input("Tell me: "))
    if(life<=0):
        print("Sheesh! You not borned yet.")
    elif(life==1):
        print("I'm",life,"year old")
    elif(life>=70):
        print("I'm",life,"years old")
        print("Life is beautiful,but sometimes this world sucks?")
    else:
        print("I'm ", life,"years old")

call()