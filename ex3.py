import sys

class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def is_operator(c):
    return c in ['+', '-', '*', '/', '–']

def construct_tree(postfix):
    stack = []
    
    for char in postfix:

        if(char != '('):
            if not is_operator(char):
                node = Node(char)
                stack.append(node)
            else:
                node = Node(char)

                right = stack.pop()
                left = stack.pop()
                node.right = right
                node.left = left
                stack.append(node)
    
    return stack[-1]

def calculate(node):
    if node.value.isdigit():
        return int(node.value)
        
    left = calculate(node.left)
    right = calculate(node.right)
        
    print(left, right)

    if((left is not None) and (right is not None)):
        if node.value == '+':
            return left + right
        elif node.value == '-' or node.value == '–':
            return left - right
        elif node.value == '*':
            return left * right
        elif node.value == '/':
            return left // right


def infix_to_postfix(expression):
    precedence = {'+':1, '-':1,'–':1,'*':2, '/':2}
    stack = []
    postfix = []
    i = 0
    while i < len(expression):
        char = expression[i]
        if char.isdigit():
            num = [char]
            while i + 1 < len(expression) and expression[i+1].isdigit():
                i += 1
                num.append(expression[i])
            postfix.append(''.join(num))
        elif char == '(':
            stack.append(char)
        elif char == ')':
            while stack and stack[-1] != '(':
                postfix.append(stack.pop())
            if(len(stack) > 0):
                stack.pop()
        else:
            while stack and precedence.get(char, 0) <= precedence.get(stack[-1], 0):
                postfix.append(stack.pop())
            stack.append(char)
        i += 1
    
    while stack:
        postfix.append(stack.pop())
    return postfix
    
expression = sys.argv[1]
expression = expression.replace(" ", "") 
print(expression)
postfix = infix_to_postfix(expression)
print(postfix)
tree = construct_tree(postfix)
result = calculate(tree)
print(result)

