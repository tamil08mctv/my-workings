from PyQt6.QtWidgets import QPushButton, QLabel, QFrame
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QMouseEvent

def btn_connections(btn_add: QPushButton, btn_low: QPushButton, btn_high: QPushButton, lb_quan: QLabel, 
                    self, name: str, price: float, picture: str, fr_product: QFrame):
    btn_add.clicked.connect(lambda: show_controls(btn_add, btn_low, btn_high, lb_quan, self, name, price, picture))
    btn_high.clicked.connect(lambda: high(lb_quan, self, name, price))
    btn_low.clicked.connect(lambda: low(lb_quan, btn_low, btn_high, btn_add, self, name, price))
    
    fr_product.mousePressEvent = lambda event: onclick_product(event, btn_add, btn_low, 
                                            btn_high, lb_quan, self, name, price, picture)

def show_controls(btn_add: QPushButton, btn_low: QPushButton, btn_high: QPushButton, 
                  lb_quan: QLabel, self, name: str, price: float, picture: str):
    if btn_add.isHidden():
        btn_add.show()
        btn_low.hide()
        btn_high.hide()
        lb_quan.hide()
    else:
        btn_add.hide()
        btn_low.show()
        btn_high.show()
        lb_quan.show()
        lb_quan.setText("1")  # Set initial quantity to 1

        # Ensure self.selected_products is a list
        if not hasattr(self, 'selected_products') or not isinstance(self.selected_products, list):
            self.selected_products = []

        # Check if product is already in the list
        product_exists = any(product["name"] == name for product in self.selected_products)
        if not product_exists:
            self.selected_products.append({
                "name": name,
                "price": price,
                "quantity": 1,  # Initial quantity
                "picture": picture,
                "total_amount": price  # Initialize total_amount for this product
            })

        update_total_amt(self)
        print_selected_products(self)

def high(lb_quan: QLabel, self, name: str, price: float):
    quantity = int(lb_quan.text())
    quantity += 1
    lb_quan.setText(str(quantity))
    
    for product in self.selected_products:
        if product["name"] == name:
            product["quantity"] = quantity
            product["total_amount"] = price * quantity
            break
    update_total_amt(self)
    print_selected_products(self)

def low(lb_quan: QLabel, btn_low: QPushButton, btn_high: QPushButton,
        btn_add: QPushButton, self, name: str, price: float):
    quantity = int(lb_quan.text())
    if quantity > 1:
        quantity -= 1
        lb_quan.setText(str(quantity))
        
        for product in self.selected_products:
            if product["name"] == name:
                product["quantity"] = quantity
                product["total_amount"] = price * quantity
                break
    else:
        lb_quan.setText("1")
        btn_low.hide()
        btn_high.hide()
        lb_quan.hide()
        btn_add.show()
        self.selected_products = [product for product in self.selected_products if product["name"] != name]
        
    update_total_amt(self)
    print_selected_products(self)

def update_total_amt(self):
    total_amount = sum(product["total_amount"] for product in self.selected_products)
    self.lb_total_amt.setText(f"Total Amount: Rs {total_amount:.2f}")

def print_selected_products(self):
    print("Selected Products:")
    for product in self.selected_products:
        print(f"Name: {product['name']}, Price: {product['price']}, Quantity: {product['quantity']}, Total Amount: {product['total_amount']}, Picture: {product['picture']}")

def onclick_product(event: QMouseEvent, btn_add: QPushButton, btn_low: QPushButton, btn_high: QPushButton, 
                    lb_quan: QLabel, self, name: str, price: float, picture: str):
    if btn_add.isHidden():
        high(lb_quan, self, name, price)
    else:
        show_controls(btn_add, btn_low, btn_high, lb_quan, self, name, price, picture)
