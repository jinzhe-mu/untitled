a = 1.01
b = 0.99
c1 = a ** 365
c2 = b ** 365
print(a, "a的365次方是{}".format(c1))
print(b, "b的365次方是{}".format(c2))
if c1 > c2:
    print("每天进步一点点，成功就在不远处")
    print("无论基础多好，每天荒废一点点，失败终将降临")
else:
    print("no")