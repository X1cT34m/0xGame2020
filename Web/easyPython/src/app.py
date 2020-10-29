
from flask import Flask, render_template, request, redirect, url_for, flash, make_response
from flask_bootstrap import Bootstrap
from flask_login import LoginManager, login_user, logout_user, current_user, login_required
import configs
import pickle
import base64
from models import query_user, User

app = Flask(__name__)
app.config.from_object(configs)
Bootstrap(app)

# login management
login_manager = LoginManager()
login_manager.login_view = 'login'
login_manager.login_message_category = 'info'
login_manager.login_message = 'Please login'
login_manager.init_app(app)

# user loader
@login_manager.user_loader
def load_user(user_id):
    if query_user(user_id) is not None:
        curr_user = User()
        curr_user.id = user_id

        return curr_user

# home page
@app.route('/')
# @login_required
def index():
    usercookies = request.cookies.get('Cookies')
    if not usercookies:
        usercookies = "{'username':'guest'}"
    else:
        usercookies = pickle.loads(base64.b64decode(usercookies))

    resp = make_response(render_template('index.html'))
    resp.set_cookie('Cookies', base64.b64encode(pickle.dumps(usercookies)))
    return resp

@app.route('/app.py.bak')
def bak():
    return render_template('app.py.html')

@app.route('/login', methods = ['GET', 'POST'])
def login():
    usercookie = request.cookies.get('Cookies')
    usercookie = pickle.loads(base64.b64decode(usercookie))
    if request.method == 'POST':
        userid = request.form.get('userid')
        password = request.form.get('password')
        user = query_user(userid)
        if user is not None and password == user['password']:
            curr_user = User()
            curr_user.id = userid
            login_user(curr_user)
            return "<script>alert('flag in /flag');window.location.href='/';</script>"
        else:
            flash('Incorrect user id or password.')
    
    resp = make_response(render_template('login.html'))
    return resp

@app.route('/logout')
@login_required
def logout():
    logout_user()
    return "<script>alert('Logout successfully');window.location.href='/';</script>"


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)
