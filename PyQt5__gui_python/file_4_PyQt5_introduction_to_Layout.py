# PyQt5 Layout

import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QWidget,QVBoxLayout,QHBoxLayout,QGridLayout
from PyQt5.QtGui import QIcon

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setGeometry(500,200, 500, 400)
        self.setWindowTitle("Your first PyQt5 cool GUI")
        self.setWindowIcon(QIcon("C:\\Users\\abulb\\OneDrive\\Pictures\\Screenshots\\67.jpg"))
        self.initUI()

    # To keep the code organized we can use a separate method to write our ui functionality, then call that method while we initialize our constructor
    def initUI(self):
        # Our layout managers are not compatible with our MainWindow widget, MainWindow widget has a specific design and layout structure, so what we do is: we create a genericWidget add layout manager to that genericWidget, then add that genericWidget to our window object in order to display our window with a specific layout

        central_widget = QWidget()
        self.setCentralWidget(central_widget)

        label1 = QLabel("#1", self)
        label2 = QLabel("#2", self)
        label3 = QLabel("#3", self)
        label4 = QLabel("#4", self)
        label5 = QLabel("#5", self)

        label1.setStyleSheet("background-color: red;")
        label2.setStyleSheet("background-color: blue;")
        label3.setStyleSheet("background-color: green;")
        label4.setStyleSheet("background-color: yellow;")
        label5.setStyleSheet("background-color: purple;")

        # 1️⃣ vertical layout
        # Vbox = QVBoxLayout()

        # vbox.addWidget(label1) 
        # vbox.addWidget(label2) 
        # vbox.addWidget(label3) 
        # vbox.addWidget(label4) 
        # vbox.addWidget(label5) 

        # central_widget.setLayout(vbox)
        
        # 2️⃣ Horizontal Layout
        # Hbox = QHBoxLayout()

        # Hbox.addWidget(label1) 
        # Hbox.addWidget(label2) 
        # Hbox.addWidget(label3) 
        # Hbox.addWidget(label4) 
        # Hbox.addWidget(label5) 

        # central_widget.setLayout(Hbox)

        # 3️⃣ Grid Layout
        grid = QGridLayout()

        grid.addWidget(label1, 0, 0) 
        grid.addWidget(label2, 0, 1) 
        grid.addWidget(label3, 1, 0) 
        grid.addWidget(label4, 1, 1) 
        grid.addWidget(label5, 2, 2) 
        
        # adding our layout manager widget to generic widget
        central_widget.setLayout(grid)
        
        

def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()


    