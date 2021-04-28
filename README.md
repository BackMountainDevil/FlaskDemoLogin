# Introduction

Flask 案例 - 用户登陆认证

# 代码结构

|   文件   |    说明  |
| :---- | :----: |
|   /app/   |   程序包   |
|   /app/__init__.py    |   构造文件，包含程序实例   |
|   /app/templates   |   模板，主要为html文件   |
|   /app/static   |   静态文件，其中又包含js和css文件夹   |
|   /app/static/js   |   js静态文件  |
|   /app/static/css   |   js静态文件  |
|   /app/views.py   |   视图函数（控制器）   |
|   /app/forms.py   |   表单   |
|   /app/errors.py   |   错误处理   |
|   /app/models.py   |   数据库模型   |
|   /app/commands.py   |   自定义 flask 命令   |
|   /app/config.py   |   配置文件   |
|   /.flaskenv   |   flask 公开变量配置文件   |
|   /.env   |  flask 私密变量配置文件    |
|   /.gitignore   |   git 文件   |
|   /config.ini   |   配置文件   |
|   /README.md   |    简要说明书  |
|   /docs   |    项目文档  |

# 代码逻辑

某些页面需要用户登陆才能访问，可以使用 cookie、session 等来记录用户信息，例如用户名称、权限等。

本代码中的 `http://127.0.0.1:5000/auth` 是一个需要登陆之后才能访问的页面，未成功登陆的会被重定向到登陆页面，并有信息提示。

登陆页面 `http://127.0.0.1:5000/login`，用户名和密码需要用 DB Broswer for SQLite 查看，也可以用自定义 flask 命令添加一个特殊用户，我在 command 中定义了一个 addadmin 命令，运行 `flaks addadmin` 即可添加一个帐号为 admin、密码为 123456 的账户。

ps： 本代码为了简单，密码采用明文存储，在实际生产项目中应使用加密之后的密文存储，如 hash 加密。

## session

在 session 中加入一个变量来标志是否登陆，变量存在说明已经登陆，不存在则说明未登陆，也可以将变量用来存储用户名。

可以使用 `git checkout session-login` 来查看该版本代码

提示： 使用 `git tag -n` 命令可以查看项目中所有标签

# 快速上手

## 安装环境

借助 pipenv 管理虚拟环境，未安装的需要先安装 pipenv ( pip install pipenv)

安装本程序需要的基本环境
如果打算继续开发，则需要安装开发的环境 ( pipenv install --dev)
```bash
pipenv install
```

## 使用

```bash
# 激活虚拟环境
pipenv shell

# 初始化 sqlite 数据库
flask initdb

# 可选：生成测试数据（需要 dev 模式）
flask forge

# 启动 flask
flask run   
# 浏览 http://127.0.0.1:5000/
# Ctrl + C 退出flask
exit    # 退出虚拟环境
```

# License

MIT

# Refer

[Flask 模板案例](https://gitee.com/anidea/flaskdemo-templates)

[Flask 表单案例](https://gitee.com/anidea/flaskdemo-form)

[greyli /sayhello ](https://github.com/greyli/sayhello)

[greyli / bluelog](https://github.com/greyli/bluelog)
