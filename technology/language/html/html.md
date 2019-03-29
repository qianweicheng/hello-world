# HTML
## DTD
`<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">`
## Script
`<script type="text/javascript" src="xxx.js" [charset='']></script>` or  
```
<script type="text/javascript">

</script>
```
## CSS
http://www.runoob.com/tags/tag-link.html

`<link type="text/css" rel="stylesheet" href="mycss.css"/>` or
```
<style type="text/css">
</style>
```
## Form
#### action
提交地址, 可以跨域
#### method
- POST
- GET
#### enctype属性
- application/x-www-form-urlencoded
    在发送前编码所有字符(默认）
- multipart/form-data
    不对字符编码,上传二进制数据
- text/plain
    空格转换为 "+" 加号，但不对特殊字符编码
## iframe
```
    frameName.document.forms[0].xxx
    frameName.document.getElementById('xxx')
```
X-Frame-Options 静止本页面被嵌套到iframe中
- DENY
- SAMEORIGIN
- ALLOW-FROM uri
## 事件
## 画布