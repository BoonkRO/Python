def factorial(n):
    assert isinstance(n, int), 'Not number or not positive.'
    assert (n>0)
    if n==0:
        return 1
    else:
        return n * factorial(n-1)


#print(factorialFor(0))
print(factorialFor(5))
#print(factorialFor(2.5))
#print(factorialFor("salchichon"))
#print(factorialFor(-5))