# Helm
Kubernates 的包管理器
##Tiller 权限问题
kubectl create serviceaccount --namespace kube-system tiller
kubectl create clusterrolebinding tiller-cluster-rule --clusterrole=cluster-admin --serviceaccount=kube-system:tiller
kubectl patch deploy --namespace kube-system tiller-deploy -p '{"spec":{"template":{"spec":{"serviceAccount":"tiller"}}}}'
## helm init
## App Store
https://hub.kubeapps.com/
## 目前helm感觉是从一个URL下载一个文件夹，这个文件夹遵循一定的格式
可以使用任何一个文件服务器搭建一个helm的repo
官方默认的地址：https://github.com/helm/charts
https://kubernetes-charts.storage.googleapis.com
## 自带的repo
helm serve --repo-path ./
这个会扫描指定目录下的xxx.tgz文件，并生成一个index.yaml文件
## 本地预览
helm template mychart -x templates/deployment.yaml