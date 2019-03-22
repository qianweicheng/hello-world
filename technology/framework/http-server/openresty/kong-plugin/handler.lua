local BasePlugin = require "kong.plugins.base_plugin"

local MyPluginHandler = BasePlugin:extend()

function MyPluginHandler:new()
  MyPluginHandler.super.new(self, "myplugin")
end

function MyPluginHandler:access(conf)
  MyPluginHandler.super.access(self)
  kong.response.set_header("X-Foo", "weicheng-haha")
  kong.log(conf.environment) -- "development"
  kong.log(conf.server.host) -- "http://localhost"
  kong.log(conf.server.port) -- 8080
end

MyPluginHandler.PRIORITY = 1000
MyPluginHandler.VERSION = "0.1.0"

return MyPluginHandler
