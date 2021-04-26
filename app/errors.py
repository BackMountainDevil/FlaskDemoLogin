# -*- encoding: UTF-8 -*-
from flask import render_template
from app import app


@app.errorhandler(404)
def page_not_found(e):
    """自定义404页面"""
    return render_template('errors/404.html'), 404


@app.errorhandler(500)
def internal_server_error(e):
    """自定义500页面"""
    return render_template('errors/500.html'), 500