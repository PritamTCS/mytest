a = 0
b = 1

fibo = [a,b]

while(b<70):
    a,b = b, a+b
    fibo.append(b)

print(fibo)
