import sqlite3


def create_connection(db_file):
    conn = None
    try:
        conn = sqlite3.connect(db_file)
    except sqlite3.Error as b:
        print(b)
    return conn


def create_table(conn, sql):
    try:
        cursor = conn.cursor()
        cursor.execute(sql)
    except sqlite3.Error as e:
        print(e)


database = 'hw.db'
sql_create_products_table = '''
CREATE TABLE products (
id INTEGER PRIMARY KEY AUTOINCREMENT,
product_title VARCHAR(200) NOT NULL,
price DOUBLE(10,2) NOT NULL DEFAULT 0.0,
quantity DOUBLE(10) NOT NULL DEFAULT 0
)
'''


def create_products(conn, products):
    try:
        sql = '''INSERT INTO products (product_title, price, quantity) 
        VALUES (?, ?, ?)'''
        cursor = conn.cursor()
        cursor.execute(sql, products)
        conn.commit()
    except sqlite3.Error as e:
        print(e)


def update_quantity(conn, products):
    try:
        sql = '''UPDATE products SET quantity = ? WHERE id = ?'''
        cursor = conn.cursor()
        cursor.execute(sql, products)
        conn.commit()
    except sqlite3.Error as e:
        print(e)


def update_price(conn, products):
    try:
        sql = '''UPDATE products SET price = ? WHERE id = ?'''
        cursor = conn.cursor()
        cursor.execute(sql, products)
        conn.commit()
    except sqlite3.Error as e:
        print(e)


def delete_products(conn, id):
    try:
        sql = '''DELETE FROM products WHERE id = ?'''
        cursor = conn.cursor()
        cursor.execute(sql, (id,))
        conn.commit()
    except sqlite3.Error as e:
        print(e)


def select_all_products(conn):
    try:
        sql = '''SELECT * FROM products'''
        cursor = conn.cursor()
        cursor.execute(sql)
        rows = cursor.fetchall()
        for row in rows:
            print(row)
    except sqlite3.Error as e:
        print(e)


def select_products_by_limits(conn, price_limit, quantity_limit):
    try:
        sql = '''SELECT * FROM products WHERE price <= ? and quantity >= ?'''
        cursor = conn.cursor()
        cursor.execute(sql, (price_limit, quantity_limit))
        rows = cursor.fetchall()
        for row in rows:
            print(row)
    except sqlite3.Error as e:
        print(e)


def select_products_by_product_title(conn, select):
    try:
        sql = '''SELECT * FROM products WHERE product_title = ?'''
        cursor = conn.cursor()
        cursor.execute(sql, (select,))
        rows = cursor.fetchall()
        for row in rows:
            print(row)
    except sqlite3.Error as e:
        print(e)


connection = create_connection(database)
if connection is not None:
    # create_table(connection, sql_create_products_table)
    # create_products(connection, ('Жидкое мыло с запахом ванили', 65.89, 27))
    # create_products(connection, ('Мыло детское', 55.89, 27))
    # create_products(connection, ('Томатная паста', 65.89, 27))
    # create_products(connection, ('Сгущенка', 125.89, 27))
    # create_products(connection, ('Мука пшеничная', 524.99, 57))
    # create_products(connection, ('Сахар ', 85.89, 17))
    # create_products(connection, ('Рис', 95.89, 67))
    # create_products(connection, ('Соль', 12.89, 27))
    # create_products(connection, ('Чай', 65.89, 13))
    # create_products(connection, ('Картофель', 25.89, 63))
    # create_products(connection, ('Лук', 17.99, 46))
    # create_products(connection, ('Яблоки', 62.99, 47))
    # create_products(connection, ('Кефир', 65.89, 93))
    # create_products(connection, ('Молоко ', 45.89, 83))
    # create_products(connection, ('Шоколад ', 67.99, 36))
    # update_quantity(connection, (65, 5))
    # update_price(connection, (88, 4))
    # delete_products(connection, 6)
    # select_products_by_limits(connection, 100, 50)
    # select_all_products(connection)
    select_products_by_product_title(connection, ('Соль'))
    print('Done')
    connection.close()