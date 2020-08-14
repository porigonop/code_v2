from default_visitor import Visitor

class PrettyPrint(Visitor):
    def visit_element(self, element):
        print(element.element, end='')
    def visit_operator(self, operator):
        print(operator.operator, end='')
    def visit_operation(self, operation):
        print('(', end='')
        operation.left_elt.accept(self)
        print(' ', end='')
        operation.operator.accept(self)
        print(' ', end='')
        operation.right_elt.accept(self)
        print(')', end='')

    def visit_assignment(self, assignment):
        assignment.identifier.accept(self)
        print(' = ', end='')
        assignment.expression.accept(self)
    def visit_identifier(self, identifier):
        print(identifier.identifier, end='')
