## 安装 Data Integration(Kettle)
https://community.hitachivantara.com/docs/DOC-1009855

#### 解决双击启动不了的问题
>   `sudo xattr -dr com.apple.quarantine /Applications/data-integration/Data\ Integration.app`
实际启动脚本：./spoon.sh

#### Kettle 控件
1. tranformation
    - variable(environment variables)
        也就是tranformation上的parameter(参数)， 使用${}获取
    - parameter(命名参数)
        SQL 参数:`?`
    - argument(位置参数)
        Positional arguments
    自己通过
    获取前一步的参数，我们必须使用Parameters
2. job
    parameter 跟tranformation 的parameters一样