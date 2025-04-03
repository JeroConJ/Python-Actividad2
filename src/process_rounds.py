from maximo import calc_mvp

def process_round(round):
    result = {}
    for elem in round:
        puntaje = round[elem]['kills'] * 3 + round[elem]['assists'] * 1
        muerte = 0
        if (round[elem]['deaths']):
            puntaje -= 1
            muerte = 1
        result[elem] = {'kills': round[elem]['kills'], 'assists': round[elem]['assists'], 'deaths': muerte, 'points': puntaje, 'mvp': 0}
    result[calc_mvp(result)]['mvp'] += 1
    return result