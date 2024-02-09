from flask import render_template, flash, redirect, url_for
from app import app,db
import sqlalchemy as sa
from app.forms import LoginForm
from app.db_service import get_db_connection
from flask_login import current_user, login_user, logout_user, login_required
from app.models import User

@app.route('/')
@app.route('/index')
@login_required
def index():
    user = current_user
    return render_template('index.html', title='Home', user=user)

@app.route('/login', methods=['GET','POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = LoginForm()
    if form.validate_on_submit():
        user = db.session.scalar(sa.select(User).where(User.username == form.username.data))
        if user is None or not user.check_password(form.password.data):
            flash('Invalid username or password')
            return redirect(url_for('login'))
        login_user(user, remember=form.remember_me.data)
        flash('Login requested for user {}, remember_me={}'.format(user, form.remember_me.data))
        return redirect(url_for('index'))
    return render_template('login.html',title='Sign in', form=form)

@app.route('/users')
def getUsers():
    conn = get_db_connection()
    users = conn.execute('Select * from user').fetchall()
    print(users)
    conn.close()
    return None

@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('index'))