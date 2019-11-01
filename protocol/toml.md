# TOML
主要被golang使用(https://github.com/BurntSushi/toml)
## 数据类型
- 注释: `#开头`
- 字符串. TOML中有4种字符串表示方法：
  - 基本: 双引号
  - 多行-基本:
    ```
    str1 = """
    Roses are red
    Violets are blue"""
    ```
  - 字面量:单引号如`winpath = 'C:\Users\nodejs\templates'`
  - 多行-字面量
    ```
    str1 = '''
    Roses are red
    Violets are blue'''
    ```
- 数值与BOOL值
    ```
    int1 = +99
    flt3 = -0.01
    bool1 = true
    ```
- 日期时间:`date1 = 1979-05-27T07:32:00Z`
- 数组
- 表格