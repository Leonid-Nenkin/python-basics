
def num_translate(word):
    dictionary = {
        'zero':'ноль',
        'one':'один',
        'two':'два',
        'three':'три',
        'four':'четыре',
        'five':'пять',
        'six':'шесть',
        'seven':'семь',
        'eight':'восемь',
        'nine':'девять',
        'ten':'десять',
    }

    try:
        res = dictionary[word]
    except KeyError:
        res = 'Невозможно перевести'
    return res


if __name__  == '__main__':
    print(num_translate("ten"))
    print(num_translate(""))