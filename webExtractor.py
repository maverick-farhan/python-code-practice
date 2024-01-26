import re, pyperclip
phone_regex = re.compile(r'''(
                        (\d{3}|\(\d{3}\))?     #Area Code
                        (\s|-|\.)?
                        (\d{3})
                        (\s|-|\.)
                        (\d{4})
                        (\s*(ext|x|ext.)\s*(\d{2,5}))?
)''',re.VERBOSE)
#Create Email regex
email_regex = re.compile(r'''(
                         [a-zA-Z0-9._%+-]+
                         @
                         [a-zA-Z0-9.-]+
                         (\.[a-zA-Z]{2,4})
                         )''',re.VERBOSE)
string = pyperclip.paste()
(phone_regex.search(string))
(email_regex.search(string))
# (407)-243-4394
# contact@brandaffair.ro
# Amman St, no 35, 4th floor, ap 10, Bucharest
