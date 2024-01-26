import pyperclip
text = pyperclip.paste()
txt_list = text.split('\n')
for i in range(len(txt_list)):
    txt_list[i] = '* '+txt_list[i]
    lines = '\n'.join(txt_list)
pyperclip.copy(lines)
print(lines)
