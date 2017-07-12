
import sys
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *

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

        self.mbar = self.menuBar()
        self.filemenu = self.mbar.addMenu("fichier")
        self.filemenu.addAction(self.openact)
        self.filemenu.addAction(self.saveact)
        self.filemenu.addAction(self.quitact)

        self.text = QTextEdit("Hello World", self)
        self.setCentralWidget(self.text)



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