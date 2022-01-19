
def thesaurus(names):
    unique_letters = set([i[0] for i in names])

    dictionary = {}

    for i in unique_letters:
        dictionary.update({i:[]})

    for j in names:
        dictionary[j[0]].append(j)
        
    print(dictionary)

if __name__  == '__main__':
    names = ["Иван", "Мария", "Петр", "Илья"]
    thesaurus(names)