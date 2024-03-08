import sys

class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def is_operator(c):
    return c in ['+', '-', '*', '/']

def construct_tree(postfix):
    stack = []
    
    for char in postfix:
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
    
    return stack.pop()

def calculate(node):
    if node.value.isdigit():
        return int(node.value)
    
    left = calculate(node.left)
    right = calculate(node.right)
    
    if node.value == '+':
        return left + right
    elif node.value == '-':
        return left - right
    elif node.value == '*':
        return left * right
    elif node.value == '/':
        return left // right

def infix_to_postfix(expression):
    precedence = {'+':1, '-':1, '*':2, '/':2}
    stack = [] 
    postfix = [] 
    for char in expression:
        if char.isdigit():
            postfix.append(char)
        elif char == '(':
            stack.append(char)
        elif char == ')':
            while stack and stack[-1] != '(':
                postfix.append(stack.pop())
            stack.pop() 
        else:
            while stack and precedence.get(char, 0) <= precedence.get(stack[-1], 0):
                postfix.append(stack.pop())
            stack.append(char)
    while stack:
        postfix.append(stack.pop())
    return postfix

def main():
    
    expression = sys.argv[1]
    expression = expression.replace(" ", "") 
    postfix = infix_to_postfix(expression)
    tree = construct_tree(postfix)
    result = calculate(tree)
    print(result)

if __name__ == "__main__":
    main()
