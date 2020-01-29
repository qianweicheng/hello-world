# 添加新用户
三部曲:
- 为新用户生成一个密钥对，并用这个密钥生成一个证书请求
- 管理员用CA证书签发该秘钥请求，并将一个用户绑定到一个clusterrole里去
- 新用户通过集群证书,证书密钥，证书公钥三个文件生成一个context
## Demo
### 管理员
```
aws s3 cp s3://dev-k8s-easilydo-cc/dev.easilydo.cc/pki/private/ca/6746957810418909922336734849.key ca.key
aws s3 cp s3://dev-k8s-easilydo-cc/dev.easilydo.cc/pki/issued/ca/6746957810418909922336734849.crt ca.crt

openssl genrsa -out user_viewer.key 4096
openssl req -new -key user_viewer.key -out user_viewer.csr -subj '/CN=viewer/O=developer'
openssl x509 -req -in user_viewer.csr -CA ca.crt -CAkey ca.key -CAcreateserial -out user_viewer.crt -days 365

kubectl create clusterrolebinding edison-viewer-binding --clusterrole=view --user=viewer -n dev
```
### 用户端
```
aws s3 cp s3://dev-k8s-easilydo-cc/dev.easilydo.cc/pki/issued/master/6746957825513750933028685255.crt ca_master.crt
kubectl config set-cluster dev.easilydo.cc --server=https://api.dev.easilydo.cc
kubectl config set-cluster dev.easilydo.cc --certificate-authority=ca_master.crt
kubectl config set-credentials viewer --client-key=user_viewer.key --client-certificate=user_viewer.crt
kubectl config set-context dev.easilydo.cc --user=viewer --cluster dev.easilydo.cc
kubectl config use-context dev.easilydo.cc
```