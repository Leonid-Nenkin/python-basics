from json.encoder import INFINITY


def print_gt_values(first_value, src):
    previous_value = first_value

    for i in src:
        if i > previous_value:
            yield i
        previous_value = i
            


if __name__ == '__main__':
    src = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]
    my_gen = print_gt_values(src[0], src[1:])
    res = []

    res.append(next(my_gen))
    res.append(next(my_gen))
    res.append(next(my_gen))
    res.append(next(my_gen))
    res.append(next(my_gen))
    res.append(next(my_gen))

    print(res)
