from .postfixEval import evalLogic

def generate(exp):
    s = set()

    for c in exp:
        if c.isalpha():
            s.add(c)
    
    vars = sorted(s)
    n = len(vars)
    result = []

    for i in range(2**n):
        values = getValues(vars, i)
        result.append(evalLogic(exp, values))
    

    return result, vars

def getValues(vars, i):
    n = len(vars)
    values = []

    for it in range(n):
        if i>>it & 1 == 0:
            values = [True] + values
        else:
            values = [False] + values 

    return dict(zip(vars, values))

