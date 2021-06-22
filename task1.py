
a = input()
num_list = []

num = ''
for char in a:
    if char.isdigit():
        num = num + char
    else:
        if num != '':
            num_list.append(int(num))
            num = ''
if num != '':
    num_list.append(int(num))
    a1 = "".join(c for c in a if c.isalpha())
    print(a1)
    print(num_list)




