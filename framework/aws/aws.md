# AWS
## 安装awscli
```
    # install pip if it's not already
    $ wget https://bootstrap.pypa.io/get-pip.py && python get-pip.py
    $ pip3 install awscli
```
- config aws
```
    aws configure
        AWS Access Key ID: THE-ID
        AWS Secret Access 
        Key: THE-KEY
        Default region: us-west-2
        Default output format: json
```
## 开发
boto3 用来管理AWS的各种资源，对redshift等操作需要使用单独的包
## AWS elastic filesystem
- 挂载一个efs磁盘到当前系统: `mount -t efs fs-f1118e58:/ efs`
- `mount -t file-system-id.efs.aws-region.amazonaws.com`
- `mount -t nfs4 -o nfsvers=4.1,rsize=1048576,wsize=1048576,hard,timeo=600,retrans=2 172.31.9.135:/ efs`
## DB
- Redshift 使用psycopg2包操作，但copy_from/expect等不支持，需要使用execute直接写SQL
## LB
只支持TCP，不支持UDP
## Filesystem
- 修改volume大小
    - `aws ec2 modify-volume --region us-east-1 --volume-id vol-11111111111111111 --size 20 --volume-type gp2`
    - `aws ec2 modify-volume --volume-id vol-070a7796c8543f11d --size 44` 
- `aws ec2 describe-volumes-modifications --region us-east-1 --volume-id vol-111`