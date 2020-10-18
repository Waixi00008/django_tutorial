# django_tutorial
Django入门到进阶-适合Python小白的系统课程

# git使用
- git init
- git remote add origin ...
- git status
- git pull origin main
- git add.
- git commit -m '...'
- git push origin main


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
- PYTHONIOENCODING=utf-8 python3 manage.py runserver 中文环境
- python manage.py + 回车 可查看更多命令

# 路由
简单的说，url 就是常说的网址，每个网址代表不同的网页。
在django中url也称为urlconf
每个url地址对应一个唯一的views视图函数
### 哪里存在路由？
- 根目录项目中的urls.py是根路由，根路由可以集合所有应用路由
- 每个应用下创建自己的urls.py，这个urlspy属于每个应用的独有路由，通过集成或者说绑定到根路由中进行使用。
### 路由常用方法，变量与views的绑定
```
from django.urls import path, include  //倒入url编写模块
from django.contrib import admin  //导入admin功能模块
//urlpatterns: 整个项目的url集合，每个元素代表一条url信息
path(‘admin/’, admin.site.urls)  设置admin的url，’admin/’代表uri地址，即http://127.0.0.1:8000/admin/，
//admin后边的斜杠为路径的分隔符，admin.site.urls 是url对应的视图函数
path(‘’, include(‘app.urls’))  //如果url为空即代表为网站的域名，即127.0.0.1:8000,通常为网站的首页，include的是将应用中的urls包含进来
```
```
from app import urls as app_urls
path(‘’, include(app_urls))
```
扩展知识：网址分两部分，domain域名与uri按照上边的地址分别是 127.0.0.1:8000和 admin

1. url中的参数
    - 在url后边用?开始，键与值用等号连接，每对键值用&号区分，如: http://127.0.0.1:8000/app?name=dewei&age=30
    - 在路由的参数中用分隔符分开，如: http://127.0.0.1:8000/app/dewei/30
2. django2的url变量类型
    - 字符串类型：匹配任何非空字符串，但不包含斜杠，在不指定类型的前提下，默认字符串类型 <str:name>
    - 整型：匹配0和正整数 <int:age>
    - slug:   可理解为注释，后缀或附属等概念 <slug: day>
    - uuid：匹配一个uuid格式的对象 <uuid: uid> 类似xxx-xx-xx
3. 支持url类型的方法
    - from django.urls import path 2.0以后新方法
    - from django.conf.urls import url 2.0以前的方法，不支持参数中的类型，只能通过正则表达的方式进行基本的匹配
4. django2.0以前url参数匹配简介
    - url(r'^add/(?P<name>\w+)/(?P<age>\d+)$')
    - r 非转义原始字符串
    - w+  匹配1个或多个包括下划线在内的任何字字符:[A-Za-z0-9_]
    - d+ 匹配1个或多个数字
5. 为url设置别名
    - path(‘add’, view_function, name=’add’) 
    - 别名可以在重定向和模版定义的时候直接用别名替代,在template模版中会使用到
6. 读取参数
    - ?形式的参数 -> request.GET.get(参数名)
    - 以分隔符形式的参数 Django.conf.urls不支持
    ```python
    def index(request, 参数名, 参数名):
               print(参数名)
    ```
# 视图
views是django的mvt中的v部分，主要负责处理用户的请求和生成相应内容，然后在页面或其他类型文档中显示。
基本写法:
```djangotemplate
from django.http import HttpResponse
def index(request):
    return HttpResponse(‘hello django!’)

```
1. 强行将视图分三部分
    - 用户的请求  request
    - 对用户请求的逻辑处理 handler
    - 将处理后的数据返回给用户 response
2. 用户的请求对象request
    - 浏览器向服务器发送的请求对象，包含用户信息，请求内容和请求方法
    - dir(request) 查看 request对象的所有方法
3. 常用的request对象的方法
    - request.GET -> 获取url上？形式的参数
    - request.POST -> 获取post提交的数据
    - request.path ->请求的路径,比如请求127.0.0.1/test/1,那这个值就是/test/1
    - request.method -> 请求的方法 get or post 等
