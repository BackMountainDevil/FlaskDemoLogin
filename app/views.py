# -*- encoding: utf-8 -*-
from app import app, login_manager
from flask import render_template, redirect, url_for, request, session, flash
from flask_login import login_user
from app.forms import LoginForm
from app.models import User


@login_manager.user_loader
def load_user(user_id):
    """
    调用 current_user 时 flask_login 会调用此函数
    登陆时返回 user 类实例
    未登录则返回匿名对象
    """
    user = User.query.get(int(user_id))
    return user


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
        print("user: ", user, "username: ", user.username, 'id== ', user.id)
        if user:
            login_user(user)    # 登入用户。此处传的是user 而不是 user.id
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
        flash('已成功登陆' + session['AUTH'])
        return redirect(url_for('index'))
    else:
        flash(u'登陆尚未成功，请重新登陆')
        return redirect(url_for('login'))


@app.route('/logout')
def logout():
    '''
    退出登陆
    删除session中的标志
    重定向到首页
    '''
    if 'AUTH' in session:
        session.pop('AUTH')
    return redirect(url_for('index'))
