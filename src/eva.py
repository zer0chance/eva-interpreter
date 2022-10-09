import numbers

from src.environment import Environment
from src.transformer import Transformer

def isNumber(expr) -> bool:
    return isinstance(expr, numbers.Number)

def isString(expr) -> bool:
    return isinstance(expr, str) and expr[0] == '"' and expr[-1] == '"'

def isNewVariable(expr) -> bool:
    return expr[0] == 'var'

def isSetInstruction(expr) -> bool:
    return expr[0] == 'set'

def isVariableName(expr) -> bool:
    return isinstance(expr, str) # TODO: add regex to validate variable name

def isNewBlock(expr) -> bool:
    return expr[0] == 'begin'

def isIfStatement(expr) -> bool:
    return expr[0] == 'if'

def isSwitchStatement(expr) -> bool:
    return expr[0] == 'switch'

def isWhileLoop(expr) -> bool:
    return expr[0] == 'while'

def isForLoop(expr) -> bool:
    return expr[0] == 'for'

def isFunctionDeclaration(expr) -> bool:
    return expr[0] == 'def'

def isLambdaDeclaration(expr) -> bool:
    return expr[0] == 'lambda'

def isFunctionCall(expr) -> bool:
    return isinstance(expr, list)

def isClassDeclaration(expr) -> bool:
    return expr[0] == 'class'

def isSuperOperator(expr) -> bool:
    return expr[0] == 'super'

def isNewOperator(expr) -> bool:
    return expr[0] == 'new'

def isPropertyAccess(expr) -> bool:
    return expr[0] == 'prop'

class ExecutionStack:
    '''Stack that holds references to the activation
       records of currently active functions'''

    def __init__(self, globalEnv: Environment):
        # Frame is a list of [<function_name>, <env_id>] entries.
        self.stack = [['main', id(globalEnv)]]

    def pushFrame(self, frame):
        self.stack.append(frame)

    def popFrame(self):
        self.stack.pop()

    def printStackTrace(self):
        print('\n :::Stack Trace:::')
        for number, frame in enumerate(self.stack):
            print(f'-- {number}. {frame[0]} from Ox{frame[1]:x} environment')

class Eva:
    '''Eva language interpreter'''

    # Global preinstalls
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
        '=': lambda x, y: x == y,

        # Builtin functions
        'print': lambda x: print(x)
    })

    def __init__(self) -> None:
        self.execStack = ExecutionStack(self.globalEnv)
        self.transformer = Transformer()
        self.traceCallStack = False # TODO: pass by command line

    def pushFrame(self, func_name: str, env: Environment):
        self.execStack.pushFrame([func_name, id(env)])

    def popFrame(self):
        self.execStack.popFrame()

    def printStack(self):
        self.execStack.printStackTrace()

    def evalGlobal(self, expr):
        '''Evaluate expressions wrapping it into block'''
        return self.eval(['begin', expr])

    def eval(self, expr, env = globalEnv):
        if isNumber(expr):
            return expr

        if isString(expr):
            # Return string value in double quotes
            return expr[1:-1]

        if isClassDeclaration(expr):
            name, parent, body = expr[1:]

            # A class is just an environment that store methods
            # and shared properties

            parentEnv = self.eval(parent, env) or env
            classEnv = Environment({}, parentEnv)
            self.__evalBody(body, classEnv)

            return env.define(name, classEnv)

        if isPropertyAccess(expr):
            instance, name = expr[1:]
            
            instanceEnv = self.eval(instance, env)
            return instanceEnv.lookup(name)

        if isSuperOperator(expr):
            className = expr[1]
            return self.eval(className, env).parent

        if isNewOperator(expr):
            classEnv = self.eval(expr[1], env)
            # Parent component of instance environment is set to it's class

            instanceEnv = Environment({}, classEnv)
            constructorArgs = [instanceEnv] + [self.eval(arg, env) for arg in expr[2:]]
            self.__callUserDefinedFunction(classEnv.lookup('constructor'), constructorArgs, expr, classEnv)

            return instanceEnv

        if isNewVariable(expr):
            return env.define(expr[1], self.eval(expr[2], env))

        if isSetInstruction(expr):
            ref, value = expr[1:]

            if (ref[0] == 'prop'):
                instance, propName = ref[1:]
                return self.eval(instance, env).define(propName, self.eval(value, env))

            return env.assign(expr[1], self.eval(expr[2], env))

        if isNewBlock(expr):
            blockEnv = Environment(dict(), env)
            return self.__evalBlock(expr[1:], blockEnv)
        
        if isVariableName(expr):
            return env.lookup(expr)

        if isIfStatement(expr):
            ifBlockEnv = Environment(dict(), env)

            # if statement: if <cond> <consequent> <alternate>
            if (self.eval(expr[1], ifBlockEnv)):
                return self.eval(expr[2], ifBlockEnv)
            else:
                return self.eval(expr[3], ifBlockEnv)
        
        if isSwitchStatement(expr):
            switchBlockEnv = Environment(dict(), env)

            ifExpr = self.transformer.transformSwitchToIf(expr)
            return self.__evalBody(ifExpr, switchBlockEnv)

        if isWhileLoop(expr):
            whileBlockEnv = Environment(dict(), env)
            result = None

            # while loop: while <cond> <action>
            while (self.eval(expr[1], whileBlockEnv)):
                result = self.__evalBody(expr[2], whileBlockEnv)
            return result

        if isForLoop(expr):
            # TODO
            raise Exception(f"Unimplemented expression: {expr}")
            # forBlockEnv = Environment(dict(), env)
            # whileExpr = self.transformer.transformForToWhileLoop(expr)

            # return self.eval(whileExpr, forBlockEnv)

        # Functions
        if isFunctionDeclaration(expr):
            varExpr = self.transformer.transformDefToVarLambda(expr)
            return self.eval(varExpr, env)

        if isLambdaDeclaration(expr):
            # Directly return the function without installing it to the environment
            params, body = expr[1:]
            return {
                'params': params,
                'body'  : body,
                'env'   : env
            }

        if isFunctionCall(expr):
            if self.traceCallStack:
                self.printStack()

            fn = self.eval(expr[0], env)
            args = [self.eval(arg, env) for arg in expr[1:]]

            # Native functions
            if callable(fn):
                self.pushFrame(expr[0], env)
                result = fn(*args)
                self.popFrame()
                return result

            # User-defined functions
            return self.__callUserDefinedFunction(fn, args, expr, env)


        raise Exception(f"Unimplemented expression: {expr}")

    def __evalBlock(self, block, blockEnv):
        result = None
        for e in block:
            result = self.eval(e, blockEnv)
        return result

    def __evalBody(self, body, env):
        if body[0] == 'begin':
            return self.__evalBlock(body[1:], env)
        return self.eval(body, env)

    def __callUserDefinedFunction(self, fn, args, expr, env):
        if len(fn['params']) != len(args):
            raise Exception(f"Parametrs mismatch: {expr}")

        # activationRecord = {param: value for param in fn['params'] for value in args}
        activationRecord = dict(zip(fn['params'], args))
        activationEnv = Environment(activationRecord, fn['env'])

        self.pushFrame(expr[0], env)
        result = self.__evalBody(fn['body'], activationEnv)
        self.popFrame()
        return result
