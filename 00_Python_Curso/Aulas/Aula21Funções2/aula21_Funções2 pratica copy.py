def fatorial(num=1):
    f=1
    for c  in range (num,0,-1):
        f*=c
    return f

f1 = fatorial(10)
f2 = fatorial(5)
f3 = fatorial(2)
f4 = fatorial(297)
f5 = fatorial()

print(f1)
print(f2)
print(f3)
print(f4)
print(f5)


