from maximo import calc_mvp
from imprimir import imprimir_dic
from sumar_elems import sumar_dic

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



ranking_final = {}
rounds = [
{
'Shadow': {'kills': 2, 'assists': 1, 'deaths': True},
'Blaze': {'kills': 1, 'assists': 0, 'deaths': False},
'Viper': {'kills': 1, 'assists': 2, 'deaths': True},
'Frost': {'kills': 0, 'assists': 1, 'deaths': False},
'Reaper': {'kills': 1, 'assists': 1, 'deaths': False}
},
{
'Shadow': {'kills': 0, 'assists': 2, 'deaths': False},
'Blaze': {'kills': 2, 'assists': 0, 'deaths': True},
'Viper': {'kills': 1, 'assists': 1, 'deaths': False},
'Frost': {'kills': 2, 'assists': 1, 'deaths': True},
'Reaper': {'kills': 0, 'assists': 1, 'deaths': False}
},
{
'Shadow': {'kills': 1, 'assists': 0, 'deaths': False},
'Blaze': {'kills': 2, 'assists': 2, 'deaths': True},
'Viper': {'kills': 1, 'assists': 1, 'deaths': True},
'Frost': {'kills': 0, 'assists': 1, 'deaths': False},
'Reaper': {'kills': 1, 'assists': 1, 'deaths': False}
},
{
'Shadow': {'kills': 2, 'assists': 1, 'deaths': False},
'Blaze': {'kills': 1, 'assists': 0, 'deaths': True},
'Viper': {'kills': 0, 'assists': 2, 'deaths': False},
'Frost': {'kills': 1, 'assists': 1, 'deaths': True},
'Reaper': {'kills': 1, 'assists': 1, 'deaths': False}
},
{
'Shadow': {'kills': 1, 'assists': 2, 'deaths': True},
'Blaze': {'kills': 0, 'assists': 1, 'deaths': False},
'Viper': {'kills': 2, 'assists': 0, 'deaths': True},
'Frost': {'kills': 1, 'assists': 1, 'deaths': False},
'Reaper': {'kills': 1, 'assists': 1, 'deaths': True}
}
]

for i in range(len(rounds)):
    result = process_round(rounds[i])
    ranking_final = sumar_dic(ranking_final, result)
    print(f"Ranking ronda {i + 1} \nJugador  Kills  Asistencias  Muertes  MVP  Puntos")
    print('-' * 50)
    imprimir_dic(result)
    print('-' * 50)

print(f"Ranking final \nJugador  Kills  Asistencias  Muertes  MVP  Puntos")
imprimir_dic(ranking_final)