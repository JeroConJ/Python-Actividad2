def sumar_dic(ranks, round):
    if (len(ranks) == 0):
        for elem in round:
            ranks[elem] = round[elem]
    else:
        for elem in ranks:
            ranks[elem]['kills'] += round[elem]['kills']
            ranks[elem]['assists'] += round[elem]['assists']
            ranks[elem]['deaths'] += round[elem]['deaths']
            ranks[elem]['mvp'] += round[elem]['mvp']
            ranks[elem]['points'] += round[elem]['points']
    return ranks