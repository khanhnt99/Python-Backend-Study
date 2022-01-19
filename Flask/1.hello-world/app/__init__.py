# Thu muc co chua file __init__.py duoc xem nhu 1 goi
# Tao 1 goi app. Khi import goi app file init se duoc thuc thi
from flask import Flask
appvar = Flask(__name__)
from app import routes
