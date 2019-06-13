# 爬虫
## 安装
#### selenium
    `pip install selenium` or `http://www.seleniumhq.org/download/`
#### Headless
常用Headless browser
- Phantomjs（项目暂封存，慎用）
    `http://phantomjs.org/download.html`
- Chrome
    Downloads: https://sites.google.com/a/chromium.org/chromedriver/downloads
    `alias chrome="/Applications/Google\ Chrome.app/Contents/MacOS/Google\ Chrome"`
    ```
        chrome \
        --headless \                   # Runs Chrome in headless mode.
        --disable-gpu \                # Temporarily needed if running on Windows.
        --remote-debugging-port=9222 \
        https://www.chromestatus.com   # URL to open. Defaults to about:blank.
    ```
- FireFox
## 使用
```
    from selenium import webdriver
    # Method 1
    browser = webdriver.PhantomJS(executable_path='/path/to/phantomjs')
    # Method 2
    # options = Options()
    # options.add_argument("--headless")
    # options.add_argument("--disable-gpu")
    # browser = webdriver.Chrome(options=options)
    browser.get("http://www.eshow365.com/zhanhui/html/120062_0.html")
    print (browser.page_source)
    body = browser.find_element_by_tag_name('body')
    body_text = body.get_attribute('innerHTML')
```
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