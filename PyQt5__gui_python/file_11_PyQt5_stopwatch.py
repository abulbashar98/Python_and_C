# PyQt5 Stopwatch program

import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QHBoxLayout, QLabel, QPushButton
from PyQt5.QtCore import QTime, QTimer, Qt 


class Stopwatch(QWidget):
    def __init__(self):
        super().__init__()
        self.time_label = QLabel("00:00:00",self)
        self.start_button = QPushButton("start", self)
        self.stop_button = QPushButton("stop", self)
        self.reset_button = QPushButton("reset", self)
        self.time = QTime(0,0,0,0)
        self.timer = QTimer(self)
        self.initUI()

    def initUI(self):
        self.time_label.setAlignment(Qt.AlignCenter)
        vbox = QVBoxLayout()
        
        vbox.addWidget(self.time_label)
        # vbox.addWidget(self.start_button)
        # vbox.addWidget(self.stop_button)
        # vbox.addWidget(self.reset_button)

        hbox = QHBoxLayout()

        hbox.addWidget(self.start_button)
        hbox.addWidget(self.stop_button)
        hbox.addWidget(self.reset_button)

        vbox.addLayout(hbox)

        self.setLayout(vbox)

        self.setStyleSheet("""
            QLabel{
                font-size: 80px;
                background-color: hsl(186, 83%, 60%);
                border: 2px solid;
                border-radius: 15px;
                font-weight: bold;
                font-family: calibre;
                padding: 5px;
            }
            QPushButton{
                font-size: 15px;
                font-weight: bold;
            }                   
        """)

        self.start_button.clicked.connect(self.start)
        self.stop_button.clicked.connect(self.stop)
        self.reset_button.clicked.connect(self.reset)
        
        self.timer.timeout.connect(self.update_display)

    
    def start(self):
        self.timer.start(10)

    def stop(self):
        self.timer.stop()

    def reset(self):
        self.timer.stop()
        self.time = QTime(0,0,0,0)
        self.time_label.setText(self.format_time(self.time))

    def format_time(self, time):
        hour = time.hour()
        minute = time.minute()
        second = time.second()
        milSecond = int(time.msec() / 10)

        return f"{hour}:{minute}:{second}.{milSecond}" 

    def update_display(self):
        self.time = self.time.addMSecs(10)
        self.time_label.setText(self.format_time(self.time))

if __name__ == '__main__':
    app = QApplication(sys.argv)
    stopwatch = Stopwatch()
    stopwatch.show()
    sys.exit(app.exec_())




# import sys
# from PyQt5.QtWidgets import QApplication,QPushButton, QLabel, QWidget, QHBoxLayout, QVBoxLayout
# from PyQt5.QtCore import QTime, QTimer, Qt

# class Stopwatch(QWidget):
#     def __init__(self):
#         super().__init__()
#         self.time_label = QLabel("12:00:00", self)
#         self.time = QTime(0, 0, 0, 0,)
#         self.timer = QTimer(self)
#         self.start_button = QPushButton("start", self)
#         self.stop_button = QPushButton("stop", self)
#         self.reset_button = QPushButton("reset", self)
#         self.initUI()
        
#     def initUI(self):
#         self.setWindowTitle("Python StopWatch with PyQt5")
#         self.time_label.setAlignment(Qt.AlignCenter)

#         vbox = QVBoxLayout()
        
#         vbox.addWidget(self.time_label)
        
#         hbox = QHBoxLayout()

#         hbox.addWidget(self.start_button)
#         hbox.addWidget(self.stop_button)
#         hbox.addWidget(self.reset_button)

#         vbox.addLayout(hbox)

#         self.setLayout(vbox)

#         self.setStyleSheet("""
#             QPushButton, QLabel{
#                 font-weight: bold;
#             }               
#             QLabel{
#                 font-size: 60px;
#                 border: 2px solid;
#                 border-radius: 15px;
#                 background-color: hsl(186, 83%, 60%);
#                 padding: 15px;              
#             }
#             QPushButton{
#                 font-size: 15px;
#                 padding: 5px;
#                 background-color: 
#             }       
#         """)

#         self.start_button.clicked.connect(self.start)
#         self.stop_button.clicked.connect(self.stop)
#         self.reset_button.clicked.connect(self.reset)

#         self.timer.timeout.connect(self.update_display)

#     def start(self):
#         self.timer.start(10)

#     def stop(self):
#         self.timer.stop()

#     def reset(self):
#         self.timer.stop()
#         self.time = QTime(0,0,0,0)
#         self.time_label.setText(self.format_time(self.time))

#     def format_time(self, time):
#         hour = time.hour()
#         minute = time.minute()
#         second = time.second()
#         milSecond = int(time.msec() / 10)

#         return f"{hour}:{minute}:{second}.{milSecond}"

#     def update_display(self):
#         self.time = self.time.addMSecs(10)
#         self.time_label.setText(self.format_time(self.time))    


# if __name__ == '__main__':
#     app = QApplication(sys.argv)
#     stopwatch = Stopwatch()
#     stopwatch.show()
#     sys.exit(app.exec_())

