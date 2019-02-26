# PAM(Pluggable Authentication Modules)
配置文件格式: `<module interface>  <control flag>   <module name>   <module arguments>`
1. 第一列代表模块类型，类型分为4种：
- auth: 用来对用户的身份进行识别.如:提示用户输入密码,或判断用户是否为root
- account: 对帐号的各项属性进行检查.如:是否允许登录,是否达到最大用户数,或是root用户是否允许在这个终端登录等
- session: 这个模块用来定义用户登录前的,及用户退出后所要进行的操作.如:登录连接信息,用户数据的打开与关闭,挂载文件系统等.
- passwd: 使用用户信息来更新.如:修改用户密码.
2. 第二列代表控制标记：也有4种类型：
- required: 表示即使某个模块对用户的验证失败，也要等所有的模块都执行完毕后,PAM 才返回错误信息。这样做是为了不让用户知道被哪个模块拒绝。如果对用户验证成功，所有的模块都会返回成功信息
- requisite: 与required相似,但是如果这个模块返回失败,则立刻向应用程序返回失败,表示此类型失败.不再进行同类型后面的操作.
- sufficient: 表示如果一个用户通过这个模块的验证，并且前面无失败，PAM结构就立刻返回验证成功信息，把控制权交回应用程序。后面的层叠模块即使使用requisite或者required 控制标志，也不再执行。如果验证失败，sufficient 的作用和 optional 相同
- optional:表示即使本行指定的模块验证失败，也允许用户接受应用程序提供的服务，一般返回PAM_IGNORE(忽略).
- include: 引入改项指定文件中的所有配置项
- substack 和include类似。不同之处在于，对子堆中的完成和失败的行为的评估不会导致跳过整个模块堆栈的其余部分，而只会跳过子模块。
3. 第三列代表模块路径：要调用模块的位置一般是在/lib(x64)/security文件中, 但是每个版本都不太一样.
    模块|管理类型|说明
    pam_unix.so|auth,account,passwd|读取/etc/shadow
    pam_shells.so|auth,account|/etc/shells
    pam_limits.so|session|/etc/security/limits.conf,/etc/security/limits.d/*.conf
    pam_env.so|auth|/etc/security/pam_env.conf
    pam_deny.so|account,auth,passwd,session|拒绝服务
    pam_permit.so|auth,account,passwd,session|模块任何时候都返回成功
    pam_securetty.so|auth|如果root,则tty必须在/etc/securetty里面
    pam_cracklib.so|passwd|密码强度检测器
4. 第四列是模块参数
## 判断一个模块是否使用pam
`ldd /usr/sbin/sshd | grep pam`