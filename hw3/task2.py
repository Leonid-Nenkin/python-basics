
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
    
    isTitleCase = word.istitle()
    
    if isTitleCase:
        word = str.lower(word)

    try:
        res = dictionary[word]
    except KeyError:
        res = 'Невозможно перевести'

    if isTitleCase:
        res = str.title(res)
    
    return res


if __name__  == '__main__':
    print(num_translate("ten"))
    print(num_translate(""))
    print(num_translate("Ten"))
