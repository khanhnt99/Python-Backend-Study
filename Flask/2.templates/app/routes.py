from flask import render_template
from app import app

@app.route('/')
@app.route('/index')
def index():
    user = {'username': 'Khanh'}
    posts = [
        {
            'author': {'username': 'Khanh'},
            'body': 'Hom nay troi dep'
        },
        {
            'author': {'username': 'Linh'},
            'body': 'Hom nay troi khong dep'
        }
    ]
    return render_template('index.html', title='Home', user=user, posts=posts)