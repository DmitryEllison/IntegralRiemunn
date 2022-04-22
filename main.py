import math
import matplotlib.pyplot as plt


def frange(x, y, jump):
    res = [x]
    while x < y:
        x += jump
        res.append(x)
    return res


def plotI(x,y):
    plt.scatter(x, y, s=[10]*len(x))
    plt.grid()
    plt.show()


def plotIH(x, y):
    len = round(max(x) - min(x))
    plt.step(x, y, where='mid')
    plt.fill()
    plt.grid()
    plt.show()


def sumI(x, y):
    sum = 0
    for i in range(2, len(x)):
        # серединные точки
        sum += y[i-1]*(x[i]-x[i-1])
    return sum


def acurracy(num, n):
    # правые точки
    # f'(x) = -exp(-x)
    # max(f') = -1/e
    return abs(num) < abs()


t = 10

x = frange(0, 1, 1/t)
print(len(x))
y = [math.exp(-(y+0.5/t)) for y in x]

sum = 0
for i in range(0, len(x)-1):
    # серединные точки
    sum += y[i]*(x[i+1]-x[i])


print(sumI(x, y))
print(1-math.exp(-1))
