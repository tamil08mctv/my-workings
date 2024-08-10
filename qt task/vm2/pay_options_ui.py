from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_wg_payment(object):
    def setupUi(self, wg_payment):
        wg_payment.setObjectName("wg_payment")
        wg_payment.resize(1600, 800)
        wg_payment.setStyleSheet("background-color: rgb(121, 121, 121);")
        self.verticalLayout = QtWidgets.QVBoxLayout(wg_payment)
        self.verticalLayout.setObjectName("verticalLayout")
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        self.verticalLayout.addItem(spacerItem)
        self.fr_windoew = QtWidgets.QFrame(parent=wg_payment)
        self.fr_windoew.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.fr_windoew.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.fr_windoew.setObjectName("fr_windoew")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.fr_windoew)
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.fr_contents = QtWidgets.QFrame(parent=self.fr_windoew)
        self.fr_contents.setMinimumSize(QtCore.QSize(750, 500))
        self.fr_contents.setWhatsThis("")
        self.fr_contents.setStyleSheet("background-color: rgb(203, 203, 203);\n"
"border-radius:20px;")
        self.fr_contents.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.fr_contents.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.fr_contents.setMidLineWidth(0)
        self.fr_contents.setObjectName("fr_contents")
        self.lb_title = QtWidgets.QLabel(parent=self.fr_contents)
        self.lb_title.setGeometry(QtCore.QRect(280, 40, 191, 41))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(14)
        font.setBold(True)
        
        self.lb_title.setFont(font)
        self.lb_title.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.lb_title.setObjectName("lb_title")
        self.fr_cash = QtWidgets.QFrame(parent=self.fr_contents)
        self.fr_cash.setGeometry(QtCore.QRect(70, 130, 220, 300))
        self.fr_cash.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.fr_cash.setFocusPolicy(QtCore.Qt.FocusPolicy.TabFocus)
        self.fr_cash.setContextMenuPolicy(QtCore.Qt.ContextMenuPolicy.ActionsContextMenu)
        self.fr_cash.setStyleSheet("background-color: rgb(185, 192, 200);\n"
"border-radius:20px;")
        self.fr_cash.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.fr_cash.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.fr_cash.setObjectName("fr_cash")
        self.lb_cash = QtWidgets.QLabel(parent=self.fr_cash)
        self.lb_cash.setGeometry(QtCore.QRect(10, 230, 200, 40))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(16)
        font.setBold(True)
       

        self.lb_cash.setFont(font)
        self.lb_cash.setStyleSheet("background-color: rgb(185, 192, 200);\n"
"border-radius:20px;")        
        self.lb_cash.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.lb_cash.setObjectName("lb_cash")


        self.lb_pic_cash = QtWidgets.QLabel(parent=self.fr_cash)
        self.lb_pic_cash.setGeometry(QtCore.QRect(10, 10, 200, 200))
        self.lb_pic_cash.setMinimumSize(QtCore.QSize(200, 200))
        self.lb_pic_cash.setMaximumSize(QtCore.QSize(150, 150))
        self.lb_pic_cash.setFrameShape(QtWidgets.QFrame.Shape.Panel)
        self.lb_pic_cash.setText("")
        pixmap =QtGui.QPixmap("../../VM/Siva/cash.png")

        pic_rad = QtGui.QBitmap(pixmap.size())
        pic_rad.fill(QtCore.Qt.GlobalColor.white)
        painter = QtGui.QPainter(pic_rad)
        painter.setBrush(QtCore.Qt.GlobalColor.black)
        radius = 10
        painter.drawRoundedRect(0, 0, pixmap.width(), pixmap.height(), radius, radius)
        painter.end()
        pixmap.setMask(pic_rad)
        self.lb_pic_cash.setPixmap(pixmap)
        self.lb_pic_cash.setScaledContents(True)
        self.lb_pic_cash.setObjectName("lb_pic")


        self.fr_upi = QtWidgets.QFrame(parent=self.fr_contents)
        self.fr_upi.setGeometry(QtCore.QRect(460, 130, 220, 300))
        self.fr_upi.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.fr_upi.setStyleSheet("background-color: rgb(185, 192, 200);\n"
"border-radius:20px;")
        self.fr_upi.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.fr_upi.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.fr_upi.setObjectName("fr_upi")


        self.lb_pic_upi = QtWidgets.QLabel(parent=self.fr_upi)
        self.lb_pic_upi.setGeometry(QtCore.QRect(10, 10, 200, 200))
        self.lb_pic_upi.setMinimumSize(QtCore.QSize(200, 200))
        self.lb_pic_upi.setMaximumSize(QtCore.QSize(200, 200))
        self.lb_pic_upi.setFrameShape(QtWidgets.QFrame.Shape.Panel)
        self.lb_pic_upi.setText("")
        pixmap = QtGui.QPixmap("../../VM/Siva/online.jpg")

        pic_rad = QtGui.QBitmap(pixmap.size())
        pic_rad.fill(QtCore.Qt.GlobalColor.white)
        painter = QtGui.QPainter(pic_rad)
        painter.setBrush(QtCore.Qt.GlobalColor.black)
        radius = 10
        painter.drawRoundedRect(0, 0, pixmap.width(), pixmap.height(), radius, radius)
        painter.end()
        pixmap.setMask(pic_rad)
        self.lb_pic_upi.setPixmap(pixmap)
        self.lb_pic_upi.setScaledContents(True)
        self.lb_pic_upi.setObjectName("lb_pic")




        self.lb_upi = QtWidgets.QLabel(parent=self.fr_upi)
        self.lb_upi.setGeometry(QtCore.QRect(10, 230, 200, 40))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(16)
        font.setBold(True)
     
        self.lb_upi.setFont(font)
        self.lb_upi.setLineWidth(0)
        self.lb_upi.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.lb_upi.setObjectName("lb_upi")
        self.horizontalLayout.addWidget(self.fr_contents)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout.addItem(spacerItem2)
        self.verticalLayout.addWidget(self.fr_windoew, 0, QtCore.Qt.AlignmentFlag.AlignHCenter)
        spacerItem3 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        self.verticalLayout.addItem(spacerItem3)
        self.fr_btn = QtWidgets.QFrame(parent=wg_payment)
        self.fr_btn.setMinimumSize(QtCore.QSize(0, 50))
        self.fr_btn.setMaximumSize(QtCore.QSize(16777215, 50))
        self.fr_btn.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.fr_btn.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.fr_btn.setObjectName("fr_btn")
        self.btn_back = QtWidgets.QPushButton(parent=self.fr_btn)
        self.btn_back.setGeometry(QtCore.QRect(20, 10, 100, 40))
        self.btn_back.setMinimumSize(QtCore.QSize(100, 40))
        self.btn_back.setMaximumSize(QtCore.QSize(100, 40))
        self.btn_back.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(16)
        font.setBold(True)
       
        self.btn_back.setFont(font)
        self.btn_back.setStyleSheet("background-color: rgb(234, 0, 0);\n"
"border-radius:20px;")
        self.btn_back.setObjectName("btn_back")
        self.verticalLayout.addWidget(self.fr_btn, 0, QtCore.Qt.AlignmentFlag.AlignBottom)

        self.retranslateUi(wg_payment)
        QtCore.QMetaObject.connectSlotsByName(wg_payment)

    def retranslateUi(self, wg_payment):
        _translate = QtCore.QCoreApplication.translate
        wg_payment.setWindowTitle(_translate("wg_payment", "Form"))
        self.lb_title.setText(_translate("wg_payment", "Payment"))
        self.lb_cash.setText(_translate("wg_payment", "Cash Payment"))
        self.lb_upi.setText(_translate("wg_payment", "UPI Payment"))
        self.btn_back.setText(_translate("wg_payment", "Back"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    wg_payment = QtWidgets.QWidget()
    ui = Ui_wg_payment()
    ui.setupUi(wg_payment)
    wg_payment.show()
    sys.exit(app.exec())
