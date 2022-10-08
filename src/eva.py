from cmath import exp
import numbers

from src.environment import Environment

def isNumber(expr) -> bool:
    return isinstance(expr, numbers.Number)

def isString(expr) -> bool:
    return isinstance(expr, str) and expr[0] == '"' and expr[-1] == '"'

def isAddition(expr) -> bool:
    return expr[0] == '+'

def isSubstraction(expr) -> bool:
    return expr[0] == '-'

def isMultiplication(expr) -> bool:
    return expr[0] == '*'

def isDivision(expr) -> bool:
    return expr[0] == '/'

def isModule(expr) -> bool:
    return expr[0] == '%'

def isNewVariable(expr) -> bool:
    return expr[0] == 'var'

def isVariableName(expr) -> bool:
    return isinstance(expr, str) # TODO: add regex to validate variable name

class Eva:
    '''Eva language interpreter'''

    # Global preinstalled variables
    globalEnv = Environment({
        'null': None,
        'true': True,
        'false': False,
        'EVA_VERSION': 0.1
    })

    def __init__(self) -> None:
        pass

    def eval(self, expr, env = globalEnv):
        if isNumber(expr):
            return expr

        elif isString(expr):
            # Return string value in double quotes
            return expr[1:-1]

        # Math expressions
        elif isAddition(expr):
            return self.eval(expr[1]) + self.eval(expr[2])
        elif isSubstraction(expr):
            return self.eval(expr[1]) - self.eval(expr[2])
        elif isMultiplication(expr):
            return self.eval(expr[1]) * self.eval(expr[2])
        elif isDivision(expr):
            return self.eval(expr[1]) / self.eval(expr[2])
        elif isModule(expr):
            return self.eval(expr[1]) % self.eval(expr[2])

        if isNewVariable(expr):
            return env.define(expr[1], self.eval(expr[2]))

        if isVariableName(expr):
            return env.lookup(expr)

        raise Exception(f"Unimplemented expression: {expr}")


if __name__ == '__main__':
    eva = Eva()
