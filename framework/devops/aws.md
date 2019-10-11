# AWS
## 开发
boto3 用来管理AWS的各种资源，对redshift等操作需要使用单独的包
Redshift 使用psycopg2包操作，但copy_from/expect等不支持，需要使用execute直接写SQL
sudo mount -t efs fs-f1118e58:/ efs
## AWS elastic filesystem
sudo mount -t file-system-id.efs.aws-region.amazonaws.com
sudo mount -t nfs4 -o nfsvers=4.1,rsize=1048576,wsize=1048576,hard,timeo=600,retrans=2 172.31.9.135:/ efs
## LB
只支持TCP，不支持UDP
## Filesystem
- `aws ec2 modify-volume --region us-east-1 --volume-id vol-11111111111111111 --size 20 --volume-type gp2`
- `aws ec2 describe-volumes-modifications --region us-east-1 --volume-id vol-11111111111111111`
- `kubectl get node -o wide`