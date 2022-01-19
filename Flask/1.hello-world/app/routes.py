from app import appvar

@appvar.route('/')
def root():
    return "This is root"

@appvar.route('/index')
def index():
    return "Hello, World!"
