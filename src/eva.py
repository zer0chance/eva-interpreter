from cmath import exp
import numbers

from src.environment import Environment

def isNumber(expr) -> bool:
    return isinstance(expr, numbers.Number)

def isString(expr) -> bool:
    return isinstance(expr, str) and expr[0] == '"' and expr[-1] == '"'

def isNewVariable(expr) -> bool:
    return expr[0] == 'var'

def isSetVariable(expr) -> bool:
    return expr[0] == 'set'

def isVariableName(expr) -> bool:
    return isinstance(expr, str) # TODO: add regex to validate variable name

def isNewBlock(expr) -> bool:
    return expr[0] == 'begin'

def isIfStatement(expr) -> bool:
    return expr[0] == 'if'

def isWhileLoop(expr) -> bool:
    return expr[0] == 'while'

def isFunctionCall(expr) -> bool:
    return isinstance(expr, list)

class Eva:
    '''Eva language interpreter'''

    # Global preinstalled variables
    globalEnv = Environment({
        'null': None,
        'true': True,
        'false': False,
        'EVA_VERSION': 0.1,
        
        # Math operators:
        '+': lambda x, y: x + y,
        '-': lambda x, y: x - y,
        '*': lambda x, y: x * y,
        '/': lambda x, y: x / y,
        '%': lambda x, y: x % y,

        # Comparison operators
        '<' : lambda x, y: x < y,
        '<=': lambda x, y: x <= y,
        '>' : lambda x, y: x > y,
        '>=': lambda x, y: x >= y,
        '==': lambda x, y: x == y,

        # Builtin functions
        'print': lambda x: print(x)
    })

    def __init__(self) -> None:
        pass

    def eval(self, expr, env = globalEnv):
        if isNumber(expr):
            return expr

        if isString(expr):
            # Return string value in double quotes
            return expr[1:-1]

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

        if isIfStatement(expr):
            ifBlockEnv = Environment(dict(), env)

            # if statement: if <cond> <consequent> <alternate>
            if (self.eval(expr[1], ifBlockEnv)):
                return self.eval(expr[2], ifBlockEnv)
            else:
                return self.eval(expr[3], ifBlockEnv)

        if isWhileLoop(expr):
            whileBlockEnv = Environment(dict(), env)
            result = None

            # while loop: while <cond> <action>
            while (self.eval(expr[1], whileBlockEnv)):
                result = self.eval(expr[2], whileBlockEnv)
            return result
        
        # Functions
        if isFunctionCall(expr):
            fn = self.eval(expr[0], env)
            args = [self.eval(arg, env) for arg in expr[1:]]
            if callable(fn):
                return fn(*args)
            
            raise Exception(f"Undefined function: {expr}")

        raise Exception(f"Unimplemented expression: {expr}")


if __name__ == '__main__':
    eva = Eva()
