
def read_file(filename):
    try:
        file = open(filename)
    except (TypeError, FileNotFoundError) as e:
        print(f'Error with filename: {e}')

    else:  # No Error occured
        print(file.read())
        file.close()

    finally:  # Executed always
        pass


read_file(None)


def fibonacci(n):
    if type(n) is not int:
        raise TypeError("n must be an integer")
    if n < 0:
        raise ValueError("n must be positive")
    if n > 2:
        return fibonacci(n-1) + fibonacci(n - 2)
    if 2 >= n >= 1:
        return 1 
    if n == 0:
        return 0

n = 7
print(f'Fib {n} = {fibonacci(n)}')

n = 7.5
print(f'Fib {n} = {fibonacci(n)}')


class FibError(TypeError):
    pass
