
class Environment:
    '''Environment to store variables'''

    def __init__(self, preinstalled = dict()) -> None:
        self.record = preinstalled

    def define(self, name: str, value):
        '''Defines a new variable with passed name and value'''
        self.record[name] = value
        return self.record[name]

    def lookup(self, name: str):
        '''Look up defined variable value'''
        if name not in self.record.keys():
            raise Exception(f"Undefined variable: {name}")
        return self.record[name]
