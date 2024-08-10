from PyQt6 import QtWidgets
from order_page import Ui_Order
from confirm_order import Ui_Form
from pay_options_ui import Ui_wg_payment

class MainWindow(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Order()
        self.ui.setupUi(self)
        self.ui.btn_next.clicked.connect(self.open_viewOrder)

    def open_viewOrder(self):
        self.view_order = ViewOrder(self, self.ui.selected_products)
        self.view_order.show()
        self.hide()

    def update_selected_products(self, updated_products):
        self.ui.selected_products = updated_products
       
class ViewOrder(QtWidgets.QWidget):
    def __init__(self, main_window, selected_products):
        super().__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.ui.btn_back.clicked.connect(self.backToOrder)
        self.main_window = main_window
        self.selected_products = selected_products
        self.ui.populateOrderList(self.selected_products)
        self.ui.btn_grab.clicked.connect(self.open_payoptions)


    def open_payoptions(self):
        self.pay_options = PayOptions(self)
        self.pay_options.show()
        self.hide()

    def backToOrder(self):
        # Pass updated products back to main window
        self.main_window.update_selected_products(self.selected_products)
        self.hide() 
        self.main_window.show()


class PayOptions(QtWidgets.QWidget):
    def __init__(self, view_order):
        super().__init__()
        self.ui = Ui_wg_payment()
        self.ui.setupUi(self)
        self.view_order = view_order
        self.ui.btn_back.clicked.connect(self.backToViewOrder)

    def backToViewOrder(self):
        self.hide()
        self.view_order.show()


app = QtWidgets.QApplication([])
window = MainWindow()   
window.show()
app.exec()
