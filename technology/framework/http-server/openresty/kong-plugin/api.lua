local crud = require "kong.api.crud_helpers"

return {
  ["/myplugin/"] = {
    before = function(self, dao_factory, helpers)
        ngx.log(ngx.ERR, 'before api')
    end,

    GET = function(self, dao_factory)
      crud.paginated_set(self, dao_factory.myplugin)
    end,

    PUT = function(self, dao_factory)
      crud.put(self.params, dao_factory.myplugin)
    end,

    POST = function(self, dao_factory)
      crud.post(self.params, dao_factory.myplugin)
    end
  }
}
