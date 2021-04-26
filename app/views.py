# -*- encoding: utf-8 -*-
from app import app
from flask import render_template, redirect, url_for, request
from app.forms import LoginForm


@app.route('/')
def index():
    return 'here is index'


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if request.method == 'POST' and form.validate_on_submit():
        username = form.username.data
        password = form.password.data
        return redirect(url_for('index'))
    return render_template('login.html', form=form)
