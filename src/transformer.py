
class Transformer:
    '''AST Transformer'''

    def transformDefToVarLambda(self, defExp):
        '''JIT-transpile function definition to a variable declaration'''
        name, params, body = defExp[1:]
        return ['var', name, ['lambda', params, body]]

    def transformSwitchToIf(self, switchExp):
        '''JIT-transpile switch statement to if statement'''
        cases = switchExp[1:]

        ifExp = ['if', None, None, None]
        currentCase = ifExp

        for i in range(len(cases) - 1):
            currentCond, currentBlock = cases[i]
            currentCase[1] = currentCond
            currentCase[2] = currentBlock

            nextCase = cases[i + 1]
            nextCond, nextBlock = nextCase

            if nextCond == 'else':
                currentCase[3] = nextBlock
            else:
                currentCase[3] = ['if', None, None, None]
            
            currentCase = currentCase[3]

        return ifExp