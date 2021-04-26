# -*- encoding: utf-8 -*-
import click
from app import app, db
from app.models import Message


@app.cli.command()
def initdb():
    """
    初始化数据库，重建 model 对于的库表
    使用方法： flask initdb
    """   
    db.create_all()
    click.echo('Initialized database.')