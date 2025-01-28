import sys
from PyQt5.QtWidgets import (QApplication, QWidget, QLabel, QPushButton, QVBoxLayout, QHBoxLayout) 
#^these are the building blocks of our applications

from PyQt5.QtCore import QTimer, QTime, Qt

class Stopwatch(QWidget):
    def __init__(self):
        super().__init__()
        self.time = QTime(0,0,0,0) #used to keep track of the time, keeps track of hours, minutes, seconds, milliseconds
        self.time_label = QLabel("00:00:00:00", self)
        self.start_button = QPushButton("Start", self)
        self.stop_button = QPushButton("Stop", self)
        self.reset_button = QPushButton("Reset", self)
        self.timer = QTimer(self)
        self.initUI()
    
    def initUI(self): # a way to change the interface
        self.setWindowTitle("Stopwatch") #changes the window name from Python to topwatch
       
         
        vbox = QVBoxLayout() #verticle layout manager
        vbox.addWidget(self.time_label) # alabel for the time
       
        self.setLayout(vbox)
        
        self.time_label.setAlignment(Qt.AlignCenter) #allign all teh button to the center even if the window gets stretched
        
        hbox = QHBoxLayout()
        hbox.addWidget(self.start_button) # a button for start
        hbox.addWidget(self.stop_button) # a button for stop
        hbox.addWidget(self.reset_button) # a button for reset
        
        vbox.addLayout(hbox)
        
        self.setStyleSheet("""
                           QPushButton, QLabel
                           {
                             padding: 20px;
                             font-weight: bold;
                             font-family: Impact;
                           }
                           
                            QPushButton
                            {
                             font-size:50px;
                             }
                             
                             QLabel
                             {
                                 font-size:120px;
                                 background-color: hsl(145, 54%, 46%);
                                 border radius: 20px;
                            }""")
        #^ the code above allows me to change the apperance of stuff like the font of the buttons and labels
        
        self.start_button.clicked.connect(self.start)
        self.stop_button.clicked.connect(self.stop)
        self.reset_button.clicked.connect(self.reset)
        self.timer.timeout.connect(self.update_display)
        #^these are used so that when you click the button on the sceen, it connects to method associated with the button
        
    def start(self): # a way to start the stop watch
        self.timer.start(10) #sets a timeout every 10 seconds
    
    def stop(self): # a way to end the stop watch
        self.timer.stop()
    
    def reset(self): # a way to reset the stop watch
        self.timer.stop()
        self.time = QTime(0,0,0,0)
        self.time_label.setText(self.format_time(self.time))
    
    def format_time(self, time):# a way to format the time
        hours = time.hour()
        minutes = time.minute()
        seconds = time.second()
        milliseconds = time.msec() // 10
        #^these are used to get our time, with milliseond I devide it by 2 to have 2 digits instead of 3
        return f"{hours:02}:{minutes:02}:{seconds:02}.{milliseconds:02}" 
        #This is used to make our time into a string so that our time can be seen, I have 02 because I want 2 leading zeros so "00:""
    
    def update_display(self): # a way to update the display
        self.time = self.time.addMSecs(10) #this updates the timer every 10 milliseconds
        self.time_label.setText(self.format_time(self.time))
    
if __name__ == "__main__":
    app = QApplication(sys.argv)
    stopwatch = Stopwatch()
    stopwatch.show()
    sys.exit(app.exec_())