4. 常用的返回对象
    - HttpResponse 可以直接返回一些字符串内容
    - from django.http import HttpResponse
    - render 将数据在模版中渲染并显示
    - from django.shortcuts import render
    - JsonResponse 返回一个json类型 通常用于与前端进行ajax交互
    - from django.http import JsonResponse
5. 视图面向对象的写法
    ```python
    from django.views.generic import View
    Class Index(View):
        def get(self, request):
            return xxx
    ```
    Index.as_views 路由处理

# Restful规范 & Http协议
1. Restful
Url定位资源，简单来说，通过一个url地址可以让我们知道这个地址所要提供的功能是什么。
比如说：127.0.0.1/add/user 那么可以看出 我们这个url要做的事情就是 添加一个用户，
再比如说，127.0.0.1/get/user/1，就可以很轻松的读出来，是 获取一个用户并且这个用户id是1
归纳一句话：url一切皆资源
2. Restful常用方法
    - Get 获取资源时使用  比如我们查看一个网页
    - Post 提交资源时使用 比如我们注册一个用户的时候
    - Put 修改资源时时候 比如我们修改自己的用户信息的时候
    - Delete 删除资源时使用 比如我们注销我们的账号的时候
3. http协议
网上应用最为广泛的一种网络协议。所有的www文件都必须遵守这个标准
4. Http的无状态性
无状态是指，当浏览器发送请求给服务器的时候，服务器响应客户端请求，但是当同一个浏览器再次给你服务器发送请求的时候，服务器并不知道它就是刚才那个浏览器。
简单的说，服务器不会记得你，所以就是无状态协议
5. Http常用状态码
    - 200 成功
    - 400 请求错误，一般是参数格式有误的时候出现
    - 403 禁止访问
    - 404 没有获取到url地址
    - 405 方法禁用，比如这个地址指定用get方法，但你用了post，就会有这个提示
    - 500 服务器异常

# Template模板
模版可以动态生成Html网页，它包括部分Html代码和一些特殊的语法
1. Template配置方法
      - 一般Template模版存放在“templates”目录中
      - 通过在项目Settings的templates的DIRS列表中添加对应的路径即可，如：os.path.join(BASE_DIR,‘templates’) 
2. Template展示渲染的数据
   - 在html中 以{{}} 为标示，在双大括号中传入视图中传入的数据
3. Template与视图的绑定
    ```
    from django.shortcuts import render
    def get(self,request):
        return render(request,'index.html',{'name':'waixi'})
    ```
4. 内置标签 用{% %}大括号 左右各一个百分号包裹
     - | **标签**                          | **介绍**           |
       | --------------------------------- | ------------------ |
       | {%  for %} {% endfor %}           | 遍历输出的内容     |
       | {% if  %} {% elif %}  {% endif %} | 对变量进行条件判断 |
       | {%  url  name args  %}            | 引用路由配置名     |
       | {%  load %}    {%  load static %} | 加载django的标签库 |
       | {%  static static_path %}         | 读取静态资源       |
       | {%  extends base_template%}       | 模版继承           |
       | {%  block data%} {% endblock %}   | 重写父模版的代码   |
       | {%  csrf_token  %}                | 跨域的  密钥       |
       
5. for标签模版
    -  | **变量**            | **说明**                |
       | ------------------- | ----------------------- |
       | forloop.counter     | 从1开始计算获取当前索引 |
       | forloop.counter0    | 从0开始计算获取当前索引 |
       | forloop.revcounter  | 索引从最大数递减到1     |
       | forloop.revcounter0 | 索引从最大数递减到0     |
       | forloop.first       | 当前元素是否是第一个    |
       | forloop.last        | 当前元素是否是最后一个  |
       | empty               | 为空的情况              |
       
# 静态文件配置
1. Css 样式文件，Javascript 文件，Image 图片文件等
2. 项目根目录创建 ‘static’ 与 ‘templates’文件夹同级
3. STATICFILES_DIRS = (os.path.join(BASE_DIR, ‘static’), )
STATICFILES_DIRS是元组，一定要逗号

