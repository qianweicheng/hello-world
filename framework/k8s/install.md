# Install
注意版本，如果客户端版本比服务器版本低，则容易出`Error from server (NotFound): the server could not find the requested resource`错误
- 安装kubectl
  - MacOS:
    ```
    curl -LO "https://storage.googleapis.com/kubernetes-release/release/$(curl -s https://storage.googleapis.com/kubernetes-release/release/stable.txt)/bin/darwin/amd64/kubectl"
    chmod +x ./kubectl
    sudo mv ./kubectl /usr/local/bin/kubectl
    ```
- 安装kops(https://github.com/kubernetes/kops)
  - MacOS: `brew update && brew install kops`
  - Linux: 
    ```
        curl -LO https://github.com/kubernetes/kops/releases/download/$(curl -s https://api.github.com/repos/kubernetes/kops/releases/latest | grep tag_name | cut -d '"' -f 4)/kops-linux-amd64
        chmod +x kops-linux-amd64
        sudo mv kops-linux-amd64 /usr/local/bin/kops
    ```
