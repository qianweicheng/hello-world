# luarocks
官网: https://luarocks.org
https://github.com/luarocks/luarocks/wiki/Creating-a-rock
## 命令
`/usr/local/bin/luarocks [<flags...>] [VAR=VALUE]... <command> [<argument>]`
`luarocks --help`
## 步骤
#### 生成rockspec
- 手动生成rockspec文件
- 自动:`luarocks write_rockspec`
#### 配置
- source指定src的位置
- build指定src包含的文件等编译信息
#### Building(本地安装)
`luarocks make # like make in c/c++`
根据当前文件夹的rockspec编译打包放到本地的rock tree  
#### 手动打包
- `luarocks pack luafruits-1.0-1.rockspec` 生成 `luafruits-1.0-1.src.rock`
- `luarocks pack <plugin-name> <version>`生成包含二进制的`luafruits-1.0-1.linux-x86.rock`
#### 上传,rock server自动生成rock文件。
`luarocks upload your-rockspec-name.rockspec --api-key=xxxx`
