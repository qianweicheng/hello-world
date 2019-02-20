# Spring Boot 
## 几个特殊的类
[Doc](https://docs.spring.io/spring-boot/docs/current/reference/html/index.html)
## 流程
    Client->DispatchServlet->HandlerMapping->Handler(filter，intecepter)->Controller->ViewResolver->jsp/Template->Client
## ApplicationListener
监听应用的事件
## WebMvcConfigurerAdapter
最重要：配置Web各种组件，如拦截器，转换器等
## Filter
一个方法：doFilter(ServletRequest servletRequest, ServletResponse servletResponse, FilterChain filterChain)
## HandlerInterceptorAdapter
拦截请求pre/post
## ControllerAdvice
## Spring-Web-Mvc
获取参数的几种方式
- 原始方式: HttpServletRequest
- 形参自动注入:
    - public ModelAndView method(@RequestParam("username")String username)//名字相同可以省略成:public ModelAndView method(String username)
    - 将参数封装成对象:public ModelAndView method3(@RequestBody User user)
- 地址栏传值:
`
@RequestMapping("/method/{id}")
public ModelAndView method(@PathVariable("id") Long id)
`
## Refresh Endpoint
#### bus-refresh
刷新Refresh Scope 
#### bus-env
更新每个Instance的env
#### refresh
#### env
