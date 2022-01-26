def tuples_generator(tutors, klasses):
    pos = 0

    for _ in tutors:
        if pos > (len(klasses) - 1):
            current_class = None
        else:
           current_class = klasses[pos]
        
        yield ((tutors[pos], current_class))
        pos += 1




if __name__ == '__main__':
    tutors = [
    'Иван', 'Анастасия', 'Петр', 'Сергей', 
    'Дмитрий', 'Борис', 'Елена'
    ]
    klasses = [
        '9А', '7В', '9Б', '9В', '8Б', '10А'
    ]

    tuples = tuples_generator(tutors, klasses)
    print(next(tuples))
    print(next(tuples))
    print(next(tuples))
    print(next(tuples))
    print(next(tuples))
    print(next(tuples))
    print(next(tuples))
    print(next(tuples))



