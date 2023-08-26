while True:
    a = str(input('enter the minuend: '))
    b = str(input('enter the subtrahend: '))
    if int(a) > int(b):
        (a, b) = (b.zfill(len(a)), a)
    else:
        (a, b) = (a.zfill(len(b)), b)
    print(a, b)
    a = list(a)
    b = list(b)
    z = [0] * len(a)
    for i in range(len(a)):
        if a[i] == '0':
            a[i] = '1'
        elif a[i] == '1':
            a[i] = '0'
    for i in range(len(a) - 1, -1, -1):
        z[i] = int(a[i]) + int(b[i])
    z[-1] += 1
    for i in range(len(a) - 1, 0, -1):
        if z[i] > 1:
            c = z[i] // 2
            z[i] = z[i] % 2
            z[i - 1] += c
    z[0] = z[0] % 2
    d = 0
    z.reverse()
    for i in range(len(z) - 1, -1, -1):
        d += z[i] * (2 ** i)
    z.reverse()
    print(z, "=", d)