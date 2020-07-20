# Mac Software Trial Forever
原理：
>拦截启动程序，使用脚本在每次启动的时候删除配置文件夹里面相应的注册信息
## 具体步骤（这里假设程序名字为`Victim`）
1. 程序的根目录下(`/Users/$(whoami)/Applications/Victim/Contents/MacOS`),将本身的主程序重命名为`Victim.real`
2. 然后新建一个脚本命名为`Victim.sh`
    ```bash
    #!/bin/bash
    rm "/Users/$(whoami)/Library/Application\ Support/Victim/the-register-file"
    rm "/Users/$(whoami)/Library/Preferences/Victim/xxxx"
    $(dirname $0)/Victim.real $@
    ```
3. 将脚本`chmod a+x Victim.sh`
## Preference文件路径
```
/Library/Application Support/
~/Library/Application\ Support/
~/Library/Preferences
```
## IntelliJ
```
cd ~/Library
rm -rf Logs/IntelliJIdeaxxx/ 
rm -rf Preferences/IntelliJIdeaxxx/
rm -rf Application\ Support/IntelliJIdeaxxx/
rm -rf Caches/IntelliJIdeaxxx
rm -rf ~/.idea
/Users/xxxx/Library/Preferences
```