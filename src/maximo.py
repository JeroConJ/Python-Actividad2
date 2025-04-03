def calc_mvp(round):
    max_pun = 0
    for elem in round:
        if (round[elem]['points'] > max_pun):
            mvp = elem
            max_pun = round[elem]['points']
    return mvp