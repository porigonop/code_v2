# Yacc example

import ply.yacc as yacc
import ast
import pretty_print
import interpreter


# Get the token map from the lexer.  This is required.
from lexer import Lexer
tokens = Lexer.tokens
precedence = (
        ('left', 'ASSIGN'),
        ('left', 'PLUS', 'MINUS'),
        ('left', 'TIMES', 'DIVIDE')
        )

def p_expression(p):
    '''
    expression : assignment
               | operation
    '''
    p[0] = p[1]

def p_operation(p):
    '''
    operation : expression PLUS expression
              | expression MINUS expression
              | expression TIMES expression
              | expression DIVIDE expression
              | LPAREN expression RPAREN
    '''
    if p[1] == '(':
        # LPAREN expression RPAREN
        p[0] = p[2]
    else:
        p[0] = ast.Operation(p[1], p[3], ast.Operator(p[2]))
def p_expression_value(p):
    '''expression : NUMBER'''
    p[0] = ast.Element(p[1])
def p_expression_identifier(p):
    '''expression : ID'''
    p[0] = ast.Identifier(p[1])

def p_assignment(p):
    '''
    assignment : ID ASSIGN expression
    '''
    p[0] = ast.Assignment(ast.Identifier(p[1]), p[3])

# Error rule for syntax errors
def p_error(p):
    print("Syntax error in input!")

# Build the parser
parser = yacc.yacc()
lexer = Lexer()
lexer.build()
interpretor = interpreter.Interpreter()
while True:
   try:
       s = input('calc > ')
   except EOFError:
       print()
       break
   if not s: continue
   result = parser.parse(s, lexer=lexer.lexer)
   result.accept(pretty_print.PrettyPrint())
   result.accept(interpretor)
   print()
   print('=', end=' ')
   interpretor.print_result()
