from ordenar import ordenar_dic

def imprimir_dic(round):
    round = ordenar_dic(round)
    for elem in round:
        if (len(elem) == 5):            #If hecho para mejorar la legibilidad de la tabla
            print(elem, end="    ")
        else:
            print(elem, end="   ")
        print(round[elem]['kills'], end="      ")
        print(round[elem]['assists'], end="            ")
        print(round[elem]['deaths'], end="        ")
        print(round[elem]['mvp'], end="    ")
        print(round[elem]['points'])