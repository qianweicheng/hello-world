# Django
参考文档在[这里](https://docs.djangoproject.com/zh-hans/2.1/intro/tutorial01/)
0. 准备环境:
    ```
        mkdir myroot;cd myroot;
        virtualenv -p python3 venv; source venv/bin/activate;
        pip install Django;
    ```
1. 创建项目: `django-admin startproject mysite`
2. 创建应用: `./manage.py startapp app_test`
3. 初始化数据库: 
    - 定义model
    - 根据models生成sql文件，`./manage.py makemigrations app_test`
    - 将SQL文件ApplyTo DB：`./manage.py migrate`, 
4. 启动应用: 
    - PyCharm 启动
    - `./manage.py runserver`
    - 直接通过gunicorn启动
    ``` 
        # In urls.py
        # For static files ONLY IN DEBUG MODE
        from django.contrib.staticfiles.urls import staticfiles_urlpatterns
        urlpatterns += staticfiles_urlpatterns()
        
        (Django):python manage.py collectstatic;
        gunicorn mysite.wsgi:application --bind 0.0.0.0:8000
    ```
5. 添加管理员: `python manage.py createsuperuser`, admin/A1234567
## 使用RESTful API
```
    pip install djangorestframework
    pip install markdown       # Markdown support for the browsable API.
    pip install django-filter  # Filtering support
```
## CMS
- Mezzanine
- django-cms: 需要开发者二次开发
- Wagtail: 需要开发者二次开发