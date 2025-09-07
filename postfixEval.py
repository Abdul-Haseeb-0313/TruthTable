from .rules import isOperator
from .infToPost import infToPost

def evalLogic(exp, values):
    stack = []

    for i, c in enumerate(exp):
        if(c.isalpha()):
            stack.append(values[c])
            continue 
        if(isOperator(c)):
            if(c == '~'):
                stack[-1] = not stack[-1]
            else:
                b = stack[-1]
                a = stack[-2]

                stack = stack[:-2]

                if(c == '+'):
                    stack.append(a or b)
                elif(c == '.'):
                    stack.append(a and b)
                elif(c == '-'):
                    stack.append((not a) or b)
                elif(c == '='):
                    stack.append(((not a) or b) and ((not b) or a))
    return stack[-1]

