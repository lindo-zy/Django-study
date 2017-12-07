# Django-study
Don`t repeate yourself  
学习教程参考：https://code.ziqiangxuetang.com/django/django-tutorial.html
***
## Django简介:  

urls.py  
网址入口，关联到对应的views.py中的一个函数（或者generic类），访问网址就对应一个函数。  
***
views.py  
处理用户发出的请求，从urls.py中对应过来, 通过渲染templates中的网页可以将显示内容，比如登陆后的用户名，用户请求的数据，输出到网页。
***
models.py  
与数据库操作相关，存入或读取数据时用到。
***
forms.py  
表单，用户在浏览器输入数据提交，对数据的验证工作以及输入框生成等工作。  
***
admin.py  
后台，可以用很少代码拥有一个强大后台。
***
settings.py  
Django的设置，配置文件。  
***
## Django安装  
推荐使用：  
```
pip install django==VERSION(版本号) 

```  
*** 
## 启动第一个项目
windows：  
cmd切换到工作目录
```
django-admin startproject projectname
```
切换到project目录  
```
python manage.py runserver [port](可选，默认8000)
```
启动Django服务，浏览器访问localhost:[port]（localhost:8000/127.0.0.1:8000） 
***
1.建立项目  
2.在templates文件夹下建立一个名为当前app名称的文件夹  
3.修改setting文件  
4.