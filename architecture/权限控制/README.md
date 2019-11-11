# 权限控制方式
- ACL：Access Control List，最简单的权限管理.常见的文件系统权限设计, 直接给用户加权限
- RBAC
  - RBAC0：这是RBAC的初始形态，也是最原始、最简单的RBAC版本；
  - RBAC1：基于RBAC0的优化，增加了角色的分层（子角色），子角色可以继承父角色的所有权限；
  - RBAC2：基于RBAC0的另一种优化，增加了对角色的一些限制：角色互斥、角色容量等；
  - RBAC3：最复杂也是最全面的RBAC模型，它在RBAC0的基础上，将RBAC1和RBAC2中的优化部分进行了整合
- ABAC：与 ACL 有点类似：非常繁琐，而且非常依赖于规则引擎，而这种引擎无法独立于系统，即需要与系统耦合在一起。
  - XACML
  - Casbin's ABAC is very simple
- PBAC: 基于策略的权限管理
- DAC:自主权限控制，常见于文件系统
- MAC：
> 其中ABAC和PBAC在互联网场景中很少使用，ACL是直接关系，RBAC是间接关系