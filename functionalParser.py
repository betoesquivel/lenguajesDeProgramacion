# Jose Alberto Esquivel A01139626
# Eduardo Sanchez A01195815
# Implementacion de un parser
#EBNF: Gramatica simplificada
#<prog> ::= <exp> <prog> | $
#<exp> ::= simbolo | numero | booleano | string | <lista>
#<lista> ::= ( <elemento> )
#<elemento> ::= <exp> <elemento> | vacio
#
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
    token = tokenList[0] # inicializa con el primer token
    prog()
    if not tokenList or tokenList(0) == eof:
        print "Expresion bien construida"
    else:
        print "\nExpresion mal construida"

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
    elif token == parIzq:
        lista()

def lista():
    global token
    if token == parIzq:
        match(parIzq)
        elemento()
        match(parDer)
    else:
        print ("Error: Se esperaba parentesis izquierdo")

def elemento():
    global token
    global tokenList

    if not tokenList:
        print ("Legal")
        sys.exit()
    else:
        exp()
        elemento()
