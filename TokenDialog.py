from PyQt5.QtWidgets import (QWidget, QApplication, QMainWindow, QAction,
                             QFileDialog, QMessageBox, QLabel, QPushButton,
                             QHBoxLayout, QVBoxLayout)

from PyQt5.QtGui import QIcon

class TokenDialog(QMainWindow):

    def __init__(self, title, argv=None):
        super().__init__(argv)
        print("Created a TokenDialog")
        print(title)
        self.initUI(title)

    def initUI(self, title):
        self.setGeometry(300, 300, 300, 150)
        addButton = QPushButton("Add", self)
        removeButton = QPushButton("Remove", self)

        hbox = QHBoxLayout()
        hbox.addStretch(1)
        hbox.addWidget(addButton)
        hbox.addWidget(removeButton)

        vbox = QVBoxLayout()
        vbox.addStretch(1)
        vbox.addLayout(hbox)

        if title == "verb":
            self.handleVerbs(title, vbox)
        elif title == "noun":
            self.handleNouns(title, vbox)
        else:
            self.handleAdjectives(title, vbox)


    def handleVerbs(self, title, vbox):
        self.setWindowTitle(title)
        self.setLayout(vbox)
        self.show()


    def handleNouns(self, title, vbox):
        self.setWindowTitle(title)
        self.setLayout(vbox)
        self.show()

    def handleAdjectives(self, title, vbox):
        self.setWindowTitle(title)
        self.setLayout(vbox)
