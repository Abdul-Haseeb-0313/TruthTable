

precedence = {
    '~': 5,
    '.': 4,
    '+': 3,
    '-': 2,
    '=': 1,
    '(': -1

}

associativity = {
    '~': "right",
    '.': "left",
    '+': "left",
    '-': "right",
    '=': "left"
}

def isOperator(c):
    return c in ['.', '+', '-', '=', '~']

