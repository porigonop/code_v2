"""
contain the tree object
"""
class Tree(object):
    """
    define the tree object with value and sons
    """
    def __init__(self, value=None):

        self.sons = []
        self.value = value
        self.position = None
    def add(self, tree):
        """
        add a son to the tree
        """
        self.sons.append(tree)

    def __repr__(self):
        return self.rec_repr(0)

    def rec_repr(self, nb_of_tab):
        """
        run throught the tree to return a str of the current tree
        """
        answer = str(self.value) + str(self.position) + "\n|"
        for son in self.sons:
            answer += "\t|"  * nb_of_tab + "------ " + son.rec_repr(nb_of_tab + 1)
        return answer
    def set_pos(self, pos):
        """
        set the position played
        """
        self.position = pos
    def set_value(self, value):
        """
        set value of this node
        """
        self.value = value
    def write_in_file(self, name_of_file: str):
        """
        write the representation of the tree in a file
        """
        msg = str(self)
        fhandle = open(name_of_file, "w")
        fhandle.write(msg)
        fhandle.close()
if __name__ == "__main__":
    a = Tree(3)
    b = Tree(1)
    b.add(Tree(2))
    c = Tree(4)
    c.add(a)
    c.add(b)
    d = Tree(3)
    d.add(Tree(2))
    tr = Tree(2)
    tr.add(d)
    tr.add(c)
    tr.add(c)
    print(tr)
