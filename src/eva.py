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

def isSetVariable(expr) -> bool:
    return expr[0] == 'set'

def isVariableName(expr) -> bool:
    return isinstance(expr, str) # TODO: add regex to validate variable name

def isNewBlock(expr) -> bool:
    return expr[0] == 'begin'

def isLess(expr) -> bool:
    return expr[0] == '<'

def isLessEqual(expr) -> bool:
    return expr[0] == '<='

def isGreater(expr) -> bool:
    return expr[0] == '>'

def isGreaterEqual(expr) -> bool:
    return expr[0] == '>='

def isEqual(expr) -> bool:
    return expr[0] == '=='

def isIfStatement(expr):
    return expr[0] == 'if'

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

        if isString(expr):
            # Return string value in double quotes
            return expr[1:-1]

        # Math expressions
        if isAddition(expr):
            return self.eval(expr[1], env) + self.eval(expr[2], env)
        if isSubstraction(expr):
            return self.eval(expr[1], env) - self.eval(expr[2], env)
        if isMultiplication(expr):
            return self.eval(expr[1], env) * self.eval(expr[2], env)
        if isDivision(expr):
            return self.eval(expr[1], env) / self.eval(expr[2], env)
        if isModule(expr):
            return self.eval(expr[1], env) % self.eval(expr[2], env)

        if isNewVariable(expr):
            return env.define(expr[1], self.eval(expr[2], env))

        if isSetVariable(expr):
            return env.assign(expr[1], self.eval(expr[2], env))

        if isVariableName(expr):
            return env.lookup(expr)

        if isNewBlock(expr):
            blockEnv = Environment(dict(), env)
            result = None
            for e in expr[1:]:
                result = self.eval(e, blockEnv)
            return result

        if isLess(expr):
            return self.eval(expr[1], env) < self.eval(expr[2], env)

        if isLessEqual(expr):
            return self.eval(expr[1], env) <= self.eval(expr[2], env)

        if isGreater(expr):
            return self.eval(expr[1], env) > self.eval(expr[2], env)

        if isGreaterEqual(expr):
            return self.eval(expr[1], env) >= self.eval(expr[2], env)

        if isEqual(expr):
            return self.eval(expr[1], env) == self.eval(expr[2], env)

        if isIfStatement(expr):
            ifBlockEnv = Environment(dict(), env)

            # if statement: if <cond> <consequent> <alternate>
            if (self.eval(expr[1], ifBlockEnv)):
                return self.eval(expr[2], ifBlockEnv)
            else:
                return self.eval(expr[3], ifBlockEnv)

        raise Exception(f"Unimplemented expression: {expr}")


if __name__ == '__main__':
    eva = Eva()
