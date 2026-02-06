num1 = int(input('enter first number '))
num2 = int(input('enter second number '))
def gcf(x, y):
    for i in range(1, x + 1 and y + 1):
        if (x % i) == 0 and (y % i == 0):
            print(i)
gcf(num1,num2)