import sqlite3
from flask import Flask, Blueprint, render_template, request, url_for, flash, redirect, jsonify
from flask_login import LoginManager, UserMixin, login_user, login_required, current_user, logout_user
from werkzeug.exceptions import abort
from werkzeug.security import generate_password_hash, check_password_hash
import sys

def get_db_connection():
    conn = sqlite3.connect('database.db')
    conn.row_factory = sqlite3.Row 
    return conn

def get_list_tasks(list_id):
    conn = get_db_connection()
    list_data = conn.execute('SELECT * FROM List WHERE id = (?)',
                        (list_id,)).fetchone()
    # conn.execute('INSERT INTO Task (name, detail) VALUES (?, ?)',
    tasks = conn.execute('SELECT * FROM Task WHERE list_id = (?)',
                        (list_id,)).fetchall()
    conn.close()
    if list is None:
        abort(404)
    return (list_data, tasks)

def get_user_lists(user):
    conn = get_db_connection()
    user_id = conn.execute('SELECT id FROM User WHERE name = (?)',
                        (user,)).fetchone()
    lists = conn.execute('SELECT * FROM List WHERE user_id = (?)',
                        (user_id['id'],)).fetchall()
    conn.close()
    return lists

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your secret key'
# # blueprint for auth routes in our app
# from .auth import auth as auth_blueprint
# app.register_blueprint(auth_blueprint)

# # blueprint for non-auth parts of app
# from .main import main as main_blueprint
# app.register_blueprint(main_blueprint)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/<user>')
#@login_required
def profile(user):
    lists = get_user_lists(user)
    return render_template('profile.html', user=user , lists=lists)

@app.route('/<int:list_id>', methods=('GET', 'POST'))
def list(list_id):
    if request.method == 'POST':
        task = request.form['name']
        detail = request.form['detail']
        conn = get_db_connection()
        conn.execute('INSERT INTO Task (name, detail, list_id) VALUES (?,?,?)',
                         (task, detail, list_id))
        conn.commit()
        conn.close()
        return redirect('/' + str(list_id))
    
    (list_data, tasks) = get_list_tasks(list_id)
    # print(tasks, file=sys.stderr)
    return render_template('list.html', list=list_data, tasks=tasks)

@app.route('/create', methods=('GET', 'POST'))
def create():
    if request.method == 'POST':
        title = request.form['title']

        if not title:
            flash('Title is required!')
        else:
            conn = get_db_connection()
            conn.execute('INSERT INTO List (title) VALUES (?)',(title,))   
            list_id = conn.execute('SELECT id FROM List WHERE title = (?)',(title,)).fetchone()
            conn.commit()
            conn.close()
            return redirect('/' + str(list_id['id']))
    return render_template('create.html')

@app.route('/login')
def login():
    return render_template("login.html")

@app.route('/login', methods=['POST'])
def login_post():
    email = request.form.get('email')
    password = request.form.get('password')
    # password=generate_password_hash(password, method='sha256')
    remember = True if request.form.get('remember') else False

    conn = get_db_connection()
    user = conn.execute('SELECT name FROM User WHERE email = (?)',(email,)).fetchone()
    userpassword = conn.execute('SELECT password FROM User WHERE email = (?)',(email,)).fetchone()
    # check if the user actually exists
    # take the user-supplied password, hash it, and compare it to the hashed password in the database
    if not user or not check_password_hash(userpassword['password'], password):
        flash('Please check your login details and try again.')
        return redirect(url_for('login'))

    conn.commit()
    conn.close()
    # if the above check passes, then we know the user has the right credentials    
        # login_user(user, remember=remember)
        # print(user['name'], file=sys.stderr)
    return redirect('/' + str(user['name']))


@app.route('/logout')
def logout():
    return render_template("logout.html")

@app.route('/signup')
def signup():
    return render_template('signup.html')

@app.route('/signup', methods=['POST'])
def signup_post():
    # code to validate and add user to database goes here
    email = request.form.get('email')
    name = request.form.get('name')
    password = request.form.get('password')
    password=generate_password_hash(password, method='sha256')       #Hash the password so the plaintext version isn't saved
    
    conn = get_db_connection()
    user = conn.execute('SELECT email FROM User WHERE email = (?)',(email,)).fetchone()
    
    # if a user is found, we want to redirect back to signup page so user can try again
    if user:
        flash('Account already exits. Log in instead.')
        return redirect(url_for('login')) 

    # add the new user to the database
    else:
        conn.execute('INSERT INTO User (email, name, password) VALUES (?,?,?)',(email, name, password))

    conn.commit()
    conn.close()
    return redirect(url_for('login'))

@app.route('/listcount.json', methods=('GET', 'POST'))
def listcount():
    # API for js AJAX : return number of lists in json format
    db = get_db_connection()
    listcounts = db.execute("SELECT COUNT(*) FROM List;").fetchone()[0]
    db.close()
    print(f" listcounts = {listcounts}")
    return jsonify({'listcounts':listcounts})
