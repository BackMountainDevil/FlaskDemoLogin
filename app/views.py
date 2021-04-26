# -*- encoding: utf-8 -*-
from app import app
from flask import render_template, redirect, url_for, request, session, flash
from app.forms import LoginForm
from app.models import User


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if request.method == 'POST' and form.validate_on_submit():
        '''验证表单'''
        username = form.username.data
        password = form.password.data
        user = User.query.filter(User.username==username, User.password==password).first()
        if user:
            session['AUTH'] = username
        return redirect(url_for('isauth'))
    if 'AUTH' in session:    
        session.pop('AUTH')
    return render_template('login.html', form=form)


@app.route('/auth')
def isauth():
    '''
    是否登陆测试页面
    已登陆： 显示'已成功登陆'
    未登陆： 重定向到登陆页面
    '''
    if 'AUTH' in session:
        return '已成功登陆'+session['AUTH']
    else:
        flash(u'登陆尚未成功，请重新登陆')
        return redirect(url_for('index'))
