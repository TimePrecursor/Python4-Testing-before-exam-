from PyQt5.QtWidgets import *
import sys



class Second2(QMainWindow):
    def __init__(self, parent=None):
        super(Second2, self).__init__(parent)
        # setting title
        self.setWindowTitle("Python ")

        # setting geometry
        self.setGeometry(100, 100, 300, 200)

        # calling methods
        self.UiComponents2()

        # # showing all the widgets
        # self.show()

    def UiComponents2(self):
        import Python4 as py4
        self.label2 = QLabel(self)
        self.label2.setText(f"Welcome {py4.Window.strlol}!")
        self.label2.setGeometry(10, 10, 200, 100)

# App = QApplication(sys.argv)
#
# # create the instance of our Window
# window = Window2()
#
# # start the app
# sys.exit(App.exec())
