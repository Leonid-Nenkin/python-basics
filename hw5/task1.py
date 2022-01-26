def odds(n):
    start = 1
    while start <= n:
        yield start
        start += 2

if __name__ == '__main__':
    for x in odds(10):
        print(x)