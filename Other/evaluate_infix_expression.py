def isOperator(ch: str) -> int:
    return ch == '+' or ch == '-' or ch == '*' or ch == '/'

def performOperation(operand, operator):
    a = operand.pop()
    b = operand.pop()
    op = operator.pop()
    if op == '+':
        return a + b
    if op == '-':
        return b - a
    if op == '*':
        return a * b
    if op == '/':
        return b // a

def precendance(ch):
    if ch == '*' or ch == '/':
        return 2
    if ch == '+' or ch == '-':
        return 1
    return 0

def evaluate(s: str) -> int:
    operand = []
    operator = []
    i = 0
    while i < len(s):
        ch = s[i]
        if ch.isdigit():
            num = 0
            while ch.isdigit():
                num = (num * 10) + int(ch)
                i += 1
                if i < len(s):
                    ch = s[i]
                else:
                    break
            i -= 1
            operand.append(num)
        elif ch == '(':
            operator.append(ch)
        elif ch == ')':
            while operator[-1] != '(':
                result = performOperation(operand, operator)
                operand.append(result)
            operator.pop()
        elif isOperator(ch):
            while len(operator) != 0 and precendance(ch) <= precendance(operator[-1]):
                result = performOperation(operand, operator)
                operand.append(result)
            operator.append(ch)
        i += 1

    while len(operator) != 0:
        result = performOperation(operand, operator)
        operand.append(result)
    return operand.pop()


print(evaluate("(1+(4+5+2)-3)+(6+8)"))
print(evaluate("3+2*2"))
print(evaluate(" 3/2 "))
print(evaluate(" 3+5 / 2 "))
print(evaluate("10 + 2 * 6"))
print(evaluate("100 * 2 + 12")) 
print(evaluate("100 * ( 2 + 12 )")) 
print(evaluate("100 * ( 2 + 12 ) / 14"))