# Casbin
https://casbin.org/
https://casbin.org/docs/en/syntax-for-models
在 Casbin 中, 访问控制模型被抽象为基于PERM的一个文件。 因此，切换或升级项目的授权机制与修改配置一样简单。 您可以通过组合可用的模型来定制您自己的访问控制模型。 例如，您可以在一个model中获得RBAC角色和ABAC属性，并共享一组policy规则。

## Concept
策略: Policy，(可以多个)
效果: Effect
请求: Request，(可以多个)
匹配器: Matcher
角色: Role(可以多个)

## PERM模型
PERM(Policy, Effect, Request, Matchers)模型很简单, 但是反映了权限的本质 – 访问控制
这个模型规定了，谁(sub)可以对什么资源(obj)进行什么操作(act)。
角色: subject(用户可以与角色合并成为 subject，于是角色组也可以表示了)
资源: object
操作: action
model文件中四个必须: `[request_definition], [policy_definition], [policy_effect], and [matchers]`, `[role_definition]`可选
- Policy: 定义权限的规则.
    ```
    [policy_definition]
    p = sub, obj, act
    p2 = sub, act
    ```
    定义的每一行称为 policy rule, p, p2 是 policy rule 的名字. p2 定义的是 sub 所有的资源都能执行 act

- Effect: 定义组合了多个 Policy 之后的结果, allow/deny
    ```
    [policy_effect]
    e = some(where (p.eft == allow)) #表示有任意一条 policy rule 满足, 则最终结果为 allow
    e = !some(where (p.eft == deny)) #表示只要有一个规则被拒绝了，这个权限请求就会被拒绝
    ```

- Request: 访问请求, 也就是谁想操作什么
  - accessing entity (Subject)
  - accessed resource (Object)
  - the access method (Action)
  
  ```
    [request_definition]
    r = sub, obj, act
  ```

- Matcher: 判断 Request 是否满足 Policy
    ```
    [matchers]
    m = r.sub == p.sub && r.obj == p.obj && r.act == p.act
    ```
    定义了 request 和 policy 匹配的方式, p.eft 是 allow 还是 deny, 就是基于此来决定的
- Group/Role:
    ```
    [role_definition]
    g = _, _
    g2 = _, _
    g3 = _, _, _
    # g, g2, g3 表示不同的 RBAC 体系
    为了使用本身提供的API，最好遵照如下顺序_, _ 表示用户和角色 _, _, _ 表示用户, 角色, 域(也就是租户)

    ```
### 完整例子
```ACL中的model.conf
# Request definition
[request_definition]
r = sub, obj, act

# Policy definition
[policy_definition]
p = sub, obj, act

# Policy effect
[policy_effect]
e = some(where (p.eft == allow))

# Matchers
[matchers]
m = r.sub == p.sub && r.obj == p.obj && r.act == p.act
```
```ACL中policy.csv
p, alice, data1, read
p, bob, data2, write
```
```Code
e := casbin.NewEnforcer("./rbac_model.conf", "./rbac_policy.csv")
```