def evaluate(RPN_expression):
    s = []
    DELIMITER = ','
    OPERATORS = {
        '+': lambda y, x: x + y,
        '-': lambda y, x: x - y,
        '*': lambda y, x: x * y,
        '/': lambda y, x: int(x / y)
    }

    for token in RPN_expression.split(DELIMITER):
        if token in OPERATORS: s.append(OPERATORS[token](s.pop(), s.pop()))
        else: s.append(int(token))
    
    return s[-1]


assert -1 == evaluate('2,-10,/')
assert -5 == evaluate('-10,2,/')
assert 5 == evaluate('-10,-2,/')
assert -5 == evaluate('5,10,-')
assert 6 == evaluate('-10,-16,-')
assert 12 == evaluate('10,2,+')
assert 15 == evaluate('1,2,+,3,4,*,+')
