# Jose Alberto Esquivel A01139626
# Eduardo Sanchez A01195815
# Implementacion de un parser
# Reconoce expresiones mediante la gramatica:
# EXP -> EXP op EXP | EXP -> (EXP) | cte
# la cual fue modificada para eliminar ambiguedad a:
# EXP  -> cte EXP1
# EXP1 -> (EXP) EXP1 | op EXP EXP1 | vacio
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

# Funcion principal: implementa el analisis sintactico
def parser():
    global token
    token = sys.stdin.read(1) # inicializa con el primer token
    sys.stdout.write(token)
    exp()
    if token == '\n':
        print "Expresion bien construida"
    else:
        print "\nExpresion mal construida"

# Modulo que reconoce expresiones
def exp():
    global token
    if token == '0':
        match(token) # reconoce Constantes
        exp1()
    elif token == '(':
        match(token) # reconoce Delimitador (
        exp()
        if token == ')':
            match(token)
            exp1()
        else:
            print "\nError: se esperaba )"
            sys.exit(1)
    else:
        func()
        exp1()

# Modulo auxiliar para reconocimiento de expresiones
def exp1():
    global token
    if token == '+':
        match(token) # reconoce operador
        exp()
        exp1()

def func():
    global token
    if token == 'F':
        match(token)
        if token == '(':
            match(token)
            A()
        else:
            print "\nError: se esperaba ("
            sys.exit(1)
    else:
        print "\nError: se esperaba F"
        sys.exit(1)

def A():
    exp()
    B()

def B():
    if token == ',':
        match(token)
        A()
    elif token == ')':
        match(token)
    else:
        print "\nError: se esperaba , o )"
        sys.exit(1)

parser()
