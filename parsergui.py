import sys
import os
from PyQt5.QtWidgets import (QWidget, QApplication, QMainWindow, QAction,
                             QFileDialog, QMessageBox, QLabel)
from PyQt5.QtGui import QIcon
import LanguageProcessor
from FileHandler import FileHandler
from PDFParser import PDFParser
from TokenDialog import TokenDialog


class Parser(QMainWindow):
    def __init__(self, argv=None):
        super().__init__(argv)
        self.initUI()

    def initMenu(self):
        # Main menu
        mainMenu = self.menuBar()
        mainMenu.setNativeMenuBar(False)
        fileMenu = mainMenu.addMenu("File")
        visualizeMenu = mainMenu.addMenu("Visualize")
        tokenMenu = mainMenu.addMenu("Tokens")
        aboutMenu = mainMenu.addMenu("About")

        # fileMenu options
        # Open button
        openButton = QAction("Open...", self)
        openButton.setShortcut("CTRL+O")
        openButton.setStatusTip("Open file")
        openButton.triggered.connect(self.openPDF)
        fileMenu.addAction(openButton)

        # Import button
        importBtn = QAction("Import", self)
        importBtn.setShortcut("CTRL+I")
        importBtn.setStatusTip("Import parsed content")
        importBtn.triggered.connect(self.importFile)
        fileMenu.addAction(importBtn)

        # Export button
        exportBtn = QAction("Export", self)
        exportBtn.setShortcut("CTRL+E")
        exportBtn.setStatusTip("Export parsed content")
        exportBtn.triggered.connect(self.exportFile)
        fileMenu.addAction(exportBtn)

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

        # tokenMenu options
        nounButton = QAction("Noun tokens", self)
        tokenMenu.addAction(nounButton)
        nounButton.triggered.connect(self.openNounTokenDialog)

        verbButton = QAction("Verb tokens", self)
        tokenMenu.addAction(verbButton)
        verbButton.triggered.connect(self.openVerbTokenDialog)

        adjectiveButton = QAction("Adjective tokens", self)
        tokenMenu.addAction(adjectiveButton)
        adjectiveButton.triggered.connect(self.openAdjectiveTokenDialog)


        # visualizeMenu options
        sentenceButton = QAction("Show sentences", self)
        visualizeMenu.addAction(sentenceButton)

    def initUI(self):

        # Windows
        self.resize(740, 420)
        self.setWindowTitle('Icon')
        self.setWindowIcon(QIcon('web.png'))
        self.setWindowTitle('Hugin pre-process')

        # Status bar
        self.statusBar().showMessage("Ready")

        # Initiate menu
        self.initMenu()

        # Init label
        self.nameLabel = QLabel(self)
        self.nameLabel.move(20, 40)

        # Show
        self.show()



    def getOpenFilePath(self):
        print("Opening QFileDialog.getOpenFileName.")
        filePath = QFileDialog.getOpenFileName(self, "Open File", os.getcwd(), "PDF files *.pdf")
        return filePath[0]

    def getSaveFilePath(self):
        print("Opening QFileDialog.getSaveFileName(.")
        filePath = QFileDialog.getSaveFileName(self, "Save File", os.getcwd(), "PDF files *.pdf")
        return filePath[0]

    def openPDF(self):
        print("In openPDF.")
        filePath = self.getFilePath()
        print("Filename: ", filePath)
        self.nameLabel.setText("File: " + filePath)
        self.nameLabel.adjustSize()
        self.parsePDF(filePath)

    def openSaveFileDialog(self):
        return 0

    def parsePDF(self, filepath):
        print("In readpdf")
        parser = PDFParser()
        result = parser.parsePDF(filepath)

    def importFile(self):
        print("Import clicked.")
        filePath = self.getOpenFilePath()
        print(filePath)
        #fh = FileHandler()
        #fh.load(filepath)

    def exportFile(self):
        print("Export clicked.")
        filePath = self.getSaveFilePath()
        print(filePath)

    def showHelpDialog(self):
        widget = QWidget()
        result = QMessageBox.about(widget, "Hello! This is a help window.", "Close")
        widget.show()


    def openNounTokenDialog(self):
        print("openNounTokenDialog")
        self.tokenDialog = TokenDialog("noun")


    def openVerbTokenDialog(self):
        print("openVerbTokenDialog")
        self.tokenDialog = TokenDialog("verb")

    def openAdjectiveTokenDialog(self):
        print("openAdjectiveTokenDialog")
        self.tokenDialog = TokenDialog("adjective")
        self.tokenDialog.show()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = Parser()
    sys.exit(app.exec_())
