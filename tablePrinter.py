from .infToPost import infToPost
from .logicResultGenerator import generate

def printTable(exp):
    try:
        postExp = infToPost(exp)
        result, vars = generate(postExp)
    except Exception as e:
        raise Exception("Something went wrong! your expression might be invalid")

    numOfVars = len(vars)

    print('_'*(numOfVars*3 + len(exp) + 2))

    print("|", end="")
    for c in vars:
        print(c, end="| ")
    print(exp, end="|\n")
    print('-'*(numOfVars*3 + len(exp) + 2))


    for i in range(2**numOfVars):
        print("|", end="")
        for j in range(numOfVars-1, -1, -1):
            if i>>j & 1 == 0:
                print("T", end="| ")
            else:
                print("F", end="| ")
        if result[i]:
            print('T', end=(" "*(len(exp)-1)) + "|\n")
        else:
            print("F", end=(" "*(len(exp)-1)) + "|\n")
    print('-'*(numOfVars*3 + len(exp) + 2))
        
