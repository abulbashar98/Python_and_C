# PyQt5 Cascading Style Sheet
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow,QWidget, QPushButton,QHBoxLayout
from PyQt5.QtGui import QIcon

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Your first PyQt5 cool GUI")
        self.setWindowIcon(QIcon("C:\\Users\\abulb\\OneDrive\\Pictures\\Screenshots\\67.jpg"))

        self.button1 = QPushButton("#1", self)
        self.button2 = QPushButton("#2", self)
        self.button3 = QPushButton("#3", self)
        self.initUI()
    
    def initUI(self):
        central_widget = QWidget()
        self.setCentralWidget(central_widget)

        hbox = QHBoxLayout()

        hbox.addWidget(self.button1)
        hbox.addWidget(self.button2)
        hbox.addWidget(self.button3)

        central_widget.setLayout(hbox)

        self.button1.setObjectName("button1")
        self.button2.setObjectName("button2")
        self.button3.setObjectName("button3")

        self.setStyleSheet("""
                QPushButton{
                    font-size: 30px;
                    font-family: Arial;
                    padding: 15px 50px;
                    margin: 25px;
                    border: 2px solid;
                    border-radius: 10px;
                }
                QPushButton#button1{
                    background-color: hsl(342, 75%, 47%);
                }
                QPushButton#button2{
                    background-color: hsl(210, 77%, 57%);
                }
                QPushButton#button3{
                    background-color: hsl(121, 85%, 53%);
                }
                QPushButton#button1:hover{
                    background-color: hsl(342, 75%, 67%);
                }
                QPushButton#button2:hover{
                    background-color: hsl(210, 77%, 77%);
                }
                QPushButton#button3:hover{
                    background-color: hsl(121, 85%, 73%);
                }                                  
            """)




def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()


    