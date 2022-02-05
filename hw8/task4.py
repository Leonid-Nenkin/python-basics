import functools


def val_checker(callback):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args):
            assert callback(*args), f'wrong val -5'
            result = func(*args)
            return result
        return wrapper
    return decorator



@val_checker(lambda x: x > 0)
def calc_cube(x):
   return x ** 3

if __name__ == "__main__":
    print(calc_cube(-5))