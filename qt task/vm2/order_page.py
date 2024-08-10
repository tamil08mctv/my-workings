from PyQt6 import QtCore, QtGui, QtWidgets
import sqlite3
from operations import btn_connections, update_total_amt

class Ui_Order(object):
    def setupUi(self, order_page):
        order_page.setObjectName("Form")
        order_page.resize(1600, 800)
        order_page.setStyleSheet("background-color: rgb(135, 135, 135);")
        order_page.setWindowTitle("Order Page")

        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        order_page.setLayout(self.verticalLayout)

        self.fr_title = QtWidgets.QFrame()
        self.fr_title.setMinimumSize(QtCore.QSize(0, 40))
        self.fr_title.setMaximumSize(QtCore.QSize(16777214, 16777215))
        self.fr_title.setLayoutDirection(QtCore.Qt.LayoutDirection.LeftToRight)
        self.fr_title.setObjectName("fr_title")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.fr_title.setLayout(self.verticalLayout_2)
        self.lb_title = QtWidgets.QLabel()
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(14)
        font.setBold(True)
        self.lb_title.setFont(font)
        self.lb_title.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.lb_title.setObjectName("lb_title")
        self.verticalLayout_2.addWidget(self.lb_title)
        self.verticalLayout.addWidget(self.fr_title)

        self.scrollArea = QtWidgets.QScrollArea()
        self.scrollArea.setMinimumSize(QtCore.QSize(850, 550))
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 868, 585))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.scrollAreaWidgetContents.setLayout(self.verticalLayout_3)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.verticalLayout.addWidget(self.scrollArea)

        self.fr_footer = QtWidgets.QFrame()
        self.fr_footer.setMinimumSize(QtCore.QSize(0, 45))
        self.fr_footer.setMaximumSize(QtCore.QSize(16777215, 40))
        self.fr_footer.setObjectName("fr_footer")
        self.horizontalLayout_footer = QtWidgets.QHBoxLayout()
        self.horizontalLayout_footer.setObjectName("horizontalLayout_footer")
        self.fr_footer.setLayout(self.horizontalLayout_footer)

        self.btn_back = QtWidgets.QPushButton()
        self.btn_back.setMinimumSize(QtCore.QSize(100, 35))
        self.btn_back.setStyleSheet("font: 75 14pt 'Times New Roman'; background-color: rgb(255, 0, 0); border-radius: 10px;")
        self.btn_back.setObjectName("btn_back")
        self.btn_back.setText("Back")
        self.horizontalLayout_footer.addWidget(self.btn_back)

        self.horizontalSpacer_left = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout_footer.addItem(self.horizontalSpacer_left)

        self.lb_total_amt = QtWidgets.QLabel()
        self.lb_total_amt.setMinimumSize(QtCore.QSize(100, 35))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        font.setBold(True)
        self.lb_total_amt.setFont(font)
        self.lb_total_amt.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.lb_total_amt.setObjectName("lb_total_amount")
        self.horizontalLayout_footer.addWidget(self.lb_total_amt)

        self.horizontalSpacer_right = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout_footer.addItem(self.horizontalSpacer_right)

        self.btn_next = QtWidgets.QPushButton()
        self.btn_next.setMinimumSize(QtCore.QSize(100, 35))
        self.btn_next.setStyleSheet("font: 75 14pt 'Times New Roman'; background-color: rgb(255, 0, 0); border-radius: 10px;")
        self.btn_next.setObjectName("btn_next")
        self.btn_next.setText("View Order")
        self.horizontalLayout_footer.addWidget(self.btn_next)

        self.verticalLayout.addWidget(self.fr_footer)

        self.lb_title.setText("Order Page")
        self.lb_total_amt.setText("Total Amount: Rs 0.00")
        QtCore.QMetaObject.connectSlotsByName(order_page)

        self.selected_products = [] 
        self.retrieve_data()

    def retrieve_data(self):
        conn = sqlite3.connect('products.db')
        cursor = conn.cursor()

        cursor.execute("SELECT name, category, price, stock, picture FROM products")
        products = cursor.fetchall()

        conn.close()
        self.display_products(products)

    def display_products(self, products):
        categories = {}
        for product in products:
            name, category, price, stock, picture = product
            if category not in categories:
                categories[category] = []
            categories[category].append((name, price, stock, picture))

        for category, products in categories.items():
            fr_category = QtWidgets.QFrame(parent=self.scrollAreaWidgetContents)
            fr_category.setMinimumSize(QtCore.QSize(0, 40))
            fr_category.setMaximumSize(QtCore.QSize(16777215, 30))
            fr_category.setObjectName("fr_category")
            horizontalLayout = QtWidgets.QHBoxLayout(fr_category)
            horizontalLayout.setObjectName("horizontalLayout")

            lb_category = QtWidgets.QLabel(parent=fr_category)
            lb_category.setMinimumSize(QtCore.QSize(0, 30))
            lb_category.setMaximumSize(QtCore.QSize(16777215, 30))
            font = QtGui.QFont()
            font.setFamily("Times New Roman")
            font.setPointSize(16)
            font.setBold(True)
            lb_category.setFont(font)
            lb_category.setObjectName("lb_category")
            lb_category.setText(category)
            horizontalLayout.addWidget(lb_category)
            self.verticalLayout_3.addWidget(fr_category)

            fr_products = QtWidgets.QWidget(parent=self.scrollAreaWidgetContents)
            fr_products.setStyleSheet("background-color: rgb(180, 255, 130); border-radius:20%")
            fr_products.setObjectName("fr_products")
            horizontalLayout_products = QtWidgets.QHBoxLayout(fr_products)
            horizontalLayout_products.setSpacing(10)

            for index, (name, price, stock, picture) in enumerate(products):
                if index % 4 == 0 and index != 0:
                    self.verticalLayout_3.addWidget(fr_products)
                    fr_products = QtWidgets.QWidget(parent=self.scrollAreaWidgetContents)
                    fr_products.setStyleSheet("background-color: rgb(180, 255, 130); border-radius:20%")
                    fr_products.setObjectName("fr_products")
                    horizontalLayout_products = QtWidgets.QHBoxLayout(fr_products)
                    horizontalLayout_products.setSpacing(10)

                fr_product = QtWidgets.QFrame(parent=fr_products)
                fr_product.setMinimumSize(QtCore.QSize(220, 300))
                fr_product.setMaximumSize(QtCore.QSize(220, 300))
                fr_product.setStyleSheet("background-color: rgb(255, 85, 0);")
                fr_product.setObjectName("fr_product")

                lb_pic = QtWidgets.QLabel(parent=fr_product)
                lb_pic.setGeometry(QtCore.QRect(10, 10, 200, 200))
                lb_pic.setMaximumSize(QtCore.QSize(200, 200))
                pixmap = QtGui.QPixmap(picture)
                pic_rad = QtGui.QBitmap(pixmap.size())
                pic_rad.fill(QtCore.Qt.GlobalColor.white)
                painter = QtGui.QPainter(pic_rad)
                painter.setBrush(QtCore.Qt.GlobalColor.black)
                radius = 10
                painter.drawRoundedRect(0, 0, pixmap.width(), pixmap.height(), radius, radius)
                painter.end()
                pixmap.setMask(pic_rad)
                lb_pic.setPixmap(pixmap)
                lb_pic.setScaledContents(True)
                lb_pic.setObjectName("lb_pic")

                lb_name = QtWidgets.QLabel(parent=fr_product)
                lb_name.setGeometry(QtCore.QRect(40, 215, 140, 30))
                font = QtGui.QFont()
                font.setFamily("Times New Roman")
                font.setPointSize(18)
                font.setBold(True)
                lb_name.setFont(font)
                lb_name.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
                lb_name.setText(name)
                lb_name.setObjectName("lb_name")

                lb_price = QtWidgets.QLabel(parent=fr_product)
                lb_price.setGeometry(QtCore.QRect(10, 250, 91, 35))
                font = QtGui.QFont()
                font.setFamily("Times New Roman")
                font.setPointSize(16)
                font.setBold(True)
                lb_price.setFont(font)
                lb_price.setStyleSheet("background-color: rgb(170, 255, 255); border-radius:15px;")
                lb_price.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
                lb_price.setText(f"Rs {price:.2f}")
                lb_price.setObjectName("lb_price")

                btn_add = QtWidgets.QPushButton(parent=fr_product)
                btn_add.setGeometry(QtCore.QRect(110, 250, 100, 35))
                btn_add.setStyleSheet("font: 75 14pt 'Times New Roman'; background-color: rgb(255, 0, 0); border-radius: 10px;")
                btn_add.setObjectName("btn_add")
                btn_add.setText("Add")

                btn_low = QtWidgets.QPushButton(parent=fr_product)
                btn_low.setGeometry(QtCore.QRect(110, 250, 30, 35))
                btn_low.setMinimumSize(QtCore.QSize(0, 35))
                btn_low.setMaximumSize(QtCore.QSize(16777215, 35))
                font = QtGui.QFont()
                font.setFamily("Times New Roman")
                font.setPointSize(24)
                font.setBold(True)
                btn_low.setFont(font)
                btn_low.setStyleSheet("background-color: rgb(255, 255, 0);")
                btn_low.setIconSize(QtCore.QSize(16, 16))
                btn_low.setObjectName("btn_low")
                btn_low.setText("-")

                btn_high = QtWidgets.QPushButton(parent=fr_product)
                btn_high.setGeometry(QtCore.QRect(180, 250, 30, 35))
                btn_high.setMinimumSize(QtCore.QSize(0, 35))
                btn_high.setMaximumSize(QtCore.QSize(16777215, 35))
                font = QtGui.QFont()
                font.setFamily("Times New Roman")
                font.setPointSize(24)
                font.setBold(True)
                btn_high.setFont(font)
                btn_high.setStyleSheet("background-color: rgb(0, 255, 0);")
                btn_high.setIconSize(QtCore.QSize(16, 16))
                btn_high.setObjectName("btn_high")
                btn_high.setText("+")

                lb_quan = QtWidgets.QLabel(parent=fr_product)
                lb_quan.setGeometry(QtCore.QRect(140, 250, 40, 35))
                lb_quan.setMinimumSize(QtCore.QSize(40, 35))
                lb_quan.setMaximumSize(QtCore.QSize(40, 35))
                lb_quan.setStyleSheet("font: 75 16pt 'Times New Roman'; background-color: rgb(255, 170, 255);")
                lb_quan.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
                lb_quan.setObjectName("lb_quan")
                lb_quan.setText("1")

                btn_low.hide()
                btn_high.hide()
                lb_quan.hide()

                btn_connections(btn_add, btn_low, btn_high, lb_quan, self, name, price, picture, fr_product)

                horizontalLayout_products.addWidget(fr_product)

            if horizontalLayout_products.count() > 0:
                self.verticalLayout_3.addWidget(fr_products)

            spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
            self.verticalLayout_3.addItem(spacerItem)

        update_total_amt(self)

    def update_display(self):
        self.scrollAreaWidgetContents.setLayout(None)  
        self.verticalLayout_3.setStretch(0, 0)
        self.verticalLayout_3.setStretch(1, 0)
        self.retrieve_data()