# 模板内置过滤器
1. 过滤器的用处
用于在html模版中，对于渲染过来的数据进行二次操作使用，过滤器其实就是用来处理这些数据的模版引擎中使用的函数
2. 常用过滤器介绍
    -  | **内置过滤器函数** | **使用方法**                      | **说明**                                       |
       | ------------------ | --------------------------------- | :--------------------------------------------- |
       | add            | {{value\|add:10}}             | 给value的值加10                            |
       | date           | {{value\|date:”Y-m-d  H:i:s”  | 把日期格式按照规定的格式化显示             |
       | cut            | {{value\|cut:’xx’}}           | 将value中的xx删掉                          |
       | capfirst       | {{value\|capfirst}}           | Value首字母大写                            |
       | default        | {{value\|default:”xx”}}       | 值为false时使用默认值                      |
       | default_if_none | {{value\|default_if_none:”xx”}} | 值为空时候使用默认值                       |
       | dictsort       | {{value\|dictsort:”key”}}     | 值为字典的列表，按照key排序                |
       | dictsortreversed | {{value\|dictsortreversed:”key”}} | 上边方法  反序                             |
       | first          | {{value\|first}}              | 返回列表中第一个索引值                     |
       | floatformat | {{value\|floatformat:2}}  | 保留小数点后2位              |
       | join       | {{value\|join:”xx”}} | 类似python’xx’.join(value)     |
       | last      | {{value\|last}}   | 返回列表最后一个索引值                 |
       | length     | {{value\|length}} | 返回值的长度                           |
       | divisibleby | {{value\|divisibleby:2}}  | 如果可以被2整除返回true        |
       | length_is  | {{value\|length_is:”2”}}  | 如果长度是2返回true            |
       | safe           | {{value\|safe}}       | 将字符串中的html标签在前端安全显示 |
       | random         | {{value\|random}}     | 随机列表中的一个值                         |
       | slice          | {{value\|slice:”:2”}} | 截取前两个字符                             |
       | slugify        | {{value\|slugify}}    | 值小写，单词用-分隔                |
       | upper          | {{value\|upper}}      | 字符串大写                                 |
       | urlize         | {{value\|urlize}}     | 字符串中链接可点击                         |
       | wordcount      | {{value\|wrodcount}}  | 字符串中单词数                             |
       | timeuntil      | {{value\|timeuntil}}  | 距离当前日期的天数和小时数（未来）         |
       
# 自定义过滤器
在Django服务器端编写函数，在模版中可以直接调用的过滤器函数
1. 在应用下创建templatetags文件夹
2. 在文件夹下创建 myfilter.py
3. INSTALLED_APPS = ['app.templatetags',]
    ```
    from django import template
    register = template.Library()
    
    @register.filter
    def add_filter(value,args):
        return value+args
    ```
    ```
    {% load myfilter %}
    num:{{num|add_filter:10}}
    ```
   
# jinja2模板引擎
安装 
1. workon Django_venv
2. pip3 install jinja2
3. | **过滤器** | **说明**                                   |
   | ---------- | ------------------------------------------ |
   | safe       | 渲染时不转义                               |
   | capitalize | 把值的首字母转换成大写，其他字母转换成小写 |
   | lower      | 把值转换成小写形式                         |
   | upper      | 把值转换成大写形式                         |
   | title      | 把值中每个单词的首字母都转换成大写         |
   | trim       | 把值的首尾空格去掉                         |
   | striptags  | 渲染前把值中所有的HTML标签都删掉           |

# django里使用jinja模板
1. 安装jinja2
2. settings.py TEMPLATES添加
    ```
    {
        'BACKEND': 'django.template.backends.jinja2.Jinja2',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
            'environment': 'jinja_app.base_jinja2.environment'
        },
    }
    ```
3. 新建base_jinja2.py在jinja_app(应用名随意)
    ```
    from jinja2 import Environment
    from django.contrib.staticfiles.storage import staticfiles_storage
    from django.urls import reverse
    
    def environment(**options):
        env = Environment(**options)
        env.globals.update({
            'static': staticfiles_storage.url,
            'url': reverse
        })
        return env
    ```
   
# django里使用mako模板
1. 安装mako
2. 新建base_render.py
    ```
    from django.template import RequestContext
    from django.conf import settings
    from django.template.context import Context
    from django.http import HttpResponse
    from mako.lookup import TemplateLookup
    import os
    def render_to_response(request,template,data=None):
        context_instance = RequestContext(request)
        # path = settings.TEMPLATES[0]['DIRS'][0] 只有主应用才能取到这个值 C:\Users\xiaobing\Desktop\Django_Projects\django_tutorial\templates
        # 不是C:\Users\xiaobing\Desktop\Django_Projects\django_tutorial\mako_app\templates
        path = os.path.join(os.path.dirname(__file__), 'templates/')
        lookup = TemplateLookup(
            directories=[path],
            output_encoding='utf-8',
            input_encoding='utf-8'
        )
        make_template = lookup.get_template(template)
    
        if not data:
            content = {}
        if context_instance:
            context_instance.update(data)
        else:
            context_instance=Context(data)
    
        data = {}
        for d in context_instance:
            data.update(d)
    
        data['csrf_token']='<input type="hidden" name="csrfmiddlewaretoken" value="{0}" />'.format(request.META['CSRF_COOKIE'])
    
        return HttpResponse(make_template.render(**data))
    ```
3. 视图
    ```
    from django.views.generic import View
    from .base_render import render_to_response
    
    class Test(View):
        TEMPLATE = 'hi.html'
    
        def get(self, request):
            data = {
                'content': 'hello django mako'
            }
            return render_to_response(request, self.TEMPLATE, data=data)
    ```
4. mako模板
    ```
    ${content}
    <%! from django.conf import settings
    %>
    ${settings.TEMPLATES[0]['DIRS'][0]}
    ```
   
# 网络请求图片，跨域问题
 <meta name="referrer" content="no-referrer">
 
# ORM
全称：object relational mapping，通过使用它，我们可以直接使用python的方法去使用数据库
通过把表映射成类，把行作为实例，把字段作为属性，orm在执行对象操作的时候会把对应的操作转换成数据库原生语句的方式来完成数据库开发工作
### 优点：
 - 使用简单，通过将数据库语法进行封装，直接使用方法即可操作数据库
 - 性能好，在通过orm转换成sql的时候是会有一些消耗，但这个消耗其实非常低，在对整体业务提升的角度说，这点消耗可以忽略不计，除非你对于io操作的要求非常的极端
 - 兼容性好，支持目前市面上多数的关系型数据库，如mysql prestresql salite等
# django shell的使用
python manage.py shell
- In [1]: from django.db import models
- In [2]: dir(models)

### django设置实现
 - 在settings.py 中设置数据库信息（需提前在数据库中创建库）
   ```
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.mysql',
            'NAME': 'django_orm_test',
            'USER': 'root',
            'PASSWORD': '',
            'HOST': '',
            'PORT': '3306'
        }
    }
    ````
 - 在应用app的models.py中以类的形式定义模型
   ```
    from django.db import models
    
    class User(models.Model):
        name = models.CharField(max_length=20)
    ```
 - 通过模型在目标数据库中创建对应的表
    - python manage.py makemigrations
    - python manage.py migrate
 - 在视图函数中通过对模型的操作实现目标数据库的读写操作
    -  ```
           def update(request):
            # user = User.objects.get(id=1)
            # user.info = "修改{}".format(time.time())
            # user.save()
        
            User.objects.filter(id=2).update(age=50)
            return HttpResponse('改')
       ```

### model列方法与属性
1. from django.db import models
2. dir(models)
3. 类型
   -   | **字段名**                | **描述**          | **例子**                                      |
       | :------------------------ | :---------------- | --------------------------------------------- |
       | CharField                 | 字符串类型        | ‘namexxxx’                                    |
       | TextField                 | 文本类型          | ‘xxxxxxxxxxxx…’                               |
       | EmailField                | 邮箱类型          | ‘xxx@muke.com’                                |
       | UrlField                  | 网址类型          | ’http://muke.com’                             |
       | BooleanField              | 布尔类型(tinyint) | True  False                                   |
       | NullBooleanField          | 可为空的布尔类型  | None  True False                              |
       | IntegerField              | 整型              | (-2147483648,  2147483647)                    |
       | SmallIntegerField         | 短整型            | (-32768,  32767)                              |
       | BigIntegerField           | 长整型            | (-9223372036854775808,  9223372036854775807), |
       | PositiveIntegerField      | 正整型            | (0,  2147483647)                              |
       | PositiveSmallIntegerField | 短正整型          | (0,  32767)                                   |
       | FloatField                | 浮点类型          | 3.14                                          |
       | DecimalField              | 十进制小数        | 12345.123123                                  |
       | DateField                 | 日期类型          | xxxx-xx-xx                                    |
       | DateTimeField             | 日期类型          | xxxx-xx-xx xx:xx:xx                           |
       | TimeField                 | 时间类型          | xx:xx:xx (时分秒)                             |
       | ImageField                | 图片类型          | xxx.jpg                                       |
       | FileField                 | 文件类型          | 任意文件类型                                  |
   
4. 公共属性
    -  | **属性名**   | **描述**                       | **例子**    | **作用于** |
       | ------------ | ------------------------------ | ----------- | ---------- |
       | null         | 值是否设为空                   | True  False |            |
       | blank        | 值是否可为空                   | True  False |            |
       | primary_key  | 设置主键                       | True        | 整型       |
       | auto_now     | 时间自动添加                   | True        | 时间类型   |
       | auto_now_add | 自动添加时间，但仅在创建的时候 | True        | 时间类型   |
       | max_length   | 字段长度                       |             | 字符串类型 |
       | default      | 默认值                         | xxx         |            |
       | verbose_name | admin中显示的名字              | name        |            |
       | db_column    | 数据库字段名                   | age         |            |
       | unique       | 唯一索引                       | True        |            |
       | db_index     | 普通索引                       | True        |            |
5. 特殊属性
    -  | **属性名**     | **描述**                                                | **例子**    | **作用于**             |
       | -------------- | ------------------------------------------------------- | ----------- | ---------------------- |
       | max_digits     | 数字中允许的最大位数                                    | 12          | DecimalField           |
       | decimal_places | 存储的十进制位数                                        | 2           | DecimalField           |
       | width_field    | 图片宽(可不传)                                          | 1024        | ImageField             |
       | height_field   | 图片高(可不传)                                          | 576         | ImageField             |
       | upload_to      | 保存上传文件的本地文件路径，该路径由 MEDIA_ROOT  中设置 | ‘/xx/xx.xx’ | ImageField,  FileField |

6. 表关联方法
   -   | **字段名**      | **描述** | **例子** |
       | --------------- | ------- | -------- |
       | ForeignKey      | 一对多   |          |
       | OneToOneField   | 一对一   |          |
       | ManyToManyField | 多对多   |          |
       
   -    | **属性名**   | **描述**         | **例子**                                     |
        | ------------ | ---------------- | -------------------------------------------- |
        | related_name | 关联表的名       | related_name=‘profile’                       |
        | on_delete    | 外键的删除的对策 | on_delete=models.SET_NULL,CASCADE,PROTECT |

### 数据库的表关系与联合索引的创建
1. 一对一：仅在两个表中，表1的a这一行的数据和表2的a这行数据有联系，且表2的a行数据也只会和表1的a行有关系
2. 一对多：表1的第a行数据，和多个表的多行数据都会有所关系，而多个表中都行数据与表1的第a行有所关系，且只和表1的第a行有所关联
3. 表1中的第a行数据可以与表2中的一行或多行相互联系，表2中的a行也可以和表中的一行或多行相互关联
4. 联合索引：一个表中 有两个字段要合并使用一个索引
    ```
    class Meta:
    unique_together = [”day", ”hour"]       # 一条数据day+hour不能于其他数据相同
    index_together = [”username", ”phone"]  # 提高查询效率
    ```
   
### 数据库的增删改查
1. 增 注意有些需要自己写save有些不需要
    - User.objects.create(xx=xx, xx=xx)
    - user = User(xx=xx, xx=xx)   user.save()
    - User.objects.get_or_create(xx=xx, xx=xx)
    - user = User()  user.xx = xx  user.save()
2. 查
    - user = User.objects.get(id=xx) 无法用在update
    - user = User.object.filter(id=xx) 
    - Users = User.objects.all()
3. 改
    - user.object.update(xx=xx, xx=xx)
    - user.xx = xx     user.save()
4. 删
    - user = User.objects.get(id=xx)
    - user.delete()

### orm的两种查询方式
1. 原生sql的查询方法 User.objects.raw(‘select * from user’)
2. 基于orm方法查询 User.objects.filter(id=xx)
    - 下边的链式操作方法并不一定要依赖一级方法，大家要灵活运用
    -  | **方法名**                                                   | **描述**                                   |
       | ------------------------------------------------------------ | ------------------------------------------ |
       | User.objects.all()                                           | 返回user表中所有的数据                     |
       | User.objects.get(**filter)                                   | 返回满足过滤条件的数据(单调，没有则抛异常) |
       | User.objects.filter(**filter)                                | 返回满足过滤条件的多条数据，没有泽返回空   |
       | User.objects.all()/filter(). exists()                        | 返回是否有对象，True False                 |
       | User.objects.all()/filter().count()                          | 返回获取到对象的数量                       |
       | User.objects.all()/filter(). exclude(**filter)               | 返回的数据中排除满足**filter的             |
       | User.objects.filter() .distinct(‘age')                       | 返回的对象中通过某个列去重                 |
       | User.objects.filter(). order_by(‘age’)                       | 返回的对象中通过age排序                    |
       | dir(User.objects)                                            | 还有更多可能不太常用的方法                 |

3. 属性
    - | **属性名**  | **描述**                          | **举例**                |
        | ----------- | --------------------------------- | ----------------------- |
        | __exact     | sql中like ‘dewei’  的精准搜索情况 | name__exact=‘dewei’     |
        | __iexact    | 精准搜索且忽略大小写              | name__iexact=‘Dewei’    |
        | __contains  | 模糊查找  类似 like ‘%dewei%’     | name__contains=‘dewei’  |
        | __icontains | 模糊查找忽略大小写                | name__icontains=‘Dewei’ |
        | __gt        | 大于                              | age__gt=18              |
        | __gte       | 大于等于                          | age__gte=18             |
        | __lt        | 小于                              | age__lt=33              |
        | __lte       | 小于等于                          | age__lte=33             |
        | __isnull    | 是否是空                          | email__isnull=True      |

4. 或查找
    ```
    from django.db import @
    User = User.objects.filter(Q(username='zhangsan')|Q(username='lisi'))
    ```
5. 聚合查询
   -   | **方法名** | **描述** | **举例**                                   |
        | ---------- | -------- | ------------------------------------------ |
        | Avg        | 平均值   | User.objects.all() .aggregate(Avg=‘age’)   |
        | Sum        | 取和     | User.objects.all() .aggregate(Sum=‘age’)   |
        | Max        | 最大值   | User.objects.all() .aggregate(Max=‘age’)   |
        | Min        | 最小值   | User.objects.all() .aggregate(Min=‘age’)   |
        | Count      | 统计数量 | User.objects.all() .aggregate(Count=‘age’) |
        
6. 多表查询之反向查询
当在user表和diary表之间所有关联的时候，通过user模型借助diary关联的条件进行查找user的时候，我们称为反向查询，例如：
user = User.objects.filter(diary__id=2) 就是说 查找在diary表中 id为2的diary这个列队迎的user的列
7. 多表查询之查询关联信息
通过主对象选择需要查找的表对应的related_name,通过value查询具体信息，如下：
    - user = User.objects.get(pk=1)
    - user.diary.values(‘content’)  -> 返回id为1用户的diary的content信息
    - user.diary.count() -> 返回id为1用户的diary关联数量
    - user.diary 其实就是 Diary模型，我们可以通过它再去调用更多方法，比如 get filter 再去扩展查询
