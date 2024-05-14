def test(*args):
    print(args)
test(1, True, [1, 2, 3], "Str")

def Factorial(n):
    if n == 0:
        return 0
    else:
        return n + Factorial(n - 1)
print(Factorial(14))