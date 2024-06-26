import psycopg2
from config import config

def connect():
  ''' Connect to PostgreSQL database server'''
  conn = None
  try:
    # Read connection parameters
    params = config()

    # Connect to the PostgreSQL server
    print('Connecting to PostgreSQL database')
    conn = psycopg2.connect(**params)

    # Create a cursor
    cur = conn.cursor()

    print('PostgreSQL database version:')
    cur.execute('SELECT version()')

    db_version = cur.fetchone()
    print(db_version)
    # Close the communication with PostgreSQl
    cur.close()
  except(Exception, psycopg2.DatabaseError) as error:
    print(error)
  finally:
    if conn is not None:
      conn.close()

if __name__ == '__main__':
  connect()