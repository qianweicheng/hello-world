##MyBatis三要素
- Entity
- Mapper
- JavaClient

##MyBatis传入参数的几种方式：
- 直接使用参数名(只适合单个参数)
- 使用序列号
- 使用Map封装
- @Param参数注解
##MyBatis的repo定义方式(两者可以同时使用)
- 声明式（annotation）
- XML配置式
##Mabatis三剑客:
- mybatis-generator
    配置文件顺序有要求
- mybatis-plugin
- mybatis-pagehelper
##aliases
- 设置XML或者application.yml里面设置package
- XML里面设置typeAlias
- 在注解里面设置