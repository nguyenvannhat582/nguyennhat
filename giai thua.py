def giaithua(n):
    #Tính giai thừa 1 số nhập từ bàn phím
    if n==1:
       return 1
    else:
       return (n*giaithua(n-1))
num=int(input("nhap so can tinh giai thua ---> "))
print("Giai thua cua so can tinh ---> ",giaithua(num))