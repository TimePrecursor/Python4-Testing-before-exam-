import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

class Event:
    def __init__(self, name):
        self.name = name
        self.handlers = []

    def add_handler(self, handler):
        """Add an event handler function."""
        self.handlers.append(handler)

    def trigger(self, *args, **kwargs):
        """Call all event handlers."""
        for handler in self.handlers:
            handler(*args, **kwargs)


# Event handler function
def on_number_exceeds_threshold(number):
    print(f"Event triggered! The number {number} has exceeded the threshold.")

# Create the event
threshold_event = Event("threshold_exceeded")

# Add the handler to the event
threshold_event.add_handler(on_number_exceeds_threshold)



# Set up the main Login Window
def window():
    app = QApplication(sys.argv)
    w = QWidget()
    label1 = QLabel(w)
    pushb1 = QPushButton(w)
    pushb1.setGeometry(1,1,100,100)
    label1.setText("Hello World!")
    w.setGeometry(100,100,500,500)
    label1.move(100, 50)
    w.resize(500,200)
    w.setWindowTitle("BMI Calculator")

    username1 = QLineEdit(w)
    username1.setEchoMode(QLineEdit.PasswordEchoOnEdit)
    username1.setGeometry(200,20,100,20)

    w.show()
    sys.exit(app.exec_())

# Access the Logins1 file









if __name__ == '__main__':
   window()