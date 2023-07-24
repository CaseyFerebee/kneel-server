import json
import sqlite3
from models import Orders, Metals, Styles, Sizes
ORDERS = [
    {
        "metalsId": 1,
        "styleId": 2,
        "sizesId": 3,
        "id": 1
    },
    {
        "metalsId": 1,
        "styleId": 1,
        "sizesId": 1,
        "id": 2
    },
    {
        "metalsId": 1,
        "styleId": 1,
        "sizesId": 1,
        "id": 3
    },
    {
        "metalsId": 4,
        "styleId": 1,
        "sizesId": 2,
        "id": 4
    },
    {
        "metalsId": 5,
        "styleId": 1,
        "sizesId": 3,
        "id": 5
    },
    {
        "metalsId": 2,
        "styleId": 2,
        "sizesId": 1,
        "id": 6
    },
    {
        "metalsId": 1,
        "styleId": 1,
        "sizesId": 1,
        "id": 7
    },
    {
        "metalsId": 1,
        "styleId": 1,
        "sizesId": 1,
        "id": 8
    }
]


def get_all_orders():
    # Open a connection to the database
    with sqlite3.connect("./kneeldiamonds.sqlite3") as conn:
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()

        db_cursor.execute("""
        SELECT
            o.id AS order_id,
            o.metal_id,
            o.style_id,
            o.size_id,
            m.id AS metal_id,
            m.metal AS metal,
            m.price AS metal_price,
            s.id AS style_id,
            s.style AS style,
            s.price AS style_price,
            si.id AS size_id,
            si.carets AS carets,
            si.price AS size_price
        FROM Orders o
        JOIN Metals m ON o.metal_id = m.id
        JOIN Styles s ON o.style_id = s.id
        JOIN Sizes si ON o.size_id = si.id;
                """)

        orders = []
        dataset = db_cursor.fetchall()

        for row in dataset:
            order = Orders(row['order_id'], row['metal_id'], row['style_id'], row['size_id'])

            metal = Metals(row['metal_id'], row['metal'], row['metal_price'])

            style = Styles(row['style_id'], row['style'], row['style_price'])

            size = Sizes(row['size_id'], row['carets'], row['size_price'])

            order.metal = metal.__dict__
            order.style = style.__dict__
            order.size = size.__dict__
            orders.append(order.__dict__)

        return orders



def get_single_order(order_id):
    with sqlite3.connect("./kneeldiamonds.sqlite3") as conn:
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()

        db_cursor.execute("""
            SELECT o.id, o.metal_id, o.style_id, o.size_id
            FROM Orders o
            WHERE o.id = ?
        """, (order_id,))

        data = db_cursor.fetchone()

        if data:
            order = Orders(
                data['id'],
                data['metal_id'],
                data['style_id'],
                data['size_id']
            )
        return order.__dict__




def create_order(new_order):
    with sqlite3.connect("./kneeldiamonds.sqlite3") as conn:
        db_cursor = conn.cursor()

        db_cursor.execute("""
        INSERT INTO Orders
            (metal_id, style_id, size_id)
        VALUES
            (?, ?, ?);
        """, (new_order['metal_id'], new_order['style_id'], new_order['size_id']))

        id = db_cursor.lastrowid

        new_order['id'] = id

    return new_order



def delete_order(id):
    with sqlite3.connect("./kneeldiamonds.sqlite3") as conn:
        db_cursor = conn.cursor()

        db_cursor.execute("""
        DELETE FROM Orders
        WHERE id = ?
        """, (id, ))


def update_order(id, new_order):
    with sqlite3.connect("./kneeldiamonds.sqlite3") as conn:
        db_cursor = conn.cursor()

        db_cursor.execute("""
        UPDATE Orders
        SET metal_id = ?,
            style_id = ?,
            size_id = ?
        WHERE id = ?;
        """, (new_order['metal_id'], new_order['style_id'], new_order['size_id'], id))
