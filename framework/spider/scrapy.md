# scrapy
分类|	名称|	简介
-|-|-
爬虫框架|	Scrapy|	爬虫程序
服务端|	Scrapyd|	Scrapy爬虫管理程序
服务端|	ScrapydArt|	增强版的 Scrapyd
客户端|	ScrapydAPI|	对Scrapyd API的封装
客户端|	ScrapydWeb|	管理调度 Scrapyd
客户端|	Gerapy|	管理调度 Scrapyd
客户端|	SpiderKeeper|	管理调度 Scrapyd
## 安装
- 启动爬虫调度器:`scrapyd`,新建文件: `dbs & twistd.pid`
- 运行UI:`spiderkeeper --server=http://localhost:6800` 新建`SpiderKeeper.db`
- 部署爬虫:
    Scrapyd-Client: `scrapyd-deploy 部署名 -p 项目名称` or `scrapyd-deploy <target> -p <project> --version <version>`
    等效:`curl http://localhost:6800/addversion.json -F project=myproject -F version=r23 -F egg=@myproject.egg`
- 也可以打包爬虫，让SpiderKeeper使用: 
    Scrapyd-Client: `scrapyd-deploy --build-egg output.egg`
    手动打包: `python setup.py bdist.egg`
## 框架scrapy
```
scrapy startproject tutorial
scrapy shell 'http://quotes.toscrape.com'
scrapy crawl quotes -o quotes.json
scrapy crawl quotes -a tag=humor
```
1. 命令行：scrapy crawl quotes -s LOG_FILE=scrapy.log
2. Spider设置
class MySpider(scrapy.Spider):
    name = 'myspider'

    custom_settings = {
        'SOME_SETTING': 'some value',
    }