# Zuul(废弃)
## 初始化
- ZuulServerAutoConfiguration
    > 注册个Servlet:ZuulController包含ZuulServlet,里面通过ZuulRunner调用Filter
    - Filter返回值没有被使用
- ZuulProxyAutoConfiguration
    > 反向代理相关的
##
RouteLocator<-RefreshableRouteLocator
SimpleRouteLocator
## 依赖Ribbon比较多
## 内置过滤器
- RibbonRoutingFilter(真正做转发的)
- SendForwardFilter(将前面filter返回的response流写入初始的响应流里)