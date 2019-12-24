# UUID
https://tools.ietf.org/html/rfc4122.html
https://en.wikipedia.org/wiki/Universally_unique_identifier
## 标准格式
UUID的格式是这样的：xxxxxxxx-xxxx-Mxxx-Nxxx-xxxxxxxxxxxx  
128byte=16Byte=Hex(8-4-4-4-12)=21.3(Base64)
- M那个位置，代表版本号，由于UUID的标准实现有5个版本，所以只会是1,2,3,4,5
- N那个位置(variants)，正常使用只会是8,9,a,b(10xx),下面四个中的第二个
  - 0xxx:  backwards compatibility with the now-obsolete
  - 10xx: referred to as RFC 4122/DCE 1.1 UUIDs (8,9,a,b这四种可能)
  - 110x: reserved, Microsoft Corporation backward compatibility
  - 111x: future variants
## UUID有多个版本
- UUID Version 1：基于时间的UUID
  基于时间的UUID通过计算当前时间戳（60bits),机器MAC地址(48bits)和序列号(13/14-bits)得到.也可以使用退化的算法，以IP地址来代替MAC地址－－Java的UUID往往是这样实现的
- UUID Version 2：DCE安全的UUID
  DCE安全的UUID和基于时间的UUID算法相同，但会把时间戳的前4位置换为POSIX的UID或GID。不过，在UUID的规范里面没有明确地指定，所以基本上所有的UUID实现都不会实现这个版本
- UUID Version 3：基于名字的UUID(MD5)
  基于名字的UUID通过计算名字和名字空间的MD5散列值得到,这个版本的UUID保证了：相同名字空间中不同名字生成的UUID的唯一性；不同名字空间中的UUID的唯一性；相同名字空间中相同名字的UUID重复生成是相同的。`uuid.uuid3(uuid.NAMESPACE_DNS, "myString")`. Only 121 or 122 bits contribute to the uniqueness of the UUID.
- UUID Version 4：随机UUID.总共122-123 bits随机
- UUID Version 5：基于名字的UUID(SHA1). 和版本3一样，不过散列函数换成了SHA1
### UUID V1
Name|Length|Contents
-|-|-
time_low|8|integer giving the low 32 bits of the time
time_mid|4|integer giving the middle 16 bits of the time
time_hi_and_version|4|4-bit "version" in the most significant bits, followed by the high 12 bits of the time
clock_seq_hi_and_res clock_seq_low|4|1 to 3-bit "variant" in the most significant bits, followed by the 13 to 15-bit clock sequence
node|12|the 48-bit node id

27cc9574-230c-11ea-b3ca-c4b301bdc0df
1c252622-230d-11ea-b3ca-c4b301bdc0df
359f7364-230d-11ea-b3ca-c4b301bdc0df
### UUID V4
cc6b33b5-723d-47f5-86a1-37d1ccadb82c
19b51b52-9dd9-4c54-9bc5-c017f4aa8ac1
### 总结
- Version 1/2: (内部使用首选)适合应用于分布式计算环境下，具有高度的唯一性。缺点:
    - 并且很多语言需要通过第三方库，或者自己做一个简单封装.
    - 安全性风险
      - 容易被猜测(前8位是毫秒数)
      - 会暴露机器的MAC或IP地址，但可以通过一定的方法避免该问题。
- Version 3/5: 本质是通过namespace和name做md5/sha1，相同的namespace和name在任何时候都生成相同的uuid，理论上跟v4一样存在冲突。
- Version 4: (入门首选)它是最简单最方便的，各种语言基本默认支持，前提是能够允许冲突或检测到冲突然后进一步处理。 在高并发的环境下，其实概率比较高了。
## 参考
- Birthday problem(https://en.wikipedia.org/wiki/Birthday_problem)
- Google搜索: `UUID collisions`
## 生成UUID
- `cat /proc/sys/kernel/random/uuid`
- `uuidgen` or 
- `dbus-uuidgen`(无分隔符)