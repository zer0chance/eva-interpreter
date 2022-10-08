import numbers

def isNumber(expr) -> bool:
    return isinstance(expr, numbers.Number)

def isString(expr) -> bool:
    return isinstance(expr, str) and expr[0] == '"' and expr[-1] == '"'

class Eva:
    def eval(self, expr):
        if isNumber(expr):
            return expr
        elif isString(expr):
            # Return string value in double quotes
            return expr[1:-1]

        raise "Unimplemented!"


if __name__ == '__main__':
    eva = Eva()
