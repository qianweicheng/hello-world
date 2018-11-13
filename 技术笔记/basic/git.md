git 三大概念
1. 工作区：就是物理目录看到的
2. index暂存区,还有个叫stage的区
3. 本地分支
4. 远程分支
=======工作区，index的暂存区=====================
git clean -hfd 清理工作区
git add  是把文件从工作区提交到暂存区
git commit  把暂存区提交到本地分支

git diff 比较的是工作区和暂存区的差别
git diff --cached 比较的是暂存区和版本库的差别
git diff HEAD 可以查看工作区和版本库的差别
git checkout --file时，是将工作区指定修改的文件被暂存区的内容覆盖
git checkout HEAD --file 会将版本库中的对应的文件内容直接替换工作区和暂存区中的该文件
git rm --cached file 直接从暂存区进行文件的删除，不会影响工作区的内容
git revert 会产生新的提交记录
git reset,其中target是历史版本

          working index HEAD target         working index HEAD
           ----------------------------------------------------
            A       B     C    D     --soft   A       B     D
                                     --mixed  A       D     D
                                     --hard   D       D     D
                                     --merge (disallowed)
                                     --keep  (disallowed)

           working index HEAD target         working index HEAD
           ----------------------------------------------------
            A       B     C    C     --soft   A       B     C
                                     --mixed  A       C     C
                                     --hard   C       C     C
                                     --merge (disallowed)
                                     --keep   A       C     C

           working index HEAD target         working index HEAD
           ----------------------------------------------------
            B       B     C    D     --soft   B       B     D
                                     --mixed  B       D     D
                                     --hard   D       D     D
                                     --merge  D       D     D
                                     --keep  (disallowed)

           working index HEAD target         working index HEAD
           ----------------------------------------------------
            B       B     C    C     --soft   B       B     C
                                     --mixed  B       C     C
                                     --hard   C       C     C
                                     --merge  C       C     C
                                     --keep   B       C     C


#### checkout 远程分枝
git checkout -b [本地分枝名字] origin/remote-branch-name

#### delete 远程分枝
git push origin :remote-branch-name
git push origin -d remote-branch-name

git branch -r -d origin/branch-name
git push origin :branch-name  

#### 新建远程分支
1）git push origin local-branch-name
2）git push origin local-branch-name:remote-branch-name

#### 分支重命名
git branch - m old_name new_name

#### 远程库地址
git remote set-url origin URL
git remote rm origin 删除现有远程仓库 
git remote add origin url添加新远程仓库
git remote -v查看远程仓库的地址

#### .gitignore
https://git-scm.com/docs/gitignore
/folder/* 只匹配当前目录下的文件
/folder/** 匹配当前文件夹下所有

