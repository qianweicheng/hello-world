#Spring Boot 几个特殊的类
##ApplicationListener
监听应用的事件
##WebMvcConfigurerAdapter
最重要：配置Web各种组件，如拦截器，转换器等
##Filter
一个方法：doFilter(ServletRequest servletRequest, ServletResponse servletResponse, FilterChain filterChain)
##HandlerInterceptorAdapter
拦截请求pre/post