import math
def fact(n):
    fact = 1
    for i in range(1, n+1):
        fact = fact * i
    return fact

def choose(n, r):
    return fact(n)//(fact(r) * fact(n - r))

def binomial(number, total, success):
    return choose(total, number)*(success ** number)*((1-success) ** (total - number))

def binomialRange(start, finish, total, success):
    sum = 0
    for i in range(start, finish+1):
        sum=sum+(binomial(i, total, success))
    return sum

def xbar(arr):
    sum=0
    for item in arr:
        sum+=item
    return sum/len(arr)

def standardDeviation(arr):
	sum=0
	xb = xbar(arr)
	for item in arr:
		sum+=((item-xb)**2)
	n1 = len(arr)-1
	return math.sqrt(sum/n1)

def quadFormulaCalc(a, b, c):
    solution = set()
    value = (b ** 2) - (4 * a * c)

    if value < 0:
        print('there are no zeros in the function')
        return
    else:
        sq = math.sqrt(value)

    solution.add((-b + sq) / (2 * a))
    solution.add((-b - sq) / (2 * a))

    print(solution)

def momentumCalc(v, m, p):
    if v == "?": 
        if p == '?' or m == '?':
            return
        p = float(p)
        m = float(m)
        return p / m 
        
    elif p == "?": 
        if v == '?' or m == '?':
            print("invalid arguments")
            return
        m = float(m)
        v = float(v)
        return m * v 

    elif m == "?": 
        if p == '?' or v == '?':
            print("invalid arguments")
            return
        v = float(v)
        p = float(p)
        return p / v
    

def highMomentumCalc(v, m, p):

    c = 300000000
    
    if v == '?':
        
        if p == '?' or m == '?':
            print("invalid arguments")
            return
        m = float(m)
        p = float(p)
        vg = p / m
        return math.sqrt(((vg * c) ** 2)/((c ** 2) + (vg ** 2)))

    elif m == '?':
        if p == '?' or v == '?':
            print("invalid arguments")
            return
        v = float(v)
        p = float(p)
        gamma = 1 / (math.sqrt(1 - ((v / c) ** 2)))
        
        return p / (v * gamma)    

    elif p == '?':
        if v == '?' or m == '?':
            print("invalid arguments")
            return
        v = float(v)
        m = float(m)
        gamma = 1 / (math.sqrt(1 - ((v / c) ** 2)))
        return (v * m * gamma)
            
def truthTable(n):

    while (n.isnumeric() and int(n) >= 1) == False:
        print('invalid argument') 
    n = int(n)
    rows = (2 ** n)
    y = 112 
    listt = []

    for x in range(n):
        z = chr(y)
        y += 1
        listt.append(z)
    print(f'{listt}\n')
    listt = []

    y = 0

    for x in range(rows):
        y += 1
        for x in range(1, n + 1):
            e = (y // (2 ** (n - x)))
            r = (y % (2 ** (n - x)))

            if ((e % 2 == 1) and (r >= 1)) or ((e % 2 != 1) and (r < 1)):
                listt.append('T')
            else:
                listt.append('F')
        return(listt)