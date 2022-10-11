
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
        
    def transformForToWhileLoop(self, forExp):
        '''JIT-transpile for loop statement to while loop'''
        # For loop syntax:
        #   (for <init> <cond> <modifier> <expr>)
        # While loop:
        #   (begin <init> while <cond> (begin <expr> <modifier>))

        init, cond, modifier, expr = forExp[1:]
        whileExp = ['begin', 
                        init, 
                        ['while', cond, 
                            ['begin', expr, modifier]
                        ]
                    ]

        return whileExp
    
    def transformIncToSet(self, incExp):
        '''JIT-transpile inc to set expression'''
        # Inc:
        #   (inc <var>)
        # Set:
        #   (set <var> (+ <var> 1))

        varName = incExp[1]
        return ['set', varName, ['+', varName, 1]]
    
    def transformDecToSet(self, incExp):
        '''JIT-transpile inc to set expression'''
        # Dec:
        #   (dec <var>)
        # Set:
        #   (set <var> (- <var> 1))

        varName = incExp[1]
        return ['set', varName, ['-', varName, 1]]
