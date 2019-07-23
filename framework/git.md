# git 
文档: https://git-scm.com/docs
## 概念
- 工作区：就是物理目录看到的
- index暂存区,还有个叫stage的区
- 本地分支
- 远程分支
## 常用命令
清理工作区: `git clean -hfd`
把文件从工作区提交到暂存区:`git add`
把暂存区提交到本地分支: `git commit`
比较的是工作区和暂存区的差别:`git diff`
比较的是暂存区和版本库的差别:`git diff --cached`
可以查看工作区和版本库的差别:`git diff HEAD`
将工作区指定修改的文件被暂存区的内容覆盖: `git checkout --file`
将版本库中的对应的文件内容直接替换工作区和暂存区中的该文件: `git checkout HEAD --file`
直接从暂存区进行文件的删除，不会影响工作区的内容: `git rm --cached file`
回滚(产生新的提交记录):  `git revert`
## 分支操作
删除远程分支: `git push origin :remote-branch-name` or `git push origin -d remote-branch-name`
新建远程分支: `git push origin local-branch-name` or `git push origin local-branch-name:remote-branch-name`
签出远程分枝: `git checkout -b [本地分枝名字] origin/remote-branch-name`
关联远程分支: `git push --set-upstream origin remote-branch-name`
删除本地分支: `git branch -r -d origin/branch-name`
重命名本地分支: `git branch -m old_name new_name`
远程库地址:
关联远程库: `git remote set-url origin URL`
添加新远程仓库: `git remote add origin url`
删除现有远程仓库: `git remote rm origin`
查看远程仓库的地址: `git remote -v`
查看本地分支和远程分支对应关系: `git branch -vv`
查看本地分支: `git symbolic-ref --short -q HEAD`
查看当前提交号: `git rev-list @`
查看是否有更新: 
    `git remote -v update; git rev-list HEAD...origin/master --count`
    or 
    ```
    git remote -v update; \
    current_branch=$(git branch | awk '/\*/{print $2}'); \
    LOCAL=$(git rev-parse @); \
    REMOTE=$(git rev-parse origin/$current_branch); \
    [[ "$LOCAL" != "$REMOTE" ]] && echo "HAS UPDATE"
    ```
"local is behind" and "local has diverged"
## Merge
合并某次提交: `git cherry-pick commit-id`
合并: `git merge`
## .gitignore
https://git-scm.com/docs/gitignore
/folder/* 只匹配当前目录下的文件
/folder/** 匹配当前文件夹下所有

## git reset 工作区/index的暂存区(其中target是历史版本)
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
## Etc
查看远程跟本地分支的差距
`git rev-list --left-right --count master...origin/master`
`git fetch && git branch -sb`