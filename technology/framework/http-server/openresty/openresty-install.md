# Openresty Install
- 直接下载 binary packages
- `brew install openresty/brew/openresty`
- make from source code
## Source Code Compline
- 编译pcre: ftp://ftp.csx.cam.ac.uk/pub/software/programming/pcre/
    ./configure && make && make install
- 编译openssl: https://www.openssl.org/source/openssl-1.1.1a.tar.gz
    ./config && make && make install
- 编译openresty: https://openresty.org/en/download.html
    ```
    ./configure \
    --with-pcre-jit \
    --with-http_ssl_module \
    --with-http_realip_module \
    --with-http_stub_status_module \
    --with-http_v2_module
    ```
 - 编译luarocks: http://luarocks.github.io/luarocks/releases/luarocks-3.0.4.tar.gz
    ```
    ./configure \
    --lua-suffix=jit \
    --with-lua=/usr/local/openresty/luajit \
    --with-lua-include=/usr/local/openresty/luajit/include/luajit-2.1
   ```
## Plugins
两种包安装方式:
- opm 安装包默认是全局模式, 文件都会被放在 `/usr/local/openresty/site/` 路径下
- luarocks:
    ```
    luarocks install luasql-sqlite3
    luarocks install luasql-postgres
    luarocks install luasql-mysql
    luarocks install luasql-sqlite
    luarocks install luasql-odbc
    ```
#### Install Kong: 
- 包管理库`luarocks install kong 1.0.2-0`
- or 源代码安装
```
    $ git clone https://github.com/Kong/kong.git
    $ cd kong
    $ make install # this simply runs the `luarocks make kong-*.rockspec` command
```
#### 常用第三方插件
- kong: 一个插件平台的插件
- lapis
- lor:一个web开发框架
## 插件开发
