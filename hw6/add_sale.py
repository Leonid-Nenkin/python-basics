import sys

def add_sale(value):
    with open('bakery.csv', 'a', encoding='utf-8') as f:
        f.writelines(value+"\n")

if __name__=="__main__":
    if len(sys.argv) == 2:
        value = str(sys.argv[1])
    else:
        value = "0"
    
    add_sale(value)