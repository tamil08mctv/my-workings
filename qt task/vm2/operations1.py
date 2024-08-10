from PyQt6.QtWidgets import QPushButton, QLabel, QWidget, QVBoxLayout, QScrollArea
from PyQt6 import QtWidgets

def confirm_order(btn_low: QPushButton, btn_high: QPushButton, lb_quan: QLabel, 
                  lb_amt: QLabel, lb_price: QLabel, self, name: str, price: float):
    
    def update_quantity():
        quantity = int(lb_quan.text())
        if quantity > 0:
            quantity -= 1
        lb_quan.setText(str(quantity))
        update_amount(quantity)

    def increase_quantity():
        quantity = int(lb_quan.text())
        quantity += 1
        lb_quan.setText(str(quantity))
        update_amount(quantity)
    
    def update_amount(quantity):
        lb_amt.setText(f"Rs {price * quantity:.2f}")

        # Update or remove product in the list
        for product in self.selected_products:
            if product["name"] == name:
                if quantity == 0:
                    self.selected_products.remove(product)
                    remove_product_ui(name)
                else:
                    product["quantity"] = quantity
                    product["total_amount"] = price * quantity
                update_total_amount()
                break
        else:
            if quantity > 0:
                self.selected_products.append({
                    "name": name,
                    "quantity": quantity,
                    "price": price,
                    "total_amount": price * quantity
                })
                update_total_amount()

    def update_total_amount():
        total_amount = sum(product["total_amount"] for product in self.selected_products)
        self.lb_tot_amt.setText(f"Total Amount: Rs {total_amount:.2f}")

    def remove_product_ui(name):
        # Iterate through the widgets in the scroll area and remove the matching one
        for i in range(self.sc_contents.layout().count()):
            widget = self.sc_contents.layout().itemAt(i).widget()
            if widget and isinstance(widget, QtWidgets.QFrame) and widget.objectName() == f"product_{name}":
                widget.deleteLater()
                break

    btn_low.clicked.connect(update_quantity)
    btn_high.clicked.connect(increase_quantity)
