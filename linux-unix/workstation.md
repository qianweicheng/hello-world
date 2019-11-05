# workstation
## iTerm2
新的终端,内置了一个简单的Tmux，但建议安装独立的(http://iterm2.com/downloads.html)
- 文本复制
- 智能选中
- 窗口面板管理
- 及时回放(⌘+opt+b)
### 使用
```
cmd+t new tab
cmd+w close tab
cmd+num switch tab
cmd+enter full screen
cmd+d split screen by vertical
cmd+shift+d split screen by horizontal
```
## zsh:新的shell
- Install: `curl -L http://install.ohmyz.sh | sh`
chsh [-s 修改默认] /bin/zsh
配置文件在 .zshrc, 类似.bash_profile+.bash_rc的作用
oh-my-zsh安装文件在$ZSH所指代的目录下
- 强大的插件主题
## mosh:新的ssh
- 使用UDP协议，在弱网络环境下优势明显
  - server side: mosh-server
  - client side: mosh 
- Install
  - Client本地可以使用
    - `brew install mosh`
    - chrome mosh插件
  - 服务器
    - Source
      ```
      # 准备编译环境
      yum groupinstall "Development Tools"
      # https://mosh.org/#getting 里面需要预选安装一些依赖
      yum install -y openssl-devel ncurses-devel protobuf-compiler protobuf-devel
      wget https://mosh.org/mosh-1.3.2.tar.gz
      tar mosh-1.3.2
      cd mosh-1.3.2
      ./configure & make & make install
      ```
    - Yum: `yum install -y mosh`
## tmux
Terminal Multiplexer，一个多终端进程管理器
- 分屏功能
- session保持: 退出了终端，但session可以继续
- Install `yum install tmux`
- 启动：`tmux`
- 配置文件`.tmux.conf`在每个用户home目录
### 窗格操作
% 左右平分出两个窗格
" 上下平分出两个窗格
x 关闭当前窗格
{ 当前窗格前移
} 当前窗格后移
; 选择上次使用的窗格
o 选择下一个窗格，也可以使用上下左右方向键来选择
space 切换窗格布局，tmux 内置了五种窗格布局，也可以通过 ⌥1 至 ⌥5来切换
z 最大化当前窗格，再次执行可恢复原来大小
q 显示所有窗格的序号，在序号出现期间按下对应的数字，即可跳转至对应的窗格
### 窗口操作
c 新建窗口，此时当前窗口会切换至新窗口，不影响原有窗口的状态
p 切换至上一窗口
n 切换至下一窗口
w 窗口列表选择，注意 macOS 下使用 ⌃p 和 ⌃n 进行上下选择
& 关闭当前窗口
, 重命名窗口，可以使用中文，重命名后能在 tmux 状态栏更快速的识别窗口 id
0 切换至 0 号窗口，使用其他数字 id 切换至对应窗口
f 根据窗口名搜索选择窗口，可模糊匹配
### 会话操作
$ 重命名当前会话
s 选择会话列表
d detach 当前会话，运行后将会退出 tmux 进程，返回至 l 主进程

tmux new -s foo # 新建名称为 foo 的会话
tmux ls # 列出所有 tmux 会话
tmux a # 恢复至上一次的会话
tmux a -t foo # 恢复名称为 foo 的会话，会话默认名称为数字
tmux kill-session -t foo # 删除名称为 foo 的会话
tmux kill-server # 删除所有的会话


