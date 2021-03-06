# Jose Alberto Esquivel A01139626
# Eduardo Sanchez A01195815
# Implementacion de un parser

#EBNF: Gramatica simplificada
#<prog> ::= <exp> <prog> | $
#<exp> ::= simbolo | numero | booleano | string | <lista>
#<lista> ::= ( <elemento> )
#<elemento> ::= <exp> <elemento> | vacio
#

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
        print ">ERROR SINTACTICO<"
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
        print ">ENTRADA CORRECTA<"
    else:
        print ">ERROR SINTACTICO<"
        print tokenList

def prog():
    global token
    print "[PROG]"
    if token != eof:
        exp()
        prog()
    else:
        match(eof)

def exp():
    global token
    print "[EXP]"
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
    print "[LISTA]"
    if token == parIzq:
        match(parIzq)
        elemento()
        if token == parDer:
            match(parDer)
        else:
            print (">ERROR SINTACTICO<")
            sys.exit()
    else:
        print (">ERROR SINTACTICO<")
        sys.exit()

def elemento():
    global token
    print "[ELEMENTO]"
    if (token == parenIzq or\
        token == simbolo or \
        token == numero or \
        token == booleano or \
        token == string):
        exp()
        elemento()
