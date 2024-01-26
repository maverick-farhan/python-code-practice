def printTable(itemDict,leftWidth,rightWidth):
    print('Picnic Items'.center(leftWidth + rightWidth,'-'))
    for k,v in itemDict.items():
        print(k.ljust(leftWidth,'.')+str(v).rjust(rightWidth))

itemDict = {'sandwich':10,'dosa':10,'tea':2,'biryani':4}
printTable(itemDict,10,4)
printTable(itemDict,20,10)
