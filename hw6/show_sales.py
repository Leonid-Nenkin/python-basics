import sys

def show_sales(file, start, end=""):
    sales = open(file).read().splitlines()

    if end == "":
        end = len(sales)
    else:
        end = min(len(sales), end+1)

    for i in range(start, end):
        print(sales[i])

if __name__=="__main__":
    file = 'bakery.csv'
    if len(sys.argv) == 3:
        start = int(sys.argv[1])
        end = int(sys.argv[2])
        show_sales(file, start, end)
    elif len(sys.argv) == 2:
        start = int(sys.argv[1])
        show_sales(file, start)
    
    