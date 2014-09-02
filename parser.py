# Implementación de un parser
# Reconoce expresiones mediante la gramática:
# EXP -> EXP op EXP | EXP -> (EXP) | cte
# la cual fué modificada para eliminar ambigüedad a:
# EXP  -> cte EXP1
# EXP1 -> (EXP) EXP1 | op EXP EXP1 | vacío
#
# Autor: Dr. Santiago Conant, Agosto 2014

import sys

# Empata y obtiene el siguiente token
def match(tokenEsperado):
    global token
    if token == tokenEsperado:
        token = sys.stdin.read(1) # token = caracter
        sys.stdout.write(token)
    else:
        print "Error: se esperaba " + tokenEsperado
        sys.exit(1)

# Función principal: implementa el análisis sintáctico
def parser():
    global token 
    token = sys.stdin.read(1) # inicializa con el primer token
    sys.stdout.write(token)
    exp()
    if token == '\n':
        print "Expresión bien construida"
    else:
        print "\nExpresión mal construida"

# Módulo que reconoce expresiones
def exp():
    global token
    if token == '0':
        match(token) # reconoce Constantes
        exp1()
    elif token == '(':
        match(token) # reconoce Delimitador (
        exp()
    else:
        print "\nError: se esperaba CTE o ("
        sys.exit(1)

# Módulo auxiliar para reconocimiento de expresiones
def exp1():
    global token
    if token == '+':
        match(token) # reconoce operador
        exp()
        exp1()
    
        
