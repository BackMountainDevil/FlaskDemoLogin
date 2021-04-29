# -*- encoding: utf-8 -*-
from app import app, login_manager
from flask import render_template, redirect, url_for, request, session, flash
from flask_login import login_user, logout_user, current_user
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
        # user 可能为空：没有这个用户、名称或者密码不对
        if user:
            print("user: ", user, "username: ", user.username, 'id== ', user.id)
            login_user(user)    # 登入用户。此处传的是user 而不是 user.id
        return redirect(url_for('isauth'))
    return render_template('login.html', form=form)


@app.route('/auth')
def isauth():
    '''
    是否登陆测试页面
    已登陆： 显示'已成功登陆'
    未登陆： 重定向到登陆页面
    '''
    if current_user.is_authenticated:
        flash('已成功登陆')
        return redirect(url_for('index'))
    else:
        flash(u'登陆尚未成功，请重新登陆')
        return redirect(url_for('login'))


@app.route('/logout')
def logout():
    '''
    退出登陆
    使用 flask-login 的注销用户功能
    重定向到首页
    '''
    logout_user()   # 注销  flask-login 中的用户
    flash('成功注销', 'info')
    return redirect(url_for('index'))
