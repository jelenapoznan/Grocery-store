from flask import Flask, request, jsonify, json
from flask_cors import CORS
import product_dao
import uom_dao
import order_dao

app = Flask(__name__)
CORS(app)  # This enables CORS for all domains on all routes.

@app.route('/getProducts', methods = ['GET'])
def get_products():
  products = product_dao.get_all_products()
  response = jsonify(products)
  response.headers.add('Access-Control-Allow-Origin', '*')
  return response

@app.route('/getUOM', methods = ['GET'])
def get_uom():
  uom = uom_dao.get_uoms()
  response = jsonify(uom)
  response.headers.add('Access-Control-Allow-Origin', '*')
  response.headers.add('Access-Control-Allow-Headers', 'Authorization, Content-Type')
  return response

@app.route('/deleteProduct', methods = ['POST'])
def delete_product():
  return_id = product_dao.delete_product(request.form['product_id'])
  response = jsonify({
    'product_id' : return_id
  })
  response.headers.add('Access-Control-Allow-Origin', '*')
  response.headers.add('Access-Control-Allow-Headers', 'Authorization, Content-Type')
  return response

@app.route('/insertOrder', methods = ['POST'])
def insert_order():

  request_payload = json.loads(request.form['data'])
  order_id = order_dao.insert_order(request_payload)

  response = jsonify({
    'order_id' : order_id
  })
  response.headers.add('Access-Control-Allow-Origin', '*')
  response.headers.add('Access-Control-Allow-Headers', 'Authorization, Content-Type')
  return response

@app.route('/getAllOrders', methods = ['GET'])
def get_all_orders():
  response = order_dao.get_all_orders()
  response = jsonify(response)
  response.headers.add('Access-Control-Allow-Origin', '*')
  return response

@app.route('/insertProduct', methods = ['POST'])
def insert_product():
# Data that comes form the UI will be string so we convert it to dict using  json.loads!
  request_payload = json.loads(request.form['data']) # Data from UI
  product_id = product_dao.insert_new_product(request_payload)

  response = jsonify({
    'product_id' : product_id
  })
  response.headers.add('Access-Control-Allow-Origin', '*')
  response.headers.add('Access-Control-Allow-Headers', 'Authorization, Content-Type')
  return response


if __name__ == '__main__':
  print("Starting Python Flask Server For Grocery-store Menagment System")
  app.run(port=5000)