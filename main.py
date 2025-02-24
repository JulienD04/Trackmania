import sys

from PyQt5 import QtCore, QtGui, QtWidgets

sys.path.append("../Trackmania")
sys.path.append("Qt_Ui_Python")
sys.path.append("Classes")
from main_window import Ui_MainWindow


def main():
    app = QtWidgets.QApplication(sys.argv)
    main_window = QtWidgets.QMainWindow()
    main_window_ui = Ui_MainWindow()
    main_window_ui.setupUi(main_window)
    main_window.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
