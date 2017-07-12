import sys

from PyQt5.QtWidgets import *
from PyQt5.QtGui import QPainter, QColor


class MatrixInputWidget(QWidget):
    """Widget to enter the value of a square matrix and modify its size"""

    def __init__(self):

        super().__init__()

        self.initUI()

    def initUI(self):

        #Button to modify the size
        plusButton = QPushButton("+")
        lessButton = QPushButton("-")

        #Grid for layout
        grid = QGridLayout()
        self.setLayout(grid)

        #Add widget to grid
        grid.addWidget(plusButton, 0, 0)
        grid.addWidget(lessButton, 2, 2)


        self.show()

class VectorInputWidget(QWidget):
    """Widget to enter a column vector"""

    def __init__(self):

        super().__init__()

        self.initUI()


    def initUI(self):

        #Grid for layout
        grid = QGridLayout()
        self.setLayout(grid)
        self.show()     


        
class SystemInputWidget(QWidget):
    """Widget to enter a linear system"""

    def __init__(self):

        super().__init__()

        self.initUI()


    def initUI(self):

        pass
        
    


class LinearSystemInterface(QMainWindow):
    """Interface to enter a linearSystem, print LU decomposition and solve it with LU or Jacobi method"""

    def __init__(self):

        super().__init__()

        self.initUI()

    def initUI(self):

        self.setGeometry(300, 300, 300, 200)
        self.setWindowTitle("Linear System Solving Interface")

        menubar = self.menuBar()
        lu_decomposition = menubar.addMenu('LU')
        jacobi = menubar.addMenu('Jacobi')

        miw = MatrixInputWidget()

        self.setCentralWidget(miw)

        
        
        
        self.statusBar().showMessage('Ready')
        self.show()



if __name__ == "__main__":

    
    app = QApplication(sys.argv)
    lsi = LinearSystemInterface()
    sys.exit(app.exec_())
