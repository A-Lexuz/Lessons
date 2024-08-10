

def is_prime(func):
    def wrapper(*args):
        sum = func(*args)
        if isinstance(sum, int):
            print('Простое')
        else:
            print("Составное")
        return sum
    return wrapper

@is_prime
def sum_three(a,b,c):
    return a+b+c

result = sum_three(2, 3, 6)
print(result)