n = int(input('Enter number of Commands:'))
M = []
for _ in range (n) :
    s = input('Enter the command:').split()
    if s[0] == 'append': 
        M.append(int(s[1]))
    elif s[0] == 'insert':
        M.insert(int(s[1]),int(s[2]))
    elif s[0] == 'remove':
        M.remove(int(s[1]))
    elif s[0] == 'pop':
        M.pop()
    elif s[0] == 'sort':
        M.sort()
    elif s[0] == 'print':
        print(M)
    else:
        M.reverse()