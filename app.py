# save this as app.py
from flask import Flask
from controllers.product import product

app = Flask(__name__)

app.register_blueprint(product, url_prefix="/products") # register written API in product.py as a blueprint

# @app.route("/", methods=['GET']) # This example code could be called as 1 API. And we can omit the method argument.
# @app.route("/", methods=['POST'])  # If you want to change method, we can do like this.
@app.route("/home/test") # this represent the strings after the domain. So we should access with 12x.xxx.xxx.xx/home/test with port 200, otherwise "not found 404" error occurs.
def hello():
    return "Hello, World!"

if __name__=="__main__": # when we want to change in real time with changed code.
    app.run(debug=True)