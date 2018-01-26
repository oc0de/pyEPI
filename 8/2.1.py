def evaluate(exp):
    s = []
    DELIMITER = ','
    OPERATORS = {
        '+': lambda y, x: x + y,
        '-': lambda y, x: x - y,
        '*': lambda y, x: x * y,
        '/': lambda y, x: int(x / y)
    }

    for token in reversed(exp.split(DELIMITER)):
        if token in OPERATORS: s.append(OPERATORS[token](s.pop(), s.pop()))
        else: s.append(int(token.trim()))

    return s[-1]


assert 10 == evaluate('+, 2, 8')
assert 4 == evaluate('/, 2, 8')
assert 0 == evaluate('-,4,/,2,8')
