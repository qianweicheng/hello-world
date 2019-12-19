# Jenkins
[Jenkins](https://jenkins.io)
[Hello-world](https://jenkins.io/doc/pipeline/tour/hello-world/)
## Install
macos: `brew install jenkins`
``` docker
docker run \
  --rm \
  -u root \
  -d \
  -p 8080:8080 \
  -v /var/run/docker.sock:/var/run/docker.sock \
  -v /usr/bin/docker:/usr/bin/docker  \
  jenkins/jenkins:lts
```
``` docker with blueocean
mkdir jenkins-data
docker run \
  --rm \
  -u root \
  -p 8080:8080 \
  -v ./jenkins-data:/var/jenkins_home \
  -v /var/run/docker.sock:/var/run/docker.sock \
  -v "$HOME":/home \
  jenkinsci/blueocean
```
## Concept
- Project(Job):
- Folder: 树状结构，便于管理project,如权限控制等(project本身在文件系统还是扁平结构)
- View: 就是一个project的filter
## Integrate with k8s
https://blog.csdn.net/Andriy_dangli/article/details/85062813
## Webhook
- 内置的: `/github-webhook/`
- 在gitserver上配置webhook的secret
## 项目类型
- Freestyle: 
  - 纯粹运行一些列脚本，这是Jenkins的核心，其他类型的project都是基于这个core，增加一个gradle解析器实现
  - 提供任务管理，日记管理，触发器等
  - 可以配置代码库，直接下载整个项目，然后全部使用自定义脚本进行处理
  - 但我们由于需要使用docker镜像进行构建，以及使用密码管理，所有使用pipeline会表方便
- Pipeline
  - Pipeline文件管理方式：
    - local pipeline
      - 不会自动拉取代码，需要在pipeline文件里面添加
    - pipeline from scm
      - 拉取pipeline的时候自动把pipeline对于的scm库拉取下来了
      - 可以指定Jenkinsfile的路径和分支
  - 两种格式（可以相互转换）:
    - Declarative(声明式,推荐),`pipeline{}`
    - Scripted(高级), 是用Groovy写的:`node{}`
  - 一般流程
    - 指定一个代码库
    - 指定分支
    - 指定代码库中Jenkinsfile路径
    - workspace会在第一次运行的时候创建(可以清理掉，在下一次运行的时候重建)
- MultiBranch Pipeline
  - 跟pipeline类似
  - 只不过不指定分支，通过扫描分支下是否存在Jenkinsfile自动进行，相对来说灵活性少了一些
## Pipeline优势
- 流水线上的代码评审/迭代
- 对流水线进行审计跟踪
- 流水线的单一可信数据源，能够被项目的多个成员查看和编辑。
## 插件
- Authorize Project
- Role-based Authorization Strategy
## 权限
一个用户必须拥有global_role和project_role(可选)，
- global role中必须要overall的read权限，并且控制所有project的权限
- project rold 根据正则控制单个项目的权限