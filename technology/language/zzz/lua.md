# lua
包管理器: luarocks
## 语法
- 注释: `--` or `-[==[  ]==]`
- 数据结构：
    - nil
    - boolean
    - number
    - string: ',",[[]], `[==[ xxx ]==]`等号数相等就OK，表示切除[[随后的一个回车
    - function
    - table: 可以表示数组，默认都是1开始
        ```
        local a1 = {1,2,3,4}
        local t1 = {
            one=1,
            [key]=value, -- key可以有特殊字符
            two=2; -- 可以逗号或者分号
        }
        ```
- 运算符: `+,-,*,/,%,^,==,~=(不等于),>,<, and,or,not,..` 
## 原型(metatable)
- setmetatable
