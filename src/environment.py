
class Environment:
    '''Environment to store variables'''

    def __init__(self, preinstalled = dict(), parent = None) -> None:
        self.parent = parent
        self.record = preinstalled

    def define(self, name: str, value):
        '''Defines a new variable with passed name and value'''
        self.record[name] = value
        return self.record[name]

    def assign(self, name: str, value):
        '''Assigns a new value to the defined variable'''
        if name not in self.record.keys():
            if self.parent != None:
                return self.parent.assign(name, value)
            raise Exception(f"Undefined variable: {name}")
        
        self.record[name] = value
        return self.record[name]

    def lookup(self, name: str):
        '''Look up defined variable value'''
        if name not in self.record.keys():
            if self.parent != None:
                return self.parent.lookup(name)
            raise Exception(f"Undefined variable: {name}")
        return self.record[name]
