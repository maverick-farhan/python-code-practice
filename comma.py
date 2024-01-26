#!/usr/bin/env python3
# def comma(params):
#     return ', '.join(params)
#
# spam = ['apples','bananas','mangoes','oranges','strawberry']
# Ques_note = "It's not the switches causing the double clicking in Logitech mice, it's Logitech running the switches well under the required voltage.
#
# I wouldn't look specifically for a mouse with omron japans with the idea that they're the fix when a Logitech mouse with them still developes a double click.
#
# Razer optical switches obviously won't double click, and I rarely hear of double click issues with Zowie mice. And some specific mice like the G305, even though it's Logitech, rarely double clicks as well.
# "
# ans_note = "Double isn't happen because of switch, but static electricity trapped in the components in the mice"
# print(comma(spam))
# birthDays = {"Alice":"Apr 1","Imran":"June 16","Mobashara":"Apr 2","Salman":"Feb 24"}
# # print("Enter days in the format as 'Apr 1'")
# def returnBirthInfo(params):
#     return str(birthDays)
# while True:
#     print('Enter a name: (Enter to quit)')
#     name = input()
#     if(name ==''):
#         break
#     if name in birthDays:
#         print('Birthday of '+ name + " is "+birthDays[name])
#     else:
#         print("I do not have birthday information for "+ name)
#         print('What is thier birthday date?')
#         bday = input()
#         birthDays[name]=bday
#         print('Birthday database updated')
#
# print('Info: '+ returnBirthInfo(birthDays))
import pprint
message = 'abcdefghijklmnopqrstuvwxyz'
count = {}

for character in message:
    count.setdefault(character,0)
    count[character] = count[character] + 1

print(pprint.pformat(count))
print(len(count.keys()))

