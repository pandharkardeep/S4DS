cube = lambda x: x*x*x

def fibonacci(n):
    if n == 0 :
        return [0]
    elif n == 1:
        return [0,1]
    a = 0
    b = 1
    M = [0,1]
    for _ in range(n-2):
        c = a+b
        M.append(c)
        a = b
        b = c
    return M
        
    

if __name__ == '__main__':
    n = int(input())
    print(list(map(cube, fibonacci(n))))