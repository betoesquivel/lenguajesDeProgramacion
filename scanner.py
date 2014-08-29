# Implementacion de un scanner mediante la codificacion de un Automata
# Finito Determinista como una Matriz de Transiciones
# Autor: Dr. Santiago Conant, Agosto 2014

import sys

# Matriz de transiciones: codificacion del AFD
# [renglon, columna] = [estado, transicion]
# Estados > 99 son finales (ACEPTORES)
# Caso especial: Estado 200 = ERROR
#      dig   op   (    )  raro  esp  .   $   A-Z   _
MT = [[  1, 102, 105, 106,   4,   0, 4, 107,   5,   4], # edo 0 - estado inicial
      [  1, 100, 100, 100, 100, 100, 2, 100,   4,   4], # edo 1 - digitos enteros
      [  3, 200, 200, 200,   4, 200, 4, 200,   4,   4], # edo 2 - primer decimal flotante
      [  3, 101, 101, 101, 101, 101, 4, 101,   4,   4], # edo 3 - decimales restantes flotante
      [200, 200, 200, 200,   4, 200, 4, 200, 200,   4], # edo 4 - estado de error
      [  5, 108, 108, 108,   4, 108, 4,   4,   5,   5]] # edo 5 - identificadores con A-Z o _

# Filtro de caracteres: regresa el numero de columna de la matriz de transiciones
# de acuerdo al caracter dado
def filtro(c):
    """Regresa el numero de columna asociado al tipo de caracter dado(c)"""
    if c == '0' or c == '1' or c == '2' or \
       c == '3' or c == '4' or c == '5' or \
       c == '6' or c == '7' or c == '8' or c == '9': # digitos
        return 0
    elif c == '+' or c == '-' or c == '*' or \
         c == '/': # operadores
        return 1
    elif c == '(': # delimitador (
        return 2
    elif c == ')': # delimitador )
        return 3
    elif c == ' ' or ord(c) == 10 or ord(c) == 13: # blancos
        return 5
    elif c == '.': # punto
        return 6
    elif c == '$': # fin de entrada
        return 7
    elif c == 'A' or c == 'B' or c == 'C' or c == 'D' or \
         c == 'E' or c == 'F' or c == 'G' or c == 'H' or \
         c == 'I' or c == 'J' or c == 'K' or c == 'L' or \
         c == 'M' or c == 'N' or c == 'O' or c == 'P' or \
         c == 'Q' or c == 'R' or c == 'S' or c == 'T' or \
         c == 'U' or c == 'V' or c == 'W' or c == 'X' or \
         c == 'Y' or c == 'Z':
        return 8
	elif c == '_':
		return 9
    else: # caracter raro
        return 4

# Funcion principal: implementa el analisis lexico
def scanner():
    """Implementa un analizador lexico: lee los caracteres de la entrada estandar"""
    edo = 0 # numero de estado en el automata
    lexema = ""
    leer = True # indica si se requiere leer un caracter de la entrada estandar
    while (True):
        while edo < 100:    # mientras el estado no sea ACEPTOR ni ERROR
            if leer: c = sys.stdin.read(1)
            else: leer = True
            edo = MT[edo][filtro(c)]
            if edo != 0: lexema += c
        if edo == 100:      # Token 100
            lexema = lexema[:-1] # elimina el delimitador
            leer = False
            print "Entero " + lexema
        elif edo == 101:    # Token 101
            lexema = lexema[:-1] # elimina el delimitador
            leer = False
            print "Flotante " + lexema
        elif edo == 102:    # Token 102
            print "Operador " + lexema
        elif edo == 105:    # Token 105
            print "Delimitador " + lexema
        elif edo == 106:    # Token 106
            print "Delimitador " + lexema
        elif edo == 107:    # Termina analisis
            return 0
        elif edo == 108:
            lexema = lexema[:-1] # elimina el delimitador
            leer = False
            print "Identificador " + lexema
        elif edo == 200:    # ERROR
            lexema = lexema[:-1] # el ultimo caracter no es raro
            leer = False
            print "ERROR! palabra ilegal " + lexema
        lexema = ""
        edo = 0


scanner()

