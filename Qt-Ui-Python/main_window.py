# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'untitled.ui'
#
# Created by: PyQt5 UI code generator 5.15.11
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(2100, 1400)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.stackedWidget = QtWidgets.QStackedWidget(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("STHupo")
        font.setPointSize(30)
        self.stackedWidget.setFont(font)
        self.stackedWidget.setObjectName("stackedWidget")
        self.main_menu = QtWidgets.QWidget()
        self.main_menu.setObjectName("main_menu")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.main_menu)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.title = QtWidgets.QLabel(self.main_menu)
        font = QtGui.QFont()
        font.setPointSize(50)
        font.setBold(False)
        font.setUnderline(True)
        font.setWeight(50)
        self.title.setFont(font)
        self.title.setAlignment(QtCore.Qt.AlignCenter)
        self.title.setObjectName("title")
        self.verticalLayout_2.addWidget(self.title)
        self.text_editor_frame = QtWidgets.QFrame(self.main_menu)
        self.text_editor_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.text_editor_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.text_editor_frame.setObjectName("text_editor_frame")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.text_editor_frame)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        spacerItem = QtWidgets.QSpacerItem(294, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem)
        self.text_editor_push_button = QtWidgets.QPushButton(self.text_editor_frame)
        self.text_editor_push_button.setMinimumSize(QtCore.QSize(500, 120))
        self.text_editor_push_button.setObjectName("text_editor_push_button")
        self.horizontalLayout_2.addWidget(self.text_editor_push_button)
        spacerItem1 = QtWidgets.QSpacerItem(294, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem1)
        self.verticalLayout_2.addWidget(self.text_editor_frame)
        spacerItem2 = QtWidgets.QSpacerItem(20, 500, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Maximum)
        self.verticalLayout_2.addItem(spacerItem2)
        self.stackedWidget.addWidget(self.main_menu)
        self.text_editor = QtWidgets.QWidget()
        self.text_editor.setObjectName("text_editor")
        self.stackedWidget.addWidget(self.text_editor)
        self.horizontalLayout.addWidget(self.stackedWidget)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 18))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.text_editor_push_button.clicked.connect(lambda: self.text_editor_push_button_clicked())

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.title.setText(_translate("MainWindow", "Trackmania Tools"))
        self.text_editor_push_button.setText(_translate("MainWindow", "Text Editor"))

    def text_editor_push_button_clicked(self):
        self.stackedWidget.setCurrentIndex(1)


def main():
    import sys
    app = QtWidgets.QApplication(sys.argv)
    main_window = QtWidgets.QMainWindow()
    ui_main_window = Ui_MainWindow()
    ui_main_window.setupUi(main_window)
    main_window.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
