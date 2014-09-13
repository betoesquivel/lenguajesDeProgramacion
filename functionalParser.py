# Jose Alberto Esquivel A01139626
# Eduardo Sanchez A01195815
# Implementacion de un parser
#EBNF: Gramatica simplificada
#<prog> ::= <exp> <prog> | $
#<exp> ::= simbolo | numero | booleano | string | <lista>
#<lista> ::= ( <elemento> )
#<elemento> ::= <exp> <elemento> | vacio
#
# P -> E $
# E -> simbolo E'
# E -> num E'
# E ->  bool E’
# E -> string
# E -> ( E ) E'
# E' -> E E'
# E' -> ø
# autor de gramatica: Gustavo Ferrufino
# Autor: Dr. Santiago Conant, Agosto 2014

import sys

parIzq = 100
parDer = 101
eof = 106
simbolo = 102
numero = 103
string = 104
booleano = 105
error = 200

# Empata y obtiene el siguiente token
def match(tokenEsperado):
    global token
    global tokenList
    if token == tokenEsperado:
        if(tokenList):
            tokenList.pop(0)
            if(tokenList):
                token = tokenList[0] # token = caracter
    else:
        print "Error: se esperaba " + tokenEsperado
        sys.exit(1)

# Funcion principal: implementa el analisis sintactico
def parser(listOfTokens):
    global token
    global tokenList
    tokenList = listOfTokens
    print tokenList
    token = tokenList[0] # inicializa con el primer token
    prog()
    if not tokenList or tokenList[0] == eof:
        print "Expresion bien construida"
    else:
        print "\nExpresion mal construida"
        print tokenList

def prog():
    global token
    if token != eof:
        exp()
        prog()
    else:
        match(eof)

def exp():
    global token
    if token == simbolo:
        match(simbolo)
    elif token == numero:
        match(numero)
    elif token == booleano:
        match(booleano)
    elif token == string:
        match(string)
    else:
        lista()

def lista():
    global token
    if token == parIzq:
        match(parIzq)
        elemento()
        if token == parDer:
            match(parDer)
        else:
            print ("Error: Se esperaba parentesis derecho")
            sys.exit()
    else:
        print ("Error: Se esperaba parentesis izquierdo o un atomo")
        sys.exit()

def elemento():
    global token
    if (token == parenIzq or\
        token == simbolo or \
        token == numero or \
        token == booleano or \
        token == string):
        exp()
        elemento()
