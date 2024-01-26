all_guest = {
        "Akash":{'apple':5,'pizza':2},
        'Bob':{'sandwich':3,'cake':10},
        'Steve':{'biryani':5,'tea':2}
        }
def getItem(guests,item):
    number_brought = 0
    for k,v in all_guest.items():
        number_brought = number_brought + v.get(item,0)
        return number_brought

print('Number of things being brought:')
print('- Apple '+str(getItem(all_guest,'apple')))
print('- Cake '+str(getItem(all_guest,'cake')))
print('- Biryani '+str(getItem(all_guest,'biryani')))
print('- Cola '+str(getItem(all_guest,'cola')))
print('- Tea '+str(getItem(all_guest,'tea')))
