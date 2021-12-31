def task1():
    print(15 * 3)
    print(15 / 3)
    print(15 // 2)
    print(15 ** 2)

def change_arr():
    arr = ['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха', 'была', '+5', 'градусов']

    for i in range(len(arr)):
        if arr[i].isnumeric():
            if len(arr[i]) == 1:
                arr[i] = '"' + arr[i].zfill(2) + '"'
            else:
                arr[i] = '"' + arr[i] + '"'

        elif (arr[i][0] in ['+', '-']) & (arr[i][1:].isnumeric()):
            if len(arr[i][1:]) == 1:
                arr[i] = '"' + (arr[i][0]) + (arr[i][1:].zfill(2)) + '"'
            else:
                arr[i] = '"' + arr[i] + '"'
    
    print(" ".join(arr))


def proper_name(arr):
    for i in arr:
        name = i.split(' ')[-1:][0].title()
        print(f'Привет, {name}!')

if __name__ == '__main__':
    task1()
    change_arr()
    arr = ['инженер-конструктор Игорь', 'главный бухгалтер МАРИНА', 'токарь высшего разряда нИКОЛАй', 'директор аэлита']
    proper_name(arr)