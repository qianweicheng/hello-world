
# Service 
## 分成三类
1. ClusterIP
2. NodePort (default: 30000-32767)
3. LoadBalancer
4. Headless service:port 无需定义，不走service的port, pod 上的port在非NodePort情况下无需定义
## Service 的三种格式:
- xxxx
- xxxx.<namespace>
- xxxx.<namespace>.svc.cluster.local
##  普通service vs headless service(type:ClusterIP + clusterIP:None) 
1. There is a long history of DNS libraries not respecting DNS TTLs and caching the results of name lookups.
2. Many apps do DNS lookups once and cache the results.
3. Even if apps and libraries did proper re-resolution, the load of every client re-resolving DNS over and over would be difficult to manage.
## Discovering Services
- environment variables 
- DNS.
## Public Service
https://kubernetes.io/docs/concepts/services-networking/service/
https://kubernetes.io/docs/concepts/cluster-administration/cloud-providers/
- ClusterIP
- NodePort
- LoadBalancer
  - Internal load balancer: `service.beta.kubernetes.io/aws-load-balancer-internal: "true"`
  - TLS support on AWS: 
    - `service.beta.kubernetes.io/aws-load-balancer-ssl-cert: arn:aws:xxx`
    - `service.beta.kubernetes.io/aws-load-balancer-backend-protocol: (https|http|ssl|tcp)`
    - `service.beta.kubernetes.io/aws-load-balancer-proxy-protocol: "*"`
    - `service.beta.kubernetes.io/aws-load-balancer-ssl-ports: "443,8443"`
    - `service.beta.kubernetes.io/aws-load-balancer-ssl-negotiation-policy: "ELBSecurityPolicy-TLS-1-2-2017-01"`
- ExternalName