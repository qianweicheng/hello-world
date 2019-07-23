# 浏览器JS相关
- 异步加载的js是不允许使用document.write, 替代方式:
  `document.createElement("script") 配合 appendChild/insertbefore 插入 script`
- 本地存储：`localStoreage, sessionStorage`
- 