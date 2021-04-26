# Introduction

Flask 案例

# 三种代码结构

## 基本结构

HTML 模板放在统一目录下，后端代码全集中在一个py文件

如 [Flask 模板案例](https://gitee.com/anidea/flaskdemo-templates)

## 包组织结构

douhu为项目名称（ FLASK_APP=douhu）

|   文件   |    说明  |
| :---- | :----: |
|   /douhu/   |   程序包   |
|   /douhu/__init__.py    |   构造文件，包含程序实例   |
|   /douhu/templates   |   模板，主要为html文件   |
|   /douhu/static   |   静态文件，其中又包含js和css文件夹   |
|   /douhu/static/js   |   js静态文件  |
|   /douhu/static/css   |   js静态文件  |
|   /douhu/views.py   |   视图函数（控制器）   |
|   /douhu/forms.py   |   表单   |
|   /douhu/errors.py   |   错误处理   |
|   /douhu/models.py   |   数据库模型   |
|   /douhu/commands.py   |   自定义 flask 命令   |
|   /douhu/config.py   |   配置文件   |
|   /.flaskenv   |   flask 公开变量配置文件   |
|   /.env   |  flask 私密变量配置文件    |
|   /.gitignore   |   git 文件   |
|   /config.ini   |   配置文件   |
|   /README.md   |    简要说明书  |
|   /docs   |    项目文档  |

如 [ greyli /sayhello ](https://github.com/greyli/sayhello)

## 蓝本

如 [greyli / bluelog](https://github.com/greyli/bluelog)
> 在该项目中，views.py 被转换成 blueprints 子包，views.py 的内容按照类别分离成 auth.py, blog.py 和 admin.py 三个模块

|   文件   |    说明  |
| :---- | :----: |
|   /blueprints/__init__.py   |      |
|   /blueprints/blog.py   |      |
|   /blueprints/auth.py   |      |
|   /blueprints/admin.py   |      |
|   /templates/admin/   |   admin模板   |
|   /templates/auth/   |   auth模板   |
|   /templates/blog/   |   blog模板   |
|   /__init__.py    |   构造文件，包含程序实例   
|   /static   |   静态文件，其中又包含js和css文件夹   |
|   /forms.py   |   表单   |
|   /models.py   |   数据库模型   |
|   /utils.py   |   辅助函数   |
|   /fakes.py   |   虚拟数据生成   |
|   /extensions.py   |   扩展   |
|   /.flaskenv   |   flask 公开变量配置文件   |
|   /.env   |  flask 私密变量配置文件    |
|   /.gitignore   |   git 文件   |

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
