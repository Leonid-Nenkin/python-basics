
def type_logger(func):
   def wrapper(*args):
       result = func(*args)
       for i in [*args]:
           print(i, ": ", type(i))
       return result

   return wrapper


@type_logger
def calc_cube(x):
   return x ** 3

if __name__ == "__main__":
    calc_cube(5)