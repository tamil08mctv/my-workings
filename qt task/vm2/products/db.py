import sqlite3

def create_database():
    conn = sqlite3.connect('products.db')
    cursor = conn.cursor()

    
    cursor.execute('''
        CREATE TABLE  products (
            id INTEGER PRIMARY KEY,
            name TEXT NOT NULL,
            category TEXT NOT NULL,
            price REAL NOT NULL,
            stock INTEGER NOT NULL,
            picture TEXT NOT NULL
        )
    ''')

   
    sample_data = [
        ('Oreo', 'Biscuits', 2.5, 100,'products\\oreo.jpg'),
        ('Bourbon', 'Biscuits', 3.0, 50,'products\\bourbon.jpg'),
        ('KitKat', 'Chocolates', 1.5, 200,'products\\kitkat.jpg'),
        ('Snickers', 'Chocolates', 2.0, 150,'products\\snickers.jpg'),
        ('Coca Cola', 'Drinks', 1.0, 300,'products\\coca cola.jpg'),
        ('Pepsi', 'Drinks', 1.0, 250,'products\\pepsi.jpg'),
    ]

    cursor.executemany('''
        INSERT INTO products (name, category, price, stock,picture)
        VALUES (?, ?, ?, ?,?)
    ''', sample_data)

    conn.commit()
    conn.close()


create_database()
