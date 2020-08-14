from interpreter import Interpreter
from pretty_print import PrettyPrint
from ast import Operator, Operation, Element

class Token:
    operator = False
    empty = False
    def __init__(self, token):
        self.token = token
        if token == '+':
            self.operator = True
        elif token == '-':
            self.operator = True
        elif token == '*':
            self.operator = True
        elif token == '/':
            self.operator = True
        elif token == '':
            self.empty = True
        else:
            self.token = int(self.token)


class Lexer:
    def __init__(self, stream):
        self.stream = stream

    def get_token(self):
        next_space = self.stream.find(' ')
        if next_space == -1:
            token = Token(self.stream)
            self.stream = ''
            return token
        token = self.stream[:next_space]
        self.stream = self.stream[next_space + 1:]
        return Token(token)


class Parser:
    def __init__(self, token_stream):
        self.token_stream = token_stream

    def parse(self, ast = None):
        if ast is None:
            first_token = self.token_stream.get_token()
            ast = Element(first_token.token)
        operator = self.token_stream.get_token()
        if operator.empty:
            return ast
        if operator.operator:
            return self.parse_operator(ast, operator)

    def parse_operator(self, left_ast, operator):
        right_token = self.token_stream.get_token()
        return self.parse(
                Operation(
                    left_ast,
                    Element(right_token.token),
                    Operator(operator.token)
                    )
                )

def test_ast():
    calcul_visitor = Interpreter()
    op = Operation(Element(7), Element(3), Operator('+'))
    Operation(op, op, Operator('+')).accept(calcul_visitor)
    calcul_visitor.print_result()

def test_lexer():
    string = '1 + 3 + 4 + 50 + 1 + 0'
    lexer = Lexer(string)
    token = lexer.get_token()
    while (not token.empty):
        print(token.token)
        token = lexer.get_token()

def test_parser():
    parser = Parser(Lexer('1 + 2 + 3'))
    ast = parser.parse()
    ast.accept(PrettyPrint())
    print()

while True:
    try:
        _in = input('string to calculate:')
    except EOFError:
        print()
        break
    ast = Parser(Lexer(_in)).parse()
    ast.accept(PrettyPrint())
    calc = Interpreter()
    ast.accept(calc)
    print(' = ', end='')
    calc.print_result()
