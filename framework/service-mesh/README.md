# Service Mesh
## 参考文档
https://legacy.gitbook.com/book/feisky/kubernetes/details
## 概述
在传统模式下，代理一般是集中式的单独的服务器，所有的请求都要先通过代理，然后再流入转发到实际的后端。
Service Mesh 中，代理变成了分布式的，它常驻在了应用的身边（最常见的就是 Kubernetes Sidecar 模式，每一个应用的 Pod 中都运行着一个代理，负责流量相关的事情）, 可以看做是传统代理的升级版，用来解决现在微服务框架中出现的问题，可以把 Service Mesh 看做是分布式的微服务代理。
Kubernetes(k8s)
## K8s vs Istio
k8s并不是因为微服务而生而是因为docker而生只是天时地利人和正好赶上了微服务流行的时代，docker的特性正好特别适用于微服务，而k8s进一步对docker方便的编排。
从基础设施方向来讲k8s可以比作是IDC机房和机房工作人员，对物理服务器（docker）的存放与管理，上机架、装系统、接网络等等。从微服务的角度来讲，k8s通过基础设施的方式通过逻辑抽象出service等概念提供了对微服务的另一种实现，就好比用N台电脑联网提供了FTP服务。
Kubernetes本身是支持微服务的架构，在Pod中部署微服务很合适，也已经解决了微服务的互访互通问题，但对服务间访问的管理如服务的熔断、限流、动态路由、调用链追踪等都不在Kubernetes的能力范围内。
Kubernetes只提供了4层负载均衡能力，无法基于应用层的信息进行负载均衡，更不会提供应用层的流量管理，在服务运行管理上也只提供了基本的探针机制，并不提供服务访问指标和调用链追踪这种应用的服务运行诊断能力。
## Concept 
数据平面(data plane)：一般用来做快速转发
控制平面(control plane)：为快速转发提供必要的信息
## 主要功能
- 服务发现(discovery)
- 负载均衡(load balancing)
- 故障恢复(failure recovery)
- 服务度量(metrics)
- 服务监控(monitoring)
- A/B测试(A/B testing)
- 灰度发布(canary rollouts)
- 限流限速(rate limiting)
- 访问控制(access control)
- 身份认证(end-to-end authentication)