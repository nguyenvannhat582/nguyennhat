i = 2
while (i < 101):
    j = 2
    while (j < (i / j)):
        if i % j == 0:
            print("%d khong phai so nguyen to" %i)
            break
        j = j + 1
    else:
        print(i, "la so nguyen to")
    i = i + 1

