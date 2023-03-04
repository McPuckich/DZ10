sp1 = ["coolor", "fruit", "pet"]
sp2 = ["blue", "apple", "dog"]


sp3 = {x: y for x, y in zip(sp1, sp2)}
print(sp3)