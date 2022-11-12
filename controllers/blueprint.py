# example
# /products/regist
# /products/list
# ...
# /users/signup
# /users/signin

# /payment/...
# /order/...

from flask import Blueprint

product=Blueprint('product', __name__)