import psycopg2
import psycopg2.extras
from datetime import datetime
from config import config


def insert_order(order):
  conn = None
  try:
    params = config()
    conn = psycopg2.connect(**params)
    cur = conn.cursor()
    order_query = '''
                     INSERT INTO orders (customer_name, total, date_time)
                     VALUES (%s, %s, %s) RETURNING order_id;''' 
    order_data = (order['customer_name'], order['total'], datetime.now())
    cur.execute(order_query, order_data)
    order_id = cur.fetchone()[0]

    order_details_query = '''
                     INSERT INTO order_details (order_id, product_id, quantity, total_price)
                     VALUES (%s, %s, %s, %s);'''
    order_details_data =[]
    for i in order['order_details']:
        order_details_data.append([
            order_id,
            int(i['product_id']),
            float(i['quantity']),
            float(i['total_price'])
        ])
    cur.executemany(order_details_query, order_details_data)
    
    conn.commit()
    cur.close()
    return order_id
  except (Exception, psycopg2.DatabaseError) as error:
        print(error)
  finally:
        if conn is not None:
            conn.close()

"""
if __name__ == '__main__':
  print(insert_order({
    'customer_name' : 'Milka',
    'total' : 90,
    'order_details' : [
      {
        'product_id' : 1,
        'quantity' : 1,
        'total_price': 30
      },
      {
        'product_id' : 3,
        'quantity' : 2,
        'total_price': 60
      }
    ]
  }
  ))
"""