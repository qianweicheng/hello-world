# Container
- Chroot Jail：一个进程的文件系统隔离起来
- FreeBSD Jails： 它是操作系统级别虚拟化技术的先驱之一
- Linux VServer：Linux 内核的系统级别的虚拟化功能实现的专用虚拟服务器
- Solaris Containers：
- OpenVZ：它允许创建多个安全隔离的 Linux 容器，即 VPS。
- Process Containers：
- LXC：这也是一种操作系统级别的虚拟化技术，允许使用单个Linux内核在宿主机上运行多个独立的系统
- Warden
- LMCTFY
- Docker
- RKT：专注于安全和开放标准的应用程序容器引擎。
- kata container
- cri-containerd
- cri-o
- 强隔离容器
  - Kata
  - gVisor
  - firecracker
## Open Container Initiative(倡议) (OCI)
The Open Container Initiative (OCI) created a runtime specification that details the API for an OCI-compatible runtime.
- runC: uses Linux cgroups and namespaces to provide isolation.
- Kata Containers: is a member of OCI and the Kata Containers runtime, kata-runtime, will be OCI-compatible.
## Container Runtime Interface (CRI) provided in Kubernetes.
A container runtime is the component that handles the lifecycle of a container, implementing basic concepts such as creating, starting, stopping and removing a container workload.

## Docker 如何运行一个容器？
- Docker引擎创建容器映像
- 将容器映像传递给 containerd
- containerd 调用 containerd-shim
- containerd-shim 使用 runC 来运行容器
- containerd-shim 允许运行时(本例中为 runC)在启动容器后退出
## References
- https://medium.com/kata-containers/why-kata-containers-doesnt-replace-kubernetes-75e484679727
- https://www.stackhpc.com/kata-io-1.html