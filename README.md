# django_tutorial
Django入门到进阶-适合Python小白的系统课程

# Web的结构
- 网站的前端：通过用户肉眼看到的网站的布局，内容，对网站的操作的功能，一切可以让用户可以直接接触与操作的部分。
- 网站的后端：大量的业务逻辑，数据库io，用户不可见，不可直接接触的部分。

Ps：用户通过访问前端的功能，前端分为静态功能和动态功能。
- 静态功能则不会和后端服务器进行交互，仅在前端处理并响应用户
- 动态功能则通过与后端的交互，通过前端发送给后端的指令，在后端接到指令并作出相应逻辑处理后响应给前端，前端在收到后端响应后，将结果直接或二次加工后呈现给用户。

# Web结构图-前后端不分离
![前后端不分离](./asserts/1.png)

# Web结构图-前后端分离
![前后端不分离](./asserts/2.png)

# Python中的后端服务器框架
   |     名称     | 描述                                                         |
   | :----------: | -----------------------------------------------------------|
   | **Tornado**  | 支持异步，有自己的服务器的Web框架，成熟的Web框架，初学难度高 |
   |  **Webpy**   | 一个小巧的Web框架，貌似已经停止更新                          |
   |  **Flask**   | 一个轻量级框架，生态齐备，使用率高，有一定学习成本           |
   | **Japronto** | 2017年出的新框架，性能很强，但生态还不齐备，当前版本还有诸多问题 |
   |  **Django**  | 成熟的PythonWeb框架，生态齐全且功能齐备，学习成本低，易于快速上手 |

# Django中的MVT
![Django中的MVT](./asserts/3.png)

# Django中的模块
- 模型 Model：数据层，处理与数据相关的所有事物
- 视图 View：视图层，用来处理用户发出的请求
- 模版 Template：模版层，通过视图函数渲染html模版，得到动态的前端页面
- 路由 Url： 网站的入口，关联到对应的视图函数，访问网址就对应一个函数
- 表单 Forms：表单，用在在浏览器输入数据提交，并对这些数据进行验证。
- 后台 Admin： Django自带一个管理后台，对你提交的数据进行管理
- 配置 Settings：Django的设置，配置文件。

# windows下模拟 mac/linux终端 cmder
[windows下模拟 mac/linux终端 cmder](http://cmder.net/)

# 推荐使用安装ipython
pip install ipython

# Virtualenv
Virtualenv是一个Python的虚拟环境库，通过它可以防止各个项目之间因为Python版本不同或第三方库版本不同引起冲突，每个虚拟环境都是独立，干净的
pip install virtualenv
创建虚拟环境路径：virtualenv  -p python3 env(名称)
启动虚拟环境：. env/bin/active
推出虚拟环境： deactive
Ps：虚拟环境不是必须的，根据个人情况和习惯使用

# Django的基础命令
- django-admin startproject 项目名->创建一个django项目
- python manage.py startapp 应用名->项目中创建一个应用
- Python manage.py shell -> 进入调试代码的调试模式
- python manage.py makemigrations -> 数据库创建更改文件
- python manage.py migrate -> 同步到数据库进行更新
- python manage.py flush -> 清空数据库
- python manage.py runserver 0.0.0.0:8000 -> 启动开发服务器
- python manage.py + 回车 可查看更多命令
