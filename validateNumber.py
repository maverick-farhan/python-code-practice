import re
# phone_number_regex_pattern = re.compile(r'\d{3}-\d{3}-\d{4}')
# number_check_object = phone_number_regex_pattern.search('My number is 415-514-4343')
# print('Phone number found: '+number_check_object.group())
#
phone = re.compile(r'\d+\s\w+')
number = phone.findall('12 drummers, 11 pipers, 10 lords, 9 ladies, 8 maids, 7 swans, 6 geese, 5 swans, 4 birds, 1 dove')
number[0] = '14 drummers'
for items in number:
    print(items)
