# about product
from flask import request
from .blueprint import product  # use blueprint.py
from models.mongodb import conn_mongodb
from models.product import Product

# product resgistration API code
# @product.route('/regist', methods=['POST'])


@product.route('/regist', methods=['POST'])
def regist():
    # receiving product info. works
    form_data = request.form  # set request form
    # name = form_data["name"]
    # price = form_data["price"]
    # description = form_data["description"]

    # save image info.
    # saving works
    Product.insert_one(form_data)
    return "This is product registration API"

# @product.route('/test', methods=['GET'])
# def test():
#     return "This is product test API"
