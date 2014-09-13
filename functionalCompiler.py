from functionalScanner import scanner
from functionalParser import parser

import sys

tokens = scanner()
parser(tokens)
