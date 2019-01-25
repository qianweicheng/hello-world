# Django
参考文档在[这里](https://docs.djangoproject.com/zh-hans/2.1/intro/tutorial01/)
0. pip install Django
1. 创建项目: `django-admin startproject mysite`
2. 创建应用: `python manage.py startapp polls`
3. 初始化数据库: 
    - 根据models生成sql文件，`python manage.py makemigrations polls`
    - 将SQL文件ApplyTo DB：`python manage.py migrate`, 
4. 启动应用: `python manage.py runserver`
5. 添加管理员: `python manage.py createsuperuser`, qianweicheng/A1234567

## CMS
- Mezzanine
- django-cms: 需要开发者二次开发
- Wagtail: 需要开发者二次开发