from flask import Flask
app = Flask(__name__)

@app.route('/hello')
# The hien ham hello_world() se duoc thuc hien khi truy cap toi /hello url cua website.
# su dung route de dinh tuyen toi cac url khac nhau
def hello_world():
    return 'Hello World'

@app.route('/')
def home():
    return 'Home Page'

@app.route('/user')
def user():
    return 'User Page'

@app.route('/about')
def about():
    return 'About Page'

# Them tham so vao url bang cach them <ten_bien>
# Dinh nghia kieu du lieu cho bien nay bang <kieu_du_lieu:tenbien>
@app.route('/user/<username>')
def show_user_profile(username):
    return 'Hello %s' % username

@app.route('/post/<int:post_id>')
def show_post(post_id):
    return "Post %d" % post_id

@app.route('/path/<path:subpath>')
def show_subpath(subpath):
    return "Subpath %s" % subpath

if __name__ == "__main__":
# Yeu cau flask thuc thi va lang nghe cac request cua nguoi dung
    app.run()
