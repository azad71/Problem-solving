

def findPrecedence(operator):
    if operator == '+' or operator == '-':
        return 1
    elif operator == '*' or operator == '/':
        return 2
    else:
        return -1


def calculateResult(a, b, op):
    if op == '+':
        return a + b
    elif op == '-':
        return b - a
    elif op == '*':
        return a * b
    elif op == '/':
        return b / a


def infixEvaluation(exp):
    operators = []
    operands = []
    i = 0
    while i < len(exp):
        token = exp[i]
        if token == ' ':
            i += 1
            continue

        if token.isdigit():
            num = 0
            while token.isdigit() and i < len(exp):
                num = num * 10 + int(token)
                i += 1
                if i < len(exp):
                    token = exp[i]
                else:
                    break
            i -= 1
            operands.append(num)
        elif token == '(':
            operators.append(token)
        elif token == ')':
            while operators[-1] != '(':
                value1 = operands.pop()
                value2 = operands.pop()
                op = operators.pop()
                operands.append(calculateResult(value1, value2, op))
            operators.pop()
        else:
            while len(operators) > 0 and (findPrecedence(token) <= findPrecedence(operators[-1])):
                value1 = operands.pop()
                value2 = operands.pop()
                op = operators.pop()
                operands.append(calculateResult(value1, value2, op))
            operators.append(token)
        i += 1
    while len(operators) > 0:
        value1 = operands.pop()
        value2 = operands.pop()
        op = operators.pop()
        operands.append(calculateResult(value1, value2, op))

    result = operands.pop()

    return int(result) if float(result).is_integer() else round(result, 2)


print(infixEvaluation('5 / ( 5 * ( 2 + 1 ) ) * 2 - 10'))
print(infixEvaluation('2 * ( 5 * ( 3 + 6 ) ) / 15 - 2'))  # 4
print(infixEvaluation("1 + 3 + ( ( 4 / 2 ) * ( 8 * 4 ) )"))  # 68
print(infixEvaluation('55+10'))


"""
Infix evaluation algorithm for future me

1. Keep two stacks, operands and operators
2. Parse given expression from left to right
3. If parsing token is number, push it to operands array. 
  There's a catch, if the number is more than one digit, 
  have to loop through untill whole number is collected
4. If token is '(', push it to operators
5. If token is ')'
  5.1. Pop two operands and one operator
  5.2. Calculate the result and push the result into operands
  5.3. Keep repeating untill a closing '(' found
6. If token is any of '+', '-', '*', '/'
  6.1. If current operator precedence is lower than top operator in operators stack
    6.1.a. Pop two operands
    6.1.b. Calculate the result with current operator and push the result into operands
    6.1.c. Keep repeating it untill higher precedence operator is found in stack or operators stack is empty
  6.2. Just push the token into operators stack
7. If operators and operands stack is still not empty,
  7.1. Pop two operands and one operator
  7.2. Push the result to operands stack
  7.3. Keep repeating it untill both stack is empty

"""
