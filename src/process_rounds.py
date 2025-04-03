from maximo import calc_mvp
from imprimir import imprimir_dic

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




rounds = [{
'Shadow': {'kills': 2, 'assists': 1, 'deaths': True},
'Blaze': {'kills': 1, 'assists': 0, 'deaths': False},
'Viper': {'kills': 1, 'assists': 2, 'deaths': True},
'Frost': {'kills': 0, 'assists': 1, 'deaths': False},
'Reaper': {'kills': 1, 'assists': 1, 'deaths': False}
}]

for i in range(len(rounds)):
    result = process_round(rounds[i])
print("""Ranking ronda 1 \nJugador   Kills   Asistencias  Muertes  Puntos  MVP \n""")
print('-' * 50)
imprimir_dic(result)
