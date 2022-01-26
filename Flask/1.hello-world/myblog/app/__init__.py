from flask import Flask
app = Flask(__name__)
from app import routes

# Trong python 1 thu muc con bao gom tep __init__.py duoc goi la 1 goi va co the duoc import
# Khi import mot package, __init__.py se duoc thuc thi va xac dinh nhung symbols ma goi do hien thi ra ben ngoai
# Tao 1 folder (package) la app.
# https://toidicode.com/packages-trong-python-355.html
