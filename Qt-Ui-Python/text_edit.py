# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'text_edit.ui'
#
# Created by: PyQt5 UI code generator 5.15.11
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_text_editor(object):
    def setupUi(self, text_editor):
        text_editor.setObjectName("text_editor")
        text_editor.resize(2200, 1600)
        font = QtGui.QFont()
        font.setFamily("STHupo")
        font.setPointSize(24)
        text_editor.setFont(font)
        self.top_layout = QtWidgets.QVBoxLayout(text_editor)
        self.top_layout.setObjectName("top_layout")
        spacerItem = QtWidgets.QSpacerItem(20, 350, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        self.top_layout.addItem(spacerItem)
        self.title = QtWidgets.QLabel(text_editor)
        self.title.setMinimumSize(QtCore.QSize(0, 150))
        self.title.setMaximumSize(QtCore.QSize(999999, 150))
        font = QtGui.QFont()
        font.setPointSize(50)
        font.setUnderline(True)
        font.setWeight(50)
        self.title.setFont(font)
        self.title.setStyleSheet("background-color: rgb(0, 0, 0);\ncolor: rgb(255, 255, 255);")
        self.title.setAlignment(QtCore.Qt.AlignCenter)
        self.title.setObjectName("title")
        self.top_layout.addWidget(self.title)
        self.top_frame = QtWidgets.QFrame(text_editor)
        self.top_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.top_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.top_frame.setObjectName("top_frame")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.top_frame)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.input_line_edit_top_frame = QtWidgets.QFrame(self.top_frame)
        self.input_line_edit_top_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.input_line_edit_top_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.input_line_edit_top_frame.setObjectName("input_line_edit_top_frame")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.input_line_edit_top_frame)
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem3 = QtWidgets.QSpacerItem(250, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem3)
        self.input_line_edit = QtWidgets.QLineEdit(self.input_line_edit_top_frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.input_line_edit.sizePolicy().hasHeightForWidth())
        self.input_line_edit.setSizePolicy(sizePolicy)
        self.input_line_edit.setMinimumSize(QtCore.QSize(750, 75))
        self.input_line_edit.setMaximumSize(QtCore.QSize(750, 75))
        self.input_line_edit.setObjectName("input_line_edit")
        self.horizontalLayout.addWidget(self.input_line_edit)
        spacerItem4 = QtWidgets.QSpacerItem(277, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem4)
        self.verticalLayout_3.addWidget(self.input_line_edit_top_frame)
        self.output_top_frame = QtWidgets.QFrame(self.top_frame)
        self.output_top_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.output_top_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.output_top_frame.setObjectName("output_top_frame")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.output_top_frame)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        spacerItem7 = QtWidgets.QSpacerItem(277, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem7)
        
        self.output_label = QtWidgets.QLabel(self.output_top_frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.output_label.sizePolicy().hasHeightForWidth())
        self.output_label.setSizePolicy(sizePolicy)
        self.output_label.setMinimumSize(QtCore.QSize(750, 75))
        self.output_label.setMaximumSize(QtCore.QSize(750, 75))
        self.output_label.setObjectName("output_label")
        self.horizontalLayout_2.addWidget(self.output_label)
        
        spacerItem8 = QtWidgets.QSpacerItem(277, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem8)
        self.verticalLayout_3.addWidget(self.output_top_frame)
        self.output_text_top_frame = QtWidgets.QFrame(self.top_frame)
        self.output_text_top_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.output_text_top_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.output_text_top_frame.setObjectName("output_text_top_frame")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.output_text_top_frame)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        spacerItem7 = QtWidgets.QSpacerItem(277, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem7)
        self.output_text_line_edit = QtWidgets.QLineEdit(self.output_text_top_frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.output_text_line_edit.sizePolicy().hasHeightForWidth())
        self.output_text_line_edit.setSizePolicy(sizePolicy)
        self.output_text_line_edit.setMinimumSize(QtCore.QSize(750, 75))
        self.output_text_line_edit.setMaximumSize(QtCore.QSize(750, 75))
        self.output_text_line_edit.setObjectName("output_text_line_edit")
        self.horizontalLayout_2.addWidget(self.output_text_line_edit)
        spacerItem8 = QtWidgets.QSpacerItem(277, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem8)
        self.verticalLayout_3.addWidget(self.output_text_top_frame)
        self.top_layout.addWidget(self.top_frame)

        # Color Selector
        self.color_top_frame = QtWidgets.QFrame(text_editor)
        self.color_top_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.color_top_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.color_top_frame.setObjectName("color_top_frame")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.color_top_frame)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        spacerItem9 = QtWidgets.QSpacerItem(260, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem9)
        self.color_picker = QtWidgets.QFrame(self.color_top_frame)
        self.color_picker.setMinimumSize(QtCore.QSize(240, 0))
        self.color_picker.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.color_picker.setFrameShadow(QtWidgets.QFrame.Raised)
        self.color_picker.setObjectName("color_picker")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.color_picker)
        self.verticalLayout_2.setContentsMargins(-1, 6, 6, 6)
        self.verticalLayout_2.setSpacing(4)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.current_color_label = QtWidgets.QLabel(self.color_picker)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.current_color_label.sizePolicy().hasHeightForWidth())
        self.current_color_label.setSizePolicy(sizePolicy)
        self.current_color_label.setMinimumSize(QtCore.QSize(0, 80))
        self.current_color_label.setStyleSheet("background-color: rgb(255, 0, 0);")
        self.current_color_label.setAlignment(QtCore.Qt.AlignCenter)
        self.current_color_label.setObjectName("current_color_label")
        self.verticalLayout_2.addWidget(self.current_color_label)
        self.red_slider_top_frame = QtWidgets.QFrame(self.color_picker)
        self.red_slider_top_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.red_slider_top_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.red_slider_top_frame.setObjectName("red_slider_top_frame")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.red_slider_top_frame)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.red_slider = QtWidgets.QSlider(self.red_slider_top_frame)
        self.red_slider.setMinimumSize(QtCore.QSize(750, 40))
        self.red_slider.setMaximumSize(QtCore.QSize(750, 40))
        self.red_slider.setMaximum(15)
        self.red_slider.setOrientation(QtCore.Qt.Horizontal)
        self.red_slider.setInvertedAppearance(False)
        self.red_slider.setInvertedControls(True)
        self.red_slider.setObjectName("red_slider")
        self.horizontalLayout_4.addWidget(self.red_slider)
        self.red_line_edit = QtWidgets.QLineEdit(self.red_slider_top_frame)
        self.red_line_edit.setMinimumSize(QtCore.QSize(80, 55))
        self.red_line_edit.setMaximumSize(QtCore.QSize(80, 55))
        self.red_line_edit.setObjectName("red_line_edit")
        font = QtGui.QFont()
        font.setPointSize(20)
        self.red_line_edit.setFont(font)
        self.red_line_edit.setAlignment(QtCore.Qt.AlignCenter)
        self.horizontalLayout_4.addWidget(self.red_line_edit)
        self.verticalLayout_2.addWidget(self.red_slider_top_frame)
        self.green_slider_top_frame = QtWidgets.QFrame(self.color_picker)
        self.green_slider_top_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.green_slider_top_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.green_slider_top_frame.setObjectName("green_slider_top_frame")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.green_slider_top_frame)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.green_slider = QtWidgets.QSlider(self.green_slider_top_frame)
        self.green_slider.setMinimumSize(QtCore.QSize(750, 40))
        self.green_slider.setMaximumSize(QtCore.QSize(750, 40))
        self.green_slider.setMaximum(15)
        self.green_slider.setOrientation(QtCore.Qt.Horizontal)
        self.green_slider.setObjectName("green_slider")
        self.horizontalLayout_5.addWidget(self.green_slider)
        self.green_line_edit = QtWidgets.QLineEdit(self.green_slider_top_frame)
        self.green_line_edit.setMinimumSize(QtCore.QSize(80, 55))
        self.green_line_edit.setMaximumSize(QtCore.QSize(80, 55))
        self.green_line_edit.setObjectName("green_line_edit")
        font = QtGui.QFont()
        font.setPointSize(20)
        self.green_line_edit.setFont(font)
        self.green_line_edit.setAlignment(QtCore.Qt.AlignCenter)
        self.horizontalLayout_5.addWidget(self.green_line_edit)
        self.verticalLayout_2.addWidget(self.green_slider_top_frame)
        self.blue_slider_top_frame = QtWidgets.QFrame(self.color_picker)
        self.blue_slider_top_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.blue_slider_top_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.blue_slider_top_frame.setObjectName("blue_slider_top_frame")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout(self.blue_slider_top_frame)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.blue_slider = QtWidgets.QSlider(self.blue_slider_top_frame)
        self.blue_slider.setMinimumSize(QtCore.QSize(750, 40))
        self.blue_slider.setMaximumSize(QtCore.QSize(750, 40))
        self.blue_slider.setMaximum(15)
        self.blue_slider.setOrientation(QtCore.Qt.Horizontal)
        self.blue_slider.setObjectName("blue_slider")
        self.horizontalLayout_6.addWidget(self.blue_slider)
        self.blue_line_edit = QtWidgets.QLineEdit(self.blue_slider_top_frame)
        self.blue_line_edit.setMinimumSize(QtCore.QSize(80, 55))
        self.blue_line_edit.setMaximumSize(QtCore.QSize(80, 55))
        self.blue_line_edit.setObjectName("blue_line_edit")
        font = QtGui.QFont()
        font.setPointSize(20)
        self.blue_line_edit.setFont(font)
        self.blue_line_edit.setAlignment(QtCore.Qt.AlignCenter)
        self.horizontalLayout_6.addWidget(self.blue_line_edit)
        self.verticalLayout_2.addWidget(self.blue_slider_top_frame)
        self.horizontalLayout_3.addWidget(self.color_picker)
        spacerItem10 = QtWidgets.QSpacerItem(261, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem10)
        self.top_layout.addWidget(self.color_top_frame)
        spacerItem11 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.top_layout.addItem(spacerItem11)

        self.retranslateUi(text_editor)
        QtCore.QMetaObject.connectSlotsByName(text_editor)

    def retranslateUi(self, text_editor):
        _translate = QtCore.QCoreApplication.translate
        text_editor.setWindowTitle(_translate("text_editor", "Form"))
        self.title.setText(_translate("text_editor", "Text Editor"))
        self.output_label.setText(_translate("text_editor", "< Output test >"))
        self.current_color_label.setText(_translate("text_editor", "Current Color"))


    @staticmethod
    def main():
        import sys
        app = QtWidgets.QApplication(sys.argv)
        text_edit = QtWidgets.QWidget()
        ui_text_edit = Ui_text_editor()
        ui_text_edit.setupUi(text_edit)
        text_edit.show()
        sys.exit(app.exec_())


if __name__ == '__main__':
    Ui_text_editor.main()
# TODO: Find font for output_label to be like TM Font
# TODO: Add Button to apply current change

# TODO: Connect sliders with line edits
# TODO: Connect Hex color to current color


# TODO: Stupid Formating....
