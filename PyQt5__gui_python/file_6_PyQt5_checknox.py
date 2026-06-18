# PyQt5 checkbox functionality

import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QCheckBox
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import Qt

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setGeometry(500,200, 500, 400)
        self.setWindowTitle("Your first PyQt5 cool GUI")
        self.setWindowIcon(QIcon("C:\\Users\\abulb\\OneDrive\\Pictures\\Screenshots\\67.jpg"))
        self.checkbox = QCheckBox("Do you like food?", self)
        self.initUI()
    
    def initUI(self):
        self.checkbox.setGeometry(100, 50, 250, 100)
        self.checkbox.setStyleSheet("font-size: 20px;"
                                    "font-family: Arial;")
        self.checkbox.setChecked(False)
        self.checkbox.stateChanged.connect(self.changed_state)

    def changed_state(self,state):
        # print(state)
        if state == Qt.Checked:
            print("You DO like food!")
        else: 
            print("You DO NOT like food")



def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()


    