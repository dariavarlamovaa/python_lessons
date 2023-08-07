import sqlite3
from DataBase import DataBase
import os

from flask import Flask, render_template, request, flash, session, redirect, url_for, \
    abort

DATABASE = '/tmp/flsk.db'
DEBUG = True
SECRET_KEY = 'FKOKRFO5KO5KO4567KO32KOKORFVLPL'

app = Flask(__name__)
app.config.from_object(__name__)

app.config.update({'DATABASE': os.path.join(app.root_path, 'flsk.db')})


def connect_db():
    con = sqlite3.connect(app.config['DATABASE'])
    con.row_factory = sqlite3.Row
    return con


def create_db():
    db = connect_db()
    with open('sq_db.sql', 'r') as f:
        db.cursor().executescript(f.read())
    db.commit()
    db.close()


menu = [
    {'name': 'Main page', 'url': '/'},
    {'name': 'About us', 'url': 'about'},
    {'name': 'Contacts', 'url': 'contacts'}
]


@app.route('/index')
@app.route('/')
def index():
    db_con = connect_db()
    db = DataBase(db_con)
    return render_template('index.html', title='Main page', menu=db.get_menu(), posts=db.get_posts())


@app.route('/add_post', methods=['GET', 'POST'])
def add_post():
    db_con = connect_db()
    db = DataBase(db_con)

    if request.method == 'POST':
        if len(request.form['title']) > 4 and len(request.form['text']) > 20:
            res = db.add_post(request.form['title'], request.form['text'], request.form['url'])
            if res:
                flash('Post successfully added', category='success')
            else:
                flash('Error while adding the post', category='error')
        else:
            flash('Error while adding the post', category='error')
    return render_template('add_post.html', title='Add a posts', menu=db.get_menu())


@app.route('/post/<post_id>')
def show_post(post_id):
    db_con = connect_db()
    db = DataBase(db_con)

    title, post = db.get_post(post_id)
    print(post)
    if not title:
        abort(404)

    return render_template('post.html', title=title, post=post, menu=db.get_menu())


@app.route('/about')
def about():
    return render_template('about.html', title='About us', menu=menu)


@app.route('/contacts', methods=['GET', 'POST'])
def contacts():
    db_con = connect_db()
    db = DataBase(db_con)

    context = {}
    if request.method == 'POST':
        if len(request.form['username']) > 1:
            flash('The message sent successfully', category='success')
        else:
            flash('Error while sending the message', category='error')
        context = {
            'username': request.form['username'],
            'email': request.form['email'],
            'message': request.form['message']
        }
    return render_template('contacts.html', **context, title='Contacts', menu=db.get_menu())


@app.route('/profile/<string:username>')
def profile(username):
    if 'userLogged' not in session or session['userLogged'] != username:
        abort(401)
    return f'User: {username}'


@app.route('/login', methods=['GET', 'POST'])
def login():
    if 'userLogged' in session:
        return redirect(url_for('profile', username=session['userLogged']))
    elif request.method == 'POST' and request.form['username'] == 'admin' \
            and request.form['password'] == 'admin':
        session['userLogged'] = request.form['username']
        return redirect(url_for('profile', username=session['userLogged']))
    return render_template('login.html', title='Log in', menu=menu)


@app.errorhandler(404)
def page_not_found(error):
    return render_template('page404.html', title='Page not found', menu=menu), 404


if __name__ == '__main__':
    create_db()
    app.run(debug=True)