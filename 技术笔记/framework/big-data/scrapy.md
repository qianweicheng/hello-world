scrapy startproject tutorial
scrapy shell 'http://quotes.toscrape.com'
scrapy crawl quotes -o quotes.json
scrapy crawl quotes -a tag=humor

1. 命令行：scrapy crawl quotes -s LOG_FILE=scrapy.log

2. Spider设置
class MySpider(scrapy.Spider):
    name = 'myspider'

    custom_settings = {
        'SOME_SETTING': 'some value',
    }