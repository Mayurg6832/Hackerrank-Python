if __name__ == '__main__':
    s = input()
flag=0
for i in s:
    if i.isalnum():
        flag=1
if flag == 1:
    print("True")
else: 
    print("False")
flag=0
for i in s:
    if i.isalpha():
        flag=1
if flag == 1:
    print("True")
else: 
    print("False")
flag=0    
for i in s:
    if i.isdigit():
        flag=1
if flag == 1:
    print("True")
else: 
    print("False")
flag=0
for i in s:
    if i.islower():
        flag=1
if flag == 1:
    print("True")
else: 
    print("False")
flag=0
for i in s:
    if i.isupper():
        flag=1
if flag == 1:
    print("True")
else: 
    print("False")