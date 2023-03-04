from random import randint


# def summ(a, b):
#    c = []
#    sp = [randint(0, a) for i in range(randint(1, b))]
#    print(sp)
#    for i in sp:
#        while i < (b-1):
#            c.append(sp[i]+sp[i+1])
#        return c
# el1 = summ(10,3)
# print(el1)
# el2 = minim(3,15)
# print(el2)
# el3 = minim(15,6)
# print(el3)

def summ(l):
    c = []
    print(l)
    for i in range(len(l)):
        if i == 0:
            c.append(l[i])
        else:
            c.append(c[i - 1] + l[i])
    return c


el1 = summ([3, 9, 1])
print(el1)
el2 = summ([2, 5, 4, 2])
print(el2)
el3 = summ([3, 5, 10, 6, 3])
print(el3)
