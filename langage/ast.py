class Visitable:
    def accept(self, visitor):
        visitor.visit(self)


class Element(Visitable):
    def __init__(self, element):
        self.element = element
class Identifier(Visitable):
    def __init__(self, identifier):
        self.identifier = identifier


class Operator(Visitable):
    def __init__(self, operator):
        self.operator = operator


class Operation(Visitable):
    def __init__(self, left_elt, right_elt, operator):
        self.left_elt = left_elt
        self.right_elt = right_elt
        self.operator = operator


class Assignment(Visitable):
    def __init__(self, variable_name, expression):
        self.identifier = variable_name
        self.expression = expression

