from time import sleep
from typing import Any
from typing import Any

import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
import datetime as dt


class Second(QMainWindow):
    def __init__(self, parent=None):
        super(Second, self).__init__(parent)


Currentuser = None

class Window(QMainWindow):
    def __init__(self):
        super().__init__()

        # setting title
        self.Currentuser = str()
        self.setWindowTitle("Python ")

        # setting geometry
        self.setGeometry(100, 100, 100, 100)

        # calling methods
        self.UiComponents()
        self.mainWindowSetup()

        # showing all the widgets
        self.show()

    def mainWindowSetup(self):
        self.setFixedSize(500, 300)
        self.setWindowTitle("Temperature Converter (TESTING)")

    def RunSecondWindow(self):
        import window2test as wt
        window2 = wt.Second2(self)
        window2.show()
        # Window.hide(self)


    def loginstuff2(self):
        usern = self.userin.text()
        with open("../../Downloads/Logins2.txt") as file:
            lines = file.readlines()
            # print(usern)
            for pos, line in enumerate(lines):
                x = line.split("|")
                # print(x)
                passinput = self.passin.text()
                if x[2] == usern:
                    import PasswordCheck as ft
                    bool1 = ft.functionclass.passwordstep(self,pos,passinput)
                    if bool1 == True:

                        Currentuser = x[0]
                        print(x[0])

                        self.RunSecondWindow()
                    else:
                        print("Wrong Password!")
                        break
                    break
    def strlol(self):
        var = self.loginstuff2.Currentuser
        print(var)
        return var



    # method for widgets
    def UiComponents(self):
        self.userlabel = QLabel(self)
        self.passlabel = QLabel(self)
        self.userin = QLineEdit(self)
        self.passin = QLineEdit(self)
        self.pushb1 = QPushButton(self)

        self.userlabel.setText("Enter Username:")
        self.userlabel.setGeometry(10,10,100,20)
        self.passlabel.setText("Enter Password:")
        self.passlabel.setGeometry(10, 50, 100, 20)
        self.userin.setGeometry(100,10,100,20)
        self.pushb1.setText("Login as")
        self.pushb1.setGeometry(50, 100, 150, 50)
        self.pushb1.clicked.connect(self.loginstuff2)
        self.passin.setGeometry(100,50,100,20)
        self.passin.setEchoMode(QLineEdit.Password)



class Logininfo:
  def __init__(self, f_name1, l_name1, user1, pass1):
    self.f_name1 = f_name1
    self.l_name1 = l_name1
    self.user1 = user1
    self.pass1 = pass1

  def __str__(self):
    return f"({self.f_name1}|{self.l_name1}|{self.user1}|{self.pass1})"


def main():
    # create pyqt5 app
    App = QApplication(sys.argv)

    # create the instance of our Window
    window = Window()

    # start the app
    sys.exit(App.exec())


    window.show()
    sys.exit(app.exec_())

# class Currentuserdef():
#     def __init__(self):
#         self.Currentuser = Currentuser
#
#     def str(self):
#         return Currentuser


if __name__ == '__main__':
    main()

# just incase:
# www.geeksforgeeks.org/pyqt5-how-to-add-action-to-a-button/

