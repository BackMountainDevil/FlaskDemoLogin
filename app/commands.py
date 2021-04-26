# -*- encoding: utf-8 -*-
import click
from app import app, db
from app.models import Message, User


@app.cli.command()
def initdb():
    """
    初始化数据库，重建 model 对于的库表
    使用方法： flask initdb
    """   
    db.create_all()
    click.echo('Initialized database.')


@app.cli.command()
@click.option('--count', default=20, help='Quantity of messages, default is 20.')
def forge(count):
    """
    向数据库中添加虚假数据，测试时使用
    使用方法： flask forge
    """  
    from faker import Faker  # noqa

    # db.drop_all()
    # db.create_all()

    fake = Faker()
    click.echo('Working...')

    for i in range(count):
        message = Message(
            name=fake.name(),
            body=fake.sentence(),
            timestamp=fake.date_time_this_year()
        )
        user = User(
            id=i,
            username=fake.name(),
            password='123456'
        )
        db.session.add(user)
        db.session.add(message)

    db.session.commit()
    click.echo('Created %d fake messages.' % count)