#! python3

import argparse

from parser import evaparser
from src.eva import Eva

def evalGlobal(eva: Eva, code: str):
    expr = evaparser.parse(f'(begin {code})')
    return eva.evalGlobal(expr)

argparser = argparse.ArgumentParser(description='=====DAVY JONES=====')
argparser.add_argument('-e', '--evaluate-expression',
                        dest='expr',
                        action='store',
                        type=str,
                        help='evaluate passed expression')
argparser.add_argument('-f', '--file',
                        dest='file',
                        action='store',
                        type=str,
                        help='execute program from file')

if __name__ == '__main__':
    args = argparser.parse_args()

    eva = Eva()
    if args.expr:
        evalGlobal(eva, args.expr)
    if args.file:
        with open(args.file, 'r') as srcFile:
            moduleSrc = srcFile.read()
        evalGlobal(eva, moduleSrc)
