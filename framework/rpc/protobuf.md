# protobuf
文档：https://developers.google.com/protocol-buffers/
- protobuf
  - https://github.com/protocolbuffers/protobuf
  - libprotobuf-c 负责编解码
  - c++实现，集成了大部分语言。
  - c语言支持在[protobuf-c](https://github.com/protobuf-c/protobuf-c)
  - golang支持插件在[protoc-gen-go](https://github.com/golang/protobuf)，通过$GOPATH/bin找到`protoc-gen-go`。 插件主要用来生成code
  - dart支持在另外的`dart-lang/protobuf`
- protobuf-c：Protocol Buffers implementation in C
  - libprotobuf-c 负责编解码
  - protobuf-c 将 `.protoc`转换成c代码
  - 新版本将rpc部分分离到`protobuf-c-rpc`项目