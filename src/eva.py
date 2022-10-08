import numbers

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

class Eva:
    def eval(self, expr):
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

        raise "Unimplemented!"


if __name__ == '__main__':
    eva = Eva()
