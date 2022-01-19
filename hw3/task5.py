from random import randrange

def get_jokes(n):
    nouns = ["автомобиль", "лес", "огонь", "город", "дом"]
    adverbs = ["сегодня", "вчера", "завтра", "позавчера", "ночью"]
    adjectives = ["веселый", "яркий", "зеленый", "утопичный", "мягкий"]
    res = []

    for i in range(n):
        noun = randrange(len(nouns))
        adverb = randrange(len(adverbs))
        adjective = randrange(len(adjectives))

        res.append(nouns[noun]+ " " + adverbs[adverb] + " " + adjectives[adjective])

    return res
        


if __name__  == '__main__':
    print(get_jokes(2))