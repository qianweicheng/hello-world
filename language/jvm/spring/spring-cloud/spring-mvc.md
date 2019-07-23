FrameworkServlet(doGet/doPost)->processRequest->doService
DispatcherServlet->doDispatch
HandlerAdapter->handle
SimpleControllerHandlerAdapter(mvc)/HttpRequestHandlerAdapter(mvc)/SimpleServletHandlerAdapter(web)/xxx->handle or other method


#### MVC
Controller->handleRequest
AbstractController->handleRequestInternal

HandlerMapping<-MatchableHandlerMapping<-AbstractUrlHandlerMapping
getHandler          match                   registerHandler
                                            getHandlerInternal

HandlerExecutionChain
