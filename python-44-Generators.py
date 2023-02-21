#########-------------Generator----------###########

def topten():

    yield 1
    yield 4
    yield 5
    yield 8
    yield 3
    yield 2

values = topten()

print(values.__next__())
print(values.__next__())

for i in values:
    print(i)

print(" ")

def sqrten():

    n = 1

    while n <= 10:
        sq = n*n
        yield sq
        n = n+1

valuse = sqrten()

for i in valuse:
    print(i)
