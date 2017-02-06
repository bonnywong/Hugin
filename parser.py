import sys
import os
from PyPDF2 import PdfFileReader
from PyQt5.QtWidgets import (QWidget, QApplication, QMainWindow, QAction,
                             QFileDialog, QMessageBox, QLabel)
from PyQt5.QtGui import QIcon

class Parser(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initMenu(self):
        # Main menu
        mainMenu = self.menuBar()
        mainMenu.setNativeMenuBar(False)
        fileMenu = mainMenu.addMenu("File")
        aboutMenu = mainMenu.addMenu("About")

        # Open button
        openButton = QAction("Open...", self)
        openButton.setShortcut("CTRL+O")
        openButton.setStatusTip("Open file")
        openButton.triggered.connect(self.openFileDialog)
        fileMenu.addAction(openButton)

        # Export button
        exportBtn = QAction("Export", self)
        exportBtn.setShortcut("CTRL+E")
        exportBtn.setStatusTip("Export parsed content")
        fileMenu.addAction(exportBtn)

        # Import button
        importBtn = QAction("Import", self)
        importBtn.setShortcut("CTRL+I")
        importBtn.setStatusTip("Import parsed content")
        fileMenu.addAction(importBtn)

        # Help button
        helpBtn = QAction("Help", self)
        helpBtn.setStatusTip("Help......")
        helpBtn.triggered.connect(self.showHelpDialog)
        aboutMenu.addAction(helpBtn)

        # Exit button
        exitButton = QAction("Exit", self)
        exitButton.setShortcut("CTRL+Q")
        exitButton.setStatusTip("Exit application")
        exitButton.triggered.connect(self.close)
        fileMenu.addAction(exitButton)

    def initUI(self):

        # Windows
        self.resize(540, 320)
        self.setWindowTitle('Icon')
        self.setWindowIcon(QIcon('web.png'))
        self.setWindowTitle('Hugin pre-process')

        # Status bar
        self.statusBar().showMessage("Ready")

        # Initiate menu
        self.initMenu()

        # Init label
        self.lbl = QLabel(self)
        self.lbl.move(20, 40)

        # Show
        self.show()

    def openFileDialog(self):
        print("Opening QFileDialog.")
        filename = QFileDialog.getOpenFileName(self, "Open File", os.getcwd())
        print("Filename: ", filename)
        for s in filename:
            print(s)
        self.lbl.setText("Filename: " + filename[0])
        self.lbl.adjustSize()
        self.readPDF(filename[0])

    def readPDF(self, filename):
        print("In readpdf")
        pdf = PdfFileReader(filename)
        print(pdf.documentInfo.title)
        for s in pdf.documentInfo:
            print(s)
        print("Number of pages: ", pdf.getNumPages())

    def showHelpDialog(self):
        widget = QWidget()
        result = QMessageBox.about(widget, "Hello! This is a help window.", "Close")
        widget.show()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = Parser()
    sys.exit(app.exec_())
