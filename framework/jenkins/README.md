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
## 项目类型
- Freestyle: 纯粹运行一些列脚本，这是Jenkins的核心，其他类型的project都是基于这个core，增加一个gradle解析器实现
- Pipeline： 两种格式，可以相互转换:
  - Declarative(声明式,推荐),`pipeline{}`
  - Scripted(高级), 是用Groovy写的:`node{}`
  - 一般流程
    - 指定一个代码库
    - 指定代码库中Jenkinsfile路径
    - workspace会在第一次运行的时候创建(可以清理掉，在下一次运行的时候重建)
- Mu l
## Integrate with k8s
https://blog.csdn.net/Andriy_dangli/article/details/85062813
## cases
- Case1
```
Jenkinsfile (Declarative Pipeline)
pipeline {
    agent { 
        docker 'python:3.5.1' 
    }
    environment {
        DISABLE_AUTH = 'true'
        DB_ENGINE    = 'sqlite'
    }
    stages {
        stage('build') {
            agent {
                docker {
                    image 'python:2-alpine' 
                }
            }
            steps {
                sh 'python --version'
                sh '''
                    echo "Multiline shell steps works too"
                    ls -lah
                '''
            }
        }
        stage('Test') {
            steps {
                sh './gradlew check'
            }
        }
    }
    post {
        always {
            echo 'This will always run'
        }
        success {
            echo 'This will run only if successful'
            slackSend channel: '#ops-room',
                  color: 'good',
                  message: "The pipeline ${currentBuild.fullDisplayName} completed successfully."
        }
        failure {
            echo 'This will run only if failed'
        }
        unstable {
            echo 'This will run only if the run was marked as unstable'
        }
        changed {
            echo 'This will run only if the state of the Pipeline has changed'
            echo 'For example, if the Pipeline was previously failing but is now successful'
        }
    }
}
```
