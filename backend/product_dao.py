import psycopg2
import psycopg2.extras

from config import config


def get_all_products():
  conn = None
  try:
    params = config()
    conn = psycopg2.connect(**params)
    cur = conn.cursor(cursor_factory = psycopg2.extras.RealDictCursor)
    cur.execute('''
                SELECT * FROM product
                INNER JOIN unit
                ON product.unit_id = unit.unit_id''')
    response = cur.fetchall()
    cur.close()
    return response
  except(Exception, psycopg2.DatabaseError) as error:
    print(error)
  finally:
    if conn is not None:
      conn.close()

def insert_new_product(product):
  conn = None
  try:
    params = config()
    conn = psycopg2.connect(**params)
    cur = conn.cursor()
    insert_product_query = '''
                     INSERT INTO product(name, unit_id, price_per_unit)
                     VALUES (%s, %s, %s) RETURNING product_id;''' 
    product_values = (product['name'], product['unit_id'], product['price_per_unit'])
    cur.execute(insert_product_query, product_values)
    product_id = cur.fetchone()[0]
    conn.commit()
    cur.close()
    return product_id
  except (Exception, psycopg2.DatabaseError) as error:
        print(error)
  finally:
        if conn is not None:
            conn.close()

def delete_product(product_id):
   conn = None
   print('product_id',product_id)
   try:
      params = config()
      conn = psycopg2.connect(**params)
      cur = conn.cursor()
      delete_product_query = '''
                             DELETE FROM product
                             WHERE product_id = %s '''
      delete_id = (product_id,)
      cur.execute(delete_product_query, delete_id)
      affected_rows = cur.rowcount  # Check how many rows were affected
      conn.commit()
      cur.close()
      return affected_rows 
   except (Exception, psycopg2.DatabaseError) as error:
        print(error)
   finally:
        if conn is not None:
            conn.close()

# if __name__ == '__main__':
  # print(delete_product(product_id))