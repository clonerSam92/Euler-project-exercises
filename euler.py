from ast import Num


def EulerNum1():
    tot = 0
    for x in range(0,1000):
        if x % 5 == 0 or x % 3 == 0:
            tot += x
    print(tot)

def Fibonacci1():
    value = 0
    fSequence = []
    terma = 0
    termb = 1
    i = 0
    sommatoria = 0
    while value < 4000000:
        value = terma + termb
        fSequence.append(value)
        terma = termb
        termb = value
        if value%2 == 0:
            sommatoria += value
        i += 1
    print(sommatoria)

def LargestPrimeFactor():
    numero = 600851475143
    primi = []
    x = 2
    while numero != 1:
        while numero % x != 0:
            x += 1
        print(x)
        primi.append(x)
        numero = numero /  x
    print(primi)

def PalindromicNumbers():
    exta = 100
    extb = 101
    num = 0
    temp = 0
    for x in range(0,898):
        for y in range(0,898):
            num = str((exta + x) * (extb + y))
            inverse = num[ -0 : int(len(num) / 2)][-1] + num[ -0 : int(len(num) / 2)][-2]
            if inverse == num[int(len(num) / 2)+1  : int(len(num))]:
                if int(num) > int(temp):
                    temp = num
    print(temp)

if __name__ == "__main__":
    PalindromicNumbers()    