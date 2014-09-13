

# Implementacion de un scanner mediante la codificacion de un Automata
# Finito Determinista como una Matriz de Transiciones
# Autor: Jose Alberto Esquivel Patinio, Septiembre 2014
# Autor: Eduardo Sanchez

#EBNF: Gramatica simplificada
#<prog> ::= <exp> <prog> | $
#<exp> ::= simbolo | numero | booleano | string | <lista>
#<lista> ::= ( <elemento> )
#<elemento> ::= <exp> <elemento> | vacio

import sys

# Matriz de transiciones: codificacion del AFD
# [renglon, columna] = [estado, transicion]
# Estados > 99 son finales (ACEPTORES)
# Caso especial: Estado 200 = ERROR
#       0-9     a-z                                   \n        t | f
#       dig   letra      (       )    raro   esp   salto    #    bool     $       "       ;
MT = [[   2,      1,   100,    101,      6,    0,      0,   4,      1,  106,      3,      5], # edo 0    inicial
      [   6,      1,   102,    102,      6,  102,    102,   6,      1,  102,      6,    102], # edo 1    simbolo
      [   2,      6,   103,    103,      6,  103,    103,   6,      6,  103,      6,    103], # edo 2    numero
      [   3,      3,     6,      6,      6,    3,      6,   6,      3,    6,    104,      6], # edo 3    string
      [   6,      6,     6,      6,      6,    6,      6,   6,    105,    6,      6,      6], # edo 4    bool
      [   5,      5,     5,      5,      5,    5,    110,   5,      5,    5,      5,      5], # edo 5    comentario
      [ 200,    200,   200,    200,      6,  200,    200, 200,    200,  200,    200,    200]] # edo 6    error
# Filtro de caracteres: regresa el numero de columna de la matriz de transiciones
# de acuerdo al caracter dado
def filtro(c):
    """Regresa el numero de columna asociado al tipo de caracter dado(c)"""
    if c == '0' or c == '1' or c == '2' or \
       c == '3' or c == '4' or c == '5' or \
       c == '6' or c == '7' or c == '8' or c == '9': # digitos
        return 0
    elif c == 't' or c == 'f' : # booleano
        return 8
    elif c >= 'a' and c <= 'z': # letra que no es t ni f
        return 1
    elif c == '(': # delimitador (
        return 2
    elif c == ' ': # blancos
        return 5
    elif c == ')': # delimitador )
        return 3
    elif c == '$': # fin de entrada
        return 9
    elif ord(c) == 10 or ord(c) == 13: # salto de linea y carriage return
        return 6
    elif c == '#': # hashtag pre booleano
        return 7
    elif c == '"': # comillas para string constant
        return 10
    elif c == ';': # punto y coma para comentarios
        return 11
    else: # caracter raro
        return 4

# Funcion principal: implementa el analisis lexico
def scanner():
    """Implementa un analizador lexico: lee los caracteres de la entrada estandar"""
    edo = 0 # numero de estado en el automata
    lexema = ""
    leer = True # indica si se requiere leer un caracter de la entrada estandar
    lexemas = []
    while (True):
        while edo < 100:    # mientras el estado no sea ACEPTOR ni ERROR
            if leer: c = sys.stdin.read(1)
            else: leer = True
            edo = MT[edo][filtro(c)]
            if edo != 0: lexema += c
        if   edo == 100:      # Token 100
            #print '(' + lexema
            lexemas.append(100)
        elif edo == 101:    # Token 101
            #print ')' + lexema
            lexemas.append(101)
        elif edo == 102:    # Token 102
            lexema = lexema[:-1] # elimina el delimitador
            leer = False
            #print "<simbolo> " + lexema
            lexemas.append(102)
        elif edo == 103:    # Token 103
            lexema = lexema[:-1] # elimina el delimitador
            leer = False
            #print "<numero> " + lexema
            lexemas.append(103)
        elif edo == 104:    # Token 104
            #print "<string> " + lexema
            lexemas.append(104)
        elif edo == 105:    # Token 105
            #print "<boolean> " + lexema
            lexemas.append(105)
        elif edo == 106:    # Token 106
            return lexemas        # Termina analisis
        elif edo == 110:    # Token 110
            lexema = lexema[:-1] # elimina el delimitador
            leer = False
            #print "<comentario> " + lexema
            lexemas.append(110)
        elif edo == 200:    # ERROR
            lexema = lexema[:-1] # el ultimo caracter no es raro
            leer = False
            print "ERROR! palabra ilegal " + lexema
            return -1
        lexema = ""
        edo = 0


#print (scanner())

