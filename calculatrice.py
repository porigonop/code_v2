class Element:
    def __init__(self, element):
        self.element = element
    def accept(self, visitor):
        visitor.visit(self)


class Operator:
    def __init__(self, operator):
        self.operator = operator
    def accept(self, visitor):
        visitor.visit(self)


class Operation:
    def __init__(self, left_elt, right_elt, operator):
        self.left_elt = left_elt
        self.right_elt = right_elt
        self.operation = operator
    def accept(self, visitor):
        visitor.visit(self)


class Visitor:
    def visit(self, _object):
        # dispatch dynamique, python connais pas mais c++ oui
        # on pourrais fair plus jolie
        if isinstance(_object, Element):
            self.visit_element(_object)
        if isinstance(_object, Operator):
            self.visit_operator(_object)
        if isinstance(_object, Operation):
            self.visit_operation(_object)
    def visit_element(self, element):
        pass
    def visit_operator(self, operator):
        pass
    def visit_operation(self, operation):
        self.visit(operation.left_elt)
        self.visit(operation.operation)
        self.visit(operation.right_elt)

class Calcul(Visitor):
    memory = 0
    operator = ''
    def visit_element(self, element):
        print(element.element, self.memory, self.operator)
        if self.operator == '':
            self.memory = element.element
        else:
            if self.operator == '+':
                self.memory += element.element


    def visit_operator(self, operator):
        self.operator = operator.operator

    def print_result(self):
        print(self.memory)


class Token:
    operator = False
    empty = False
    def __init__(self, token):
        self.token = token
        if token == '+':
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

def test_ast():
    calcul_visitor = Calcul()
    op = Operation(Element(7), Element(3), Operator('+'))
    Operation(op, op, Operator('+')).accept(calcul_visitor)
    calcul_visitor.print_result()

def test_lexer():
    string = '1 + 3 + 4 + 5 + 1 + 0'
    lexer = Lexer(string)
    token = lexer.get_token()
    while (not token.empty):
        print(token.token)
        token = lexer.get_token()

test_lexer()
