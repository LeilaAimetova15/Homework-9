def is_prime(func):
    def wrappper(*args):
        result = func(*args)
        value = True
        for i in range (2, result - 1):
            if result % i == 0:
                value = False
        if value:
            print('Простое')
        else:
            print('Составное')
        return result
    return wrappper

@is_prime
def sum_three(*args):
    return sum(args)

result = sum_three(2, 3, 6)
print(result)