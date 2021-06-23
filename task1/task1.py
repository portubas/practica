
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
    a1 = a1.capitalize()
    a1 = a1[:-1] + a1[-1].upper()
    print(a1)
    print(max(num_list))
    num_listWOL = num_list
    num_list.remove(max(num_listWOL))
    print(num_listWOL)
    num_listWOLnew = [i * i for i in num_listWOL]
    print (num_listWOLnew)







