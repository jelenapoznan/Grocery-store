import psycopg2
import psycopg2.extras

from config import config


def get_uoms():
  conn = None
  try:
    params = config()
    conn = psycopg2.connect(**params)
    cur = conn.cursor(cursor_factory = psycopg2.extras.RealDictCursor)
    cur.execute('''
                SELECT * FROM unit
                ''')
    response = cur.fetchall()
    cur.close()
    return response
  except(Exception, psycopg2.DatabaseError) as error:
    print(error)
  finally:
    if conn is not None:
      conn.close()

#if __name__ == '__main__':
  #print(get_uoms())