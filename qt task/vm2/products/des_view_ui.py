# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'des_view.ui'
##
## Created by: Qt User Interface Compiler version 6.7.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QFrame, QHBoxLayout, QLabel,
    QPushButton, QScrollArea, QSizePolicy, QSpacerItem,
    QVBoxLayout, QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(1026, 712)
        Form.setStyleSheet(u"background-color: rgb(214, 214, 214);")
        self.verticalLayout_3 = QVBoxLayout(Form)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.fr_window = QFrame(Form)
        self.fr_window.setObjectName(u"fr_window")
        self.fr_window.setFrameShape(QFrame.StyledPanel)
        self.fr_window.setFrameShadow(QFrame.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.fr_window)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.fr_title = QFrame(self.fr_window)
        self.fr_title.setObjectName(u"fr_title")
        self.fr_title.setMaximumSize(QSize(16777215, 40))
        self.fr_title.setFrameShape(QFrame.StyledPanel)
        self.fr_title.setFrameShadow(QFrame.Raised)
        self.verticalLayout = QVBoxLayout(self.fr_title)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.lb_title = QLabel(self.fr_title)
        self.lb_title.setObjectName(u"lb_title")
        font = QFont()
        font.setFamilies([u"Times New Roman"])
        font.setPointSize(16)
        font.setBold(True)
        self.lb_title.setFont(font)

        self.verticalLayout.addWidget(self.lb_title, 0, Qt.AlignHCenter|Qt.AlignVCenter)


        self.verticalLayout_4.addWidget(self.fr_title)

        self.sc_list = QScrollArea(self.fr_window)
        self.sc_list.setObjectName(u"sc_list")
        self.sc_list.setWidgetResizable(True)
        self.sc_contents = QWidget()
        self.sc_contents.setObjectName(u"sc_contents")
        self.sc_contents.setGeometry(QRect(0, 0, 986, 570))
        self.verticalLayout_2 = QVBoxLayout(self.sc_contents)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.fr_list = QFrame(self.sc_contents)
        self.fr_list.setObjectName(u"fr_list")
        self.fr_list.setMaximumSize(QSize(16777215, 260))
        self.fr_list.setFrameShape(QFrame.StyledPanel)
        self.fr_list.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.fr_list)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.left_space = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_4.addItem(self.left_space)

        self.fr_product = QFrame(self.fr_list)
        self.fr_product.setObjectName(u"fr_product")
        self.fr_product.setMinimumSize(QSize(750, 240))
        self.fr_product.setMaximumSize(QSize(16777215, 250))
        self.fr_product.setStyleSheet(u"background-color: rgb(207, 255, 227);\n"
"border-radius:20%")
        self.fr_product.setFrameShape(QFrame.StyledPanel)
        self.fr_product.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.fr_product)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.fr_pic = QFrame(self.fr_product)
        self.fr_pic.setObjectName(u"fr_pic")
        self.fr_pic.setMaximumSize(QSize(220, 220))
        self.fr_pic.setStyleSheet(u"background-color: rgb(134, 255, 168);")
        self.fr_pic.setFrameShape(QFrame.StyledPanel)
        self.fr_pic.setFrameShadow(QFrame.Raised)
        self.lb_pic = QLabel(self.fr_pic)
        self.lb_pic.setObjectName(u"lb_pic")
        self.lb_pic.setGeometry(QRect(10, 10, 200, 200))
        self.lb_pic.setMinimumSize(QSize(200, 200))
        self.lb_pic.setMaximumSize(QSize(200, 200))
        self.lb_pic.setFont(font)
        self.lb_pic.setPixmap(QPixmap(u"../vm/products/kitkat.jpg"))
        self.lb_pic.setScaledContents(True)
        self.lb_pic.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_2.addWidget(self.fr_pic)

        self.fr_price = QFrame(self.fr_product)
        self.fr_price.setObjectName(u"fr_price")
        self.fr_price.setMinimumSize(QSize(250, 210))
        self.fr_price.setMaximumSize(QSize(250, 210))
        self.fr_price.setFrameShape(QFrame.StyledPanel)
        self.fr_price.setFrameShadow(QFrame.Raised)
        self.lb_name = QLabel(self.fr_price)
        self.lb_name.setObjectName(u"lb_name")
        self.lb_name.setGeometry(QRect(50, 40, 161, 51))
        self.lb_name.setFont(font)
        self.lb_name.setAlignment(Qt.AlignCenter)
        self.lb_price = QLabel(self.fr_price)
        self.lb_price.setObjectName(u"lb_price")
        self.lb_price.setGeometry(QRect(50, 120, 161, 51))
        self.lb_price.setFont(font)
        self.lb_price.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_2.addWidget(self.fr_price)

        self.fr_amt = QFrame(self.fr_product)
        self.fr_amt.setObjectName(u"fr_amt")
        self.fr_amt.setMaximumSize(QSize(220, 250))
        self.fr_amt.setFrameShape(QFrame.StyledPanel)
        self.fr_amt.setFrameShadow(QFrame.Raised)
        self.btn_high = QPushButton(self.fr_amt)
        self.btn_high.setObjectName(u"btn_high")
        self.btn_high.setGeometry(QRect(140, 60, 31, 35))
        self.btn_high.setMinimumSize(QSize(0, 35))
        font1 = QFont()
        font1.setFamilies([u"Times New Roman"])
        font1.setPointSize(22)
        font1.setBold(True)
        self.btn_high.setFont(font1)
        self.btn_high.setStyleSheet(u"background-color: rgb(0, 255, 0);")
        self.btn_high.setIconSize(QSize(16, 16))
        self.btnlow = QPushButton(self.fr_amt)
        self.btnlow.setObjectName(u"btnlow")
        self.btnlow.setGeometry(QRect(60, 60, 31, 35))
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btnlow.sizePolicy().hasHeightForWidth())
        self.btnlow.setSizePolicy(sizePolicy)
        self.btnlow.setMinimumSize(QSize(0, 35))
        font2 = QFont()
        font2.setFamilies([u"Times New Roman"])
        font2.setPointSize(28)
        font2.setBold(True)
        self.btnlow.setFont(font2)
        self.btnlow.setStyleSheet(u"background-color: rgb(255, 255, 0);")
        self.btnlow.setIconSize(QSize(16, 14))
        self.lb_quan = QLabel(self.fr_amt)
        self.lb_quan.setObjectName(u"lb_quan")
        self.lb_quan.setGeometry(QRect(90, 60, 51, 35))
        self.lb_quan.setMinimumSize(QSize(0, 35))
        font3 = QFont()
        font3.setPointSize(12)
        font3.setBold(True)
        self.lb_quan.setFont(font3)
        self.lb_quan.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.lb_quan.setAlignment(Qt.AlignCenter)
        self.lb_amt = QLabel(self.fr_amt)
        self.lb_amt.setObjectName(u"lb_amt")
        self.lb_amt.setGeometry(QRect(40, 120, 150, 61))
        self.lb_amt.setMinimumSize(QSize(150, 0))
        self.lb_amt.setMaximumSize(QSize(150, 16777215))
        self.lb_amt.setFont(font)
        self.lb_amt.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_2.addWidget(self.fr_amt)


        self.horizontalLayout_4.addWidget(self.fr_product)

        self.right_space = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_4.addItem(self.right_space)


        self.verticalLayout_2.addWidget(self.fr_list, 0, Qt.AlignTop)

        self.sc_list.setWidget(self.sc_contents)

        self.verticalLayout_4.addWidget(self.sc_list)

        self.fr_footer = QFrame(self.fr_window)
        self.fr_footer.setObjectName(u"fr_footer")
        self.fr_footer.setMinimumSize(QSize(0, 40))
        self.fr_footer.setFrameShape(QFrame.StyledPanel)
        self.fr_footer.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.fr_footer)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.btn_back = QPushButton(self.fr_footer)
        self.btn_back.setObjectName(u"btn_back")
        self.btn_back.setMinimumSize(QSize(0, 30))
        self.btn_back.setMaximumSize(QSize(100, 60))
        font4 = QFont()
        font4.setFamilies([u"Times New Roman"])
        font4.setPointSize(14)
        font4.setBold(True)
        self.btn_back.setFont(font4)
        self.btn_back.setStyleSheet(u"background-color: rgb(255, 0, 0);\n"
"border-radius:10%")

        self.horizontalLayout_3.addWidget(self.btn_back)

        self.lb_tot_amt = QLabel(self.fr_footer)
        self.lb_tot_amt.setObjectName(u"lb_tot_amt")
        font5 = QFont()
        font5.setPointSize(14)
        self.lb_tot_amt.setFont(font5)

        self.horizontalLayout_3.addWidget(self.lb_tot_amt, 0, Qt.AlignHCenter)

        self.pushButton_2 = QPushButton(self.fr_footer)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setMinimumSize(QSize(100, 0))
        self.pushButton_2.setMaximumSize(QSize(120, 40))
        self.pushButton_2.setFont(font4)
        self.pushButton_2.setStyleSheet(u"background-color: rgb(71, 255, 117);\n"
"border-radius:10%")

        self.horizontalLayout_3.addWidget(self.pushButton_2)


        self.verticalLayout_4.addWidget(self.fr_footer, 0, Qt.AlignTop)


        self.verticalLayout_3.addWidget(self.fr_window)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.lb_title.setText(QCoreApplication.translate("Form", u"View Order", None))
        self.lb_pic.setText("")
        self.lb_name.setText(QCoreApplication.translate("Form", u"Kitkat", None))
        self.lb_price.setText(QCoreApplication.translate("Form", u"Rs. 20", None))
        self.btn_high.setText(QCoreApplication.translate("Form", u"+", None))
        self.btnlow.setText(QCoreApplication.translate("Form", u"-", None))
        self.lb_quan.setText(QCoreApplication.translate("Form", u"0", None))
        self.lb_amt.setText(QCoreApplication.translate("Form", u"Amt : Rs. 0", None))
        self.btn_back.setText(QCoreApplication.translate("Form", u"Back", None))
        self.lb_tot_amt.setText(QCoreApplication.translate("Form", u"Total Amount: Rs. 0", None))
        self.pushButton_2.setText(QCoreApplication.translate("Form", u"Grab Order", None))
    # retranslateUi

