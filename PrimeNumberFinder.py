#asal sayı bulma
x = 3
z = 0
a = input("Kaçıncı asal sayıya kadar öğrenmek istiyorsunuz: ") - 1
print("2 Asal sayıdır.")
c = 0
while a > c:
    b = int(x ** (1 / 2))
    for y in range(3,b + 1,2):
        if x % y == 0:
            z = 1
            break
    if z == 1:
        z = 0
    else:
        print(str(x) + "Asal sayıdır")
        c = c + 1
    x = x + 2
    z = 0
