import sys
import os
from PyQt5.QtWidgets import *

def openFileDialog():
    print("Opening QFileDialog.")
    filename = QFileDialog.getOpenFileName(window, "Open File", os.getcwd())
    print(filename)

def showHelpDialog():
    widget = QWidget()
    result = QMessageBox.about(widget, "Hello! This is a help window.", "Close")
    widget.show()

app = QApplication(sys.argv)

# Window initialization
window = QMainWindow()
window.resize(520, 340)
window.setWindowTitle("Munin!")

# Main menu
mainMenu = window.menuBar()
mainMenu.setNativeMenuBar(False)
fileMenu = mainMenu.addMenu("File")
aboutMenu = mainMenu.addMenu("About")

# Open button
openButton = QAction("Open...", window)
openButton.setShortcut("CTRL+O")
openButton.setStatusTip("Open file")
openButton.triggered.connect(openFileDialog)
fileMenu.addAction(openButton)

# Export button
exportBtn = QAction("Export", window)
exportBtn.setShortcut("CTRL+E")
exportBtn.setStatusTip("Export parsed content")
fileMenu.addAction(exportBtn)

# Help button
helpBtn = QAction("Help", window)
helpBtn.setStatusTip("Help......")
helpBtn.triggered.connect(showHelpDialog)
aboutMenu.addAction(helpBtn)

# Exit button
exitButton = QAction("Exit", window)
exitButton.setShortcut("CTRL+Q")
exitButton.setStatusTip("Exit application")
exitButton.triggered.connect(window.close)
fileMenu.addAction(exitButton)





# Show window
window.show()
sys.exit(app.exec_())