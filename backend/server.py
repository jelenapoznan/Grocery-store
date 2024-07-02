from flask import Flask, request, jsonify
from flask_cors import CORS
import product_dao

app = Flask(__name__)
CORS(app)  # This enables CORS for all domains on all routes.

@app.route('/getProducts', methods = ['GET'])
def get_products():
  products = product_dao.get_all_products()
  response = jsonify(products)
  response.headers.add('Access-Control-Allow-Origin', '*')
  return response

@app.route('/deleteProduct', methods = ['POST'])
def delete_product():
  return_id = product_dao.delete_product(request.form['product_id'])
  response = jsonify({
    'product_id' : return_id
  })
  response.headers.add('Access-Control-Allow-Origin', '*')
  response.headers.add('Access-Control-Allow-Headers', 'Authorization, Content-Type'),
  return response

if __name__ == '__main__':
  print("Starting Python Flask Server For Grocery-store Menagment System")
  app.run(port=5000)