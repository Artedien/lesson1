def get_summ(one, two, delimiter = '&'):
    one = str(one)
    two = str(two)
    summ = str(one +delimiter + two) .upper()
    print(summ)


get_summ('learn', 'python')
