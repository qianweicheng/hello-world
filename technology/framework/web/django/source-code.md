# 源码分析
## Django
#### View
- TemplateView
- RedirectView
- BaseDetailView(SingleObjectMixin, View)
    - DetailView(SingleObjectTemplateResponseMixin, BaseDetailView)
- ProcessFormView(View)
- BaseFormView(FormMixin, ProcessFormView)
    - FormView(TemplateResponseMixin, BaseFormView)
- BaseCreateView(ModelFormMixin, ProcessFormView)
    - CreateView(SingleObjectTemplateResponseMixin, BaseCreateView)
- BaseUpdateView(ModelFormMixin, ProcessFormView)
    - UpdateView(SingleObjectTemplateResponseMixin, BaseUpdateView)
- BaseDeleteView(DeletionMixin, BaseDetailView)
    - DeleteView(SingleObjectTemplateResponseMixin, BaseDeleteView)
- BaseListView(MultipleObjectMixin, View)
    - ListView(MultipleObjectTemplateResponseMixin, BaseListView)
#### Mixin
- ContextMixin
    - SingleObjectMixin(ContextMixin)
    - FormMixin(ContextMixin)
    - ModelFormMixin(FormMixin, SingleObjectMixin)
    - MultipleObjectMixin(ContextMixin)
- TemplateResponseMixin
    - SingleObjectTemplateResponseMixin(TemplateResponseMixin)
    - MultipleObjectTemplateResponseMixin(TemplateResponseMixin)
- DeletionMixin
## rest framework
#### View 继承
- View
    - APIView
        - GenericAPIView 
            - ListAPIView RetrieveAPIView DestroyAPIView UpdateAPIView  ListCreateAPIView RetrieveUpdateAPIView RetrieveDestroyAPIView RetrieveUpdateDestroyAPIView
#### Mixin
CreateModelMixin
ListModelMixin
RetrieveModelMixin
UpdateModelMixin
#### Renderer
- BaseRender
    - JSONRenderer
    - TemplateHTMLRenderer->StaticHTMLRenderer
    - HTMLFormRenderer
    - DocumentationRenderer
    - SchemaJSRenderer
    - MultiPartRenderer
    - CoreJSONRenderer
- _BaseOpenAPIRenderer
    - OpenAPIRenderer
    - JSONOpenAPIRenderer
#### 
ViewSetMixin
    as_view
        包装: view
ViewSet(ViewSetMixin, views.APIView)
GenericViewSet(ViewSetMixin, generics.GenericAPIView)
ReadOnlyModelViewSet(RetrieveModelMixin,ListModelMixin,GenericViewSet)
ModelViewSet(mixins.CreateModelMixin,
                   mixins.RetrieveModelMixin,
                   mixins.UpdateModelMixin,
                   mixins.DestroyModelMixin,
                   mixins.ListModelMixin,
                   GenericViewSet)
#### Response
- HttpResponseBase
    - HttpResponse
        - SimpleTemplateResponse(默认)
            调用: render()
            - TemplateResponse
#### 权限部分
Django 自带
- AccessMixin
    - LoginRequiredMixin
    - PermissionRequiredMixin
    - UserPassesTestMixin
rest framework中的
- BasePermission
    - AllowAny
    - IsAuthenticated
    - IsAdminUser
    - IsAuthenticatedOrReadOnly
    - DjangoModelPermissions
        - DjangoObjectPermissions
        - DjangoModelPermissionsOrAnonReadOnly
#### django.core.handles.base.middleware
- process_view
- process_template_response
- process_exception
- __call__
    process_request
    process_response
#### 调用
- middleware
WSGIHandler.get_response
    self._middleware_chain
    self._get_response
        View.view
            # Ensure that the incoming request is permitted
            self.perform_authentication(request)
            self.check_permissions(request)
            self.check_throttles(request)
            View.dispatch
- rest framework
    View.dispatch
        self.initial(request, *args, **kwargs)
            self.perform_authentication(request)
            self.check_permissions(request)
            self.check_throttles(request)
# Apply view middleware