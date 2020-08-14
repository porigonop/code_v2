from default_visitor import Visitor
class Interpreter(Visitor):
    memory = 0
    operator = ''
    variable = {}
    def visit_element(self, element):
        """
        1 + 3 : Operation(Elt(1) Op(+) Elt(2))
        """
        self.memory = element.element

    def visit_operator(self, operator):
        self.operator = operator.operator

    def visit_operation(self, operation):
        operation.left_elt.accept(self)
        left_operand = self.memory
        operation.operator.accept(self)
        operator = self.operator
        operation.right_elt.accept(self)
        right_operand = self.memory
        if operator == '+':
            self.memory = left_operand + right_operand
        if operator == '-':
            self.memory = left_operand - right_operand
        if operator == '*':
            self.memory = left_operand * right_operand
        if operator == '/':
            self.memory = left_operand / right_operand
    def visit_assignment(self, assignment):
        assignment.expression.accept(self)
        self.variable[assignment.identifier.identifier] = self.memory
    def visit_identifier(self, identifier):
        self.memory = self.variable[identifier.identifier]
    def print_result(self):
        print(self.memory)
