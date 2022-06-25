def contador(i, f, p):
    """ Faz uma contagem de i: inicio
       ate f: fim com o passo para cada
       numero p:passo """
    cont = i
    while cont < f+1:
        print(cont)
        cont += p


help(contador)
contador(10, 25, 1)
