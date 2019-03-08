# Openresty
Nginx + Lua, 集成了一些有用的nginx module的一个框架。
openresty命令本身也是一个快捷方式到nginx
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
## Install Kong: 
`luarocks install kong 1.0.2-0`
or
```
    $ git clone https://github.com/Kong/kong.git
    $ cd kong
    $ make install # this simply runs the `luarocks make kong-*.rockspec` command
```