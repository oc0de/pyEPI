def generate_balanced_parentheses(n):
    def helper(left, right, valid_prefix, result=[]):
        if left > 0:
            helper(left - 1, right, valid_prefix + '(', result)

        if left < right:
            helper(left, right - 1, valid_prefix + ')', result)

        if not right:
            result += valid_prefix,

        return result

    return helper(n, n, '')


assert generate_balanced_parentheses(1) == ['()']
result = generate_balanced_parentheses(2)
assert result == ['(())', '()()'] or result == ['()()', '(())']
