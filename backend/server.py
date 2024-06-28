from flask import Flask, request, jsonify
import product_dao

app = Flask(__name__)

@app.route('/getProducts', methods = ['GET'])
def get_products():
  products = product_dao.get_all_products()
  response = jsonify(products)
  response.headers.add('Access-Control-Allow-Origin', '*')
  return response

if __name__ == '__main__':
  print("Starting Python Flask Server For Grocery-store Menagment System")
  app.run(port=5000)