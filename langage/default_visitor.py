import ast

class Visitor:
    def visit(self, _object):
        # dispatch dynamique, python connais pas mais c++ oui
        # on pourrais faire plus jolie
        if isinstance(_object, ast.Element):
            self.visit_element(_object)
        if isinstance(_object, ast.Identifier):
            self.visit_identifier(_object)
        if isinstance(_object, ast.Assignment):
            self.visit_assignment(_object)
        if isinstance(_object, ast.Operator):
            self.visit_operator(_object)
        if isinstance(_object, ast.Operation):
            self.visit_operation(_object)

    def visit_element(self, element):
        pass
    def visit_identifier(self, identifier):
        pass
    def visit_assignment(self, assignment):
        pass
    def visit_operator(self, operator):
        pass
    def visit_operation(self, operation):
        operation.left_elt.accept(self)
        operation.operator.accept(self)
        operation.right_elt.accept(self)
