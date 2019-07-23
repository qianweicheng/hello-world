# [Jenkins](https://jenkins.io)
## pipeline分成两种
- Declarative(推荐)
- Scripted
## 安装部署
docker run --name jenkins -d -p 8080:8080 jenkins/jenkins:lts
docker run -it -v /var/run/docker.sock:/var/run/docker.sock -v /usr/bin/docker:/usr/bin/docker --name jenkins -d  -p 8080:8080 jenkins/jenkins:lts