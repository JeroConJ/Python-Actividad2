def ordenar_dic(round):
    ordenado = {}
    for i in range(len(round)):
        max = 0
        for elem in round:
            if (round[elem]['points'] > max):
                max = round[elem]['points']
                max_jug = elem
        ordenado[max_jug] = round[max_jug]
        del round[max_jug]
    return ordenado