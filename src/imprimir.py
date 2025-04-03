def imprimir_dic(round):
    for elem in round:
        if (len(elem) == 5):            #If hecho para mejorar la legibilidad de la tabla
            print(elem, end="     ")
        else:
            print(elem, end="    ")
        print(round[elem]['kills'], end="       ")
        print(round[elem]['assists'], end="            ")
        print(round[elem]['deaths'], end="        ")
        print(round[elem]['points'], end="       ")
        print(round[elem]['mvp'])