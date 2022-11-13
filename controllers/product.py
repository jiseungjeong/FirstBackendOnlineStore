# about product
from flask import request
from werkzeug.utils import secure_filename
from .blueprint import product  # use blueprint.py
# from models.mongodb import conn_mongodb
from models.product import Product
from datetime import datetime
import os

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
    thumbnail_img = request.files.get('thumbnail_img')
    detail_img = request.files.get('detail_img')
    thumbnail_img_url = _upload_file(thumbnail_img)
    detail_img_url = _upload_file(detail_img)

    # saving works
    Product.insert_one(form_data, thumbnail_img_url, detail_img_url)
    return "This is product registration API"

# @product.route('/test', methods=['GET'])
# def test():
#     return "This is product test API"


def _upload_file(img_file):
    timestamp = str(datetime.now().timestamp())
    filename = timestamp+'_'+secure_filename(img_file.filename)
    image_path = f'./static/uploads'
    os.makedirs(image_path, exist_ok=True)
    img = os.path.join(image_path, filename)
    img_file.save(img)

    return f'/static/uploads/'+filename
