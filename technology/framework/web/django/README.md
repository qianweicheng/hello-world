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
## admin
一行就够了 `admin.site.register(Article)`
增强:
```
class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title','pub_date','update_time',)
admin.site.register(Article,ArticleAdmin)
```
## Manager
django中的Manager类是我们通过模型类去操作数据库的工具，django给每个定义的模型默认添加一个名为objects的manager类的对象, 增加额外的manager方法是为模块添加表级功能的首选办法。
```
class BookManager(models.Manager):
  def title_count(self, keyword):
    return self.filter(title__icontains=keyword).count()
class Book(models.Model):
    xxx
# 使用
Book.objects.title_count('django')
```