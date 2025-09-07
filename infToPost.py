from .rules import isOperator, precedence, associativity

def infToPost(exp):
    n = len(exp)
    stack = ""
    postExp = ""
    for i, c in enumerate(exp):
        if(c.isalpha()):
            postExp += c
            continue

        if(c == '('):
            stack += c
            continue

        if(c == ')'):
            while stack[-1] != '(':
                postExp += stack[-1]
                stack = stack[:-1]
            
            stack = stack[:-1]
            continue
        
        if(isOperator(c)):
            while(stack != "" and ((precedence[stack[-1]] > precedence[c]) or (stack[-1] == c and associativity[c] == "left"))):
                postExp += stack[-1]
                stack = stack[:-1]
            
            stack += c
            continue

        raise Exception("Some thing went wrong! your expression might be invalid")

    while stack != "":
        postExp += stack[-1]
        stack = stack[:-1]
    
    return postExp


            
        


