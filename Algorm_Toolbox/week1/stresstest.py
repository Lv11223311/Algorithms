from product import Product
import numpy as np
while True:
    n = np.random.randint(2, 11)
    print(n)
    a = []
    for i in range(n):
        a.append(np.random.randint(1, 100000))
    for i in range(n):
        print(a[i])

    res1 = Product(a)
    res2 = Product(a)
    if res1 != res2:
        print("Wrong answer:{},{}".format(res1, res2))
        break
    else:
        print("ok!")
