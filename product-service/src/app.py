import os
from flask import Flask, jsonify, request
from db import db
from Product import Product

"""
products = [
    {'id': 1, 'name': 'Product 1'},
    {'id': 2, 'name': 'Product 2'}
]
"""

app = Flask(__name__)
database_uri = os.getenv('SQLALCHEMY_DATABASE_URI')
if not database_uri:
    raise ValueError("No database URI set for SQLALCHEMY_DATABASE_URI")
app.config['SQLALCHEMY_DATABASE_URI'] = database_uri
db.init_app(app)


"""
# curl -v http://localhost:5000/products
@app.route('/products')
def get_products():
    return jsonify(products)
"""

"""
@app.before_first_request
def create_tables():
    db.create_all()
"""

# curl -v http://localhost:5000/products
@app.route('/products')
def get_products():
    products = [product.json for product in Product.find_all()]
    return jsonify(products)

# curl -v http://localhost:5000/product/1
@app.route('/product/<int:id>')
def get_product(id):
    #product_list = [product for product in products if product['id'] == id]
    product = Product.find_by_id(id)
    if product is None:
        return f'Product with id {id} not found', 404
    return jsonify(product.json)


# curl --header "Content-Type: application/json" --request POST --data '{"name": "Product 3"}' -v http://localhost:5000/product
@app.route('/product', methods=['POST'])
def post_product():
    print('POST /product')
    if not request.is_json:
        return jsonify({"error": "Request must be JSON"}), 400
    # Retrieve the product from the request body
    request_product = request.get_json()
   

    # Generate an ID for the post
    #new_id = max([product['id'] for product in products]) + 1

    product = Product(None, request_product['name'])

    product.save_to_db()

    # Return the new product back to the client
    return jsonify(product.json), 201


#curl --header "Content-Type: application/json" --request PUT --data "{\"name\": \"Updated Product 2\"}" -v http://localhost:5000/product/2
@app.route('/product/<int:id>', methods=['PUT'])
def put_product(id):
    # Get the request payload
    existing_product = Product.find_by_id(id)

    if existing_product:
        updated_product = request.json

        existing_product.name = request.get_json()['name']
        existing_product.save_to_db()
        return jsonify(existing_product.json), 200

   
    return f'Product with id {id} not found', 404


# curl --request DELETE -v http://localhost:5000/product/2
@app.route('/product/<int:id>', methods=['DELETE'])
def delete_product(id):
    # Find the product with the specified ID
    existing_product = Product.find_by_id(id)

    if existing_product:
        existing_product.delete_from_db()
        return f'Product with id {id} deleted', 200
    
    return f'Product with id {id} not found', 404


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')