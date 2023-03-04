from random import randint
def minim(a, b):
    sp = [randint(0, a) for i in range(randint(1, b))]
    print(sp)
    for i in sp:
        return min(sp)


el1 = minim(10,10)
el2 = minim(5,15)
el3 = minim(15,6)
print(el1)
print(el2)
print(el3)