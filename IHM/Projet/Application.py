
import sys
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QAction, QMainWindow, QWidget, QVBoxLayout, QHBoxLayout, QPushButton, QSlider,\
                            QColorDialog, QFileDialog, QMessageBox, QApplication
from Feuille import Feuille
# pylint: disable=W0201
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.init()
    def init(self):
        self.resize(200, 300)
        self.sbar = self.statusBar()

        self.openact = QAction("ouvrir", self)
        self.openact.setShortcut("Ctrl+O")
        self.openact.setToolTip("ouvrir un fichier")
        self.openact.setStatusTip("ouvrir un fichier")
        self.openact.triggered.connect(self.openFile)

        self.saveact = QAction("sauvegarder", self)
        self.saveact.setShortcut("Ctrl+S")
        self.saveact.setToolTip("sauvegarder le fichier")
        self.saveact.setStatusTip("sauvegarder le fichier")
        self.saveact.triggered.connect(self.saveFile)

        self.quitact = QAction("quitter", self)
        self.quitact.setShortcut("Ctrl+Q")
        self.quitact.setToolTip("quitter")
        self.quitact.setStatusTip("quitter")
        self.quitact.triggered.connect(self.quitApp)

        self.choosecolact = QAction("choisir couleur", self)
        self.choosecolact.setShortcut("Ctrl+C")
        self.choosecolact.setToolTip("choisir couleur")
        self.choosecolact.setStatusTip("choisir couleur")
        self.choosecolact.triggered.connect(self.setColor)


        self.mbar = self.menuBar()
        self.filemenu = self.mbar.addMenu("fichier")
        self.filemenu.addAction(self.openact)
        self.filemenu.addAction(self.saveact)
        self.filemenu.addAction(self.quitact)
        self.filemenu.addAction(self.choosecolact)

        wid = QWidget()
        self.vbox = QVBoxLayout()

        self.hbox = QHBoxLayout()
        self.eraseonebutton = QPushButton(self)
        self.eraseonebutton.setText("erase one")
        self.eraseonebutton.clicked.connect(self.eraseOne)

        self.eraseallbutton = QPushButton(self)
        self.eraseallbutton.setText("erase all")
        self.eraseallbutton.clicked.connect(self.eraseAll)

        self.widthslider = QSlider(Qt.Horizontal, self)
        self.widthslider.valueChanged.connect(self.changeWidth)

        self.hbox.addWidget(self.eraseallbutton)
        self.hbox.addWidget(self.eraseonebutton)
        self.hbox.addWidget(self.widthslider)

        self.zone = Feuille()
        self.vbox.addLayout(self.hbox)
        self.vbox.addWidget(self.zone)
        wid.setLayout(self.vbox)
        self.setCentralWidget(wid)

    def eraseOne(self, e):
        if self.zone.paths:
            self.zone.paths.pop()
        self.zone.point1, self.zone.point2 = None, None
        self.zone.update()
    def eraseAll(self, e):
        self.zone.paths = []
        self.zone.update()
    def changeWidth(self, e):
        self.zone.width = e
        #self.zone.update()
    def setColor(self, e):
        self.colordial = QColorDialog.getColor()
        self.zone.color = self.colordial
        #self.zone.update()
    def openFile(self):
        self.openf = QFileDialog.getOpenFileName(self)
        ishtml = False
        if self.openf[0][-5:] == ".html":
            ishtml = True
        self.openf = open(self.openf[0])
        self.string = self.openf.read()
        self.openf.close()


        if ishtml:
            self.text.setHtml(self.string)
        else:
            self.text.setText(self.string)


    def saveFile(self, e):
        self.savef = QFileDialog.getSaveFileName(self)
        self.savef = open(self.savef[0], "w")
        self.savef.write(self.text.toPlainText())
        self.savef.close()

    def quitApp(self, e = None):
        reply = QMessageBox.question(self, 'Message',\
            "Are you sure to quit?", QMessageBox.Yes |\
            QMessageBox.No, QMessageBox.No)
        if reply == QMessageBox.Yes:
            sys.exit()
        else:
            if not e is None:
                e.ignore()

    def closeEvent(self, e):
        self.quitApp(e)
def main(args):
    app = QApplication(args)
    mainw = MainWindow()
    mainw.show()
    app.exec_()

if __name__ == "__main__":
    main(sys.argv)