import codecs
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

def inverse(val):
    rev = ""
    for x in range(len(str(val)) -1 , -1, -1):
        rev += val[x]
    return rev

def PalindromicNumbers():
    exta = 100
    extb = 101
    num = 0
    temp = 0
    for x in range(0,898):
        for y in range(0,898):
            num = str((exta + x) * (extb + y))
            first_part = num[0 : int(len(num) / 2)]
            inv = inverse(str(num[int(len(num) / 2) : int(len(num))]))
            if first_part == inv:
                if int(num) > int(temp):
                    temp = num
    print(temp)

def PrimeFactors(val):
    factors = {}
    x = 2
    while val != 1:
        while val % x != 0:
            x += 1
        if x in factors:
            factors[x] += 1
        else:
            factors[x] = 1
        val = val / x
    return factors
        
def SmallestMultiple():
    factors = {}
    mdm = 1
    for i in range(1,20):
        f = PrimeFactors(i)
        for e in f:
            if e not in factors:
                factors[e] = f[e]
            elif f[e] > factors[e]:
                factors[e] = f[e]
    for fact in factors:
        mdm = mdm * (fact ** factors[fact])
    print(factors, mdm)

def SumSquareDifference(n):
    sumSquare = 0
    squareSum = 0
    for x in range(0, n +1):
        sumSquare += x**2
        squareSum += x
    print(squareSum ** 2 - sumSquare)

def isPrime(val):
    for x in range(2, val):
        if val % x == 0:
            return False
    return True

def PrimeNumber(n):
    counter = 0
    num = 2
    while counter < n:
        if isPrime(num):
            counter += 1
        num += 1
    print(num -1)
## needs improve

## To be continued
def LargestProductInASeries(n, path):
    f = codecs.open(path, "r", "utf-8")
    serie = f.read().replace("\r\n", "").replace("\n", "")
    f.close()
    max = 1
    for x in range (0, len(serie) +1):
        if x + n - 1  < len(serie):
            temp = 1
            for y in range(0, n):
                temp += temp * int(str(serie)[x + y])
            if temp > max:
                max = temp
    print(max)
    
if __name__ == "__main__":
    LargestProductInASeries(3, r"C:\Users\Stefano\Documents\Esercizi python\Euler-project-exercises\inputs\Largest product in a series.txt")    