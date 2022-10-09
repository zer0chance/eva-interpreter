from parser import evaparser
from src.eva import Eva

class Run:
    @staticmethod
    def SExpression(eva: Eva, code: str):
        expr = evaparser.parse(code)
        return eva.eval(expr)
