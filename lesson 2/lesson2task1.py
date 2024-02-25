def factorial():
    a = int(input())
    f = 1
    for i in range(a + 1):
        if i == 0:
            continue
        else:
            f = f * i
    return(f)

#print(factorial(6))

def maxnum():
    a = list(map(int, input().split()))
    b = max(a)
    return(b)

#print(maxnum())

def righttriangle():
    a = int(input())
    b = int(input())
    c = (a * b) / 2
    return(c)

#print(int(righttriangle()))

print(f' Чтобы решить факториал напишите "Факториал" \n Чтобы узнать максимлаьное число из трех, напишите "Максимум" \n Чтобы узнать площадь прямоугольного треугольника, напишите "Треугольник"')
functype = str(input())

if functype == "Факториал":
    print(factorial())
if functype == "Максимум":
    print(maxnum())
if functype == "Треугольник":
    print(int(righttriangle()))
