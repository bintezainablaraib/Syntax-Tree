import ast

def SyntaxTree(value):
    syntax = ast.parse(value, mode='eval')
    print(ast.dump(syntax))
    return ast.parse

value = input("Enter any expression i.e a+(b*c): ")
ast.parse = SyntaxTree(value)
print(ast.parse)
