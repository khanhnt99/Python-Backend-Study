from flask import render_template
from app import app
@app.route('/')
@app.route('/index')
def index():
    user = {'username': 'Khanh'}
    posts = [
        {
            'author': {'username': 'Nguyen'},
            'body': 'Flask de hoc qua phai khong'
        },
        {
            'author': {'username': 'Tran'},
            'body': 'Lap trinh Web that thu vi'
        }

    ]
    return render_template('index.html', title='Home', user=user, posts=posts)
