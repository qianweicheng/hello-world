# 消息格式
```
[
  b'u-u-i-d',         # zmq identity(ies)
  b'<IDS|MSG>',       # delimiter
  b'baddad42',        # HMAC signature
  b'{header}',        # serialized header dict
  b'{parent_header}', # serialized parent header dict
  b'{metadata}',      # serialized metadata dict
  b'{content}',       # serialized content dict
  b'\xf0\x9f\x90\xb1' # extra raw data buffer(s)
  ...
]
```
## 发送一条命令
<IDS|MSG>
c7f315ac07c459083f66394451f06a9f629c878fcc541c360796ca3d34494815
{"msg_id":"7e54aeb9b8a64d86822549829c15c2d6","username":"username","session":"7ce7e7acf63f4b9f9b1e6720baf128dc","msg_type":"execute_request","version":"5.2","date":"2019-11-01T03:53:46.122349Z"}
{}
{}
{"code":"pwd","silent":false,"store_history":true,"user_expressions":{},"allow_stdin":true,"stop_on_error":true}

## 订阅了iopub端口，在收到一条client的指令之后的消息
response: kernel.74f0fb4d-8413-43dd-8f83-7eda729fd9c4.status
response: <IDS|MSG>
response: 6dc1d55a2956790b3f467fc7e4b897f4f549d06eac5e235941958f025a83ae81
response: {"msg_id":"1163ac14-e3e4c9e16070b1799d99f08e","msg_type":"status","username":"qianweicheng","session":"f5fa08c5-9f224e081e67698ad03997d1","date":"2019-11-01T03:32:18.741431Z","version":"5.3"}
response: {"msg_id":"1b2c12f606154858a3f03acfba0eb5a1","username":"username","session":"7ce7e7acf63f4b9f9b1e6720baf128dc","msg_type":"execute_request","version":"5.2","date":"2019-11-01T03:32:18.737756Z"}
response: {}
response: {"execution_state":"busy"}

response: kernel.74f0fb4d-8413-43dd-8f83-7eda729fd9c4.execute_input
response: <IDS|MSG>
response: 9f797a97cab4ed2511ff4c5f52f2a20f8d2a095720aabc0107fb1a9a835d97c7
response: {"msg_id":"9c3b0cff-9099b02b3097237e5b9aa033","msg_type":"execute_input","username":"qianweicheng","session":"f5fa08c5-9f224e081e67698ad03997d1","date":"2019-11-01T03:32:18.743107Z","version":"5.3"}
response: {"msg_id":"1b2c12f606154858a3f03acfba0eb5a1","username":"username","session":"7ce7e7acf63f4b9f9b1e6720baf128dc","msg_type":"execute_request","version":"5.2","date":"2019-11-01T03:32:18.737756Z"}
response: {}
response: {"code":"pwd","execution_count":5}

response: kernel.74f0fb4d-8413-43dd-8f83-7eda729fd9c4.execute_result
response: <IDS|MSG>
response: 44bc09cd56737387892a4b60b81f0898ec9ed6a564814393c78ed2ba542d6e0b
response: {"msg_id":"0f052609-31e3497a721bf07acb284561","msg_type":"execute_result","username":"qianweicheng","session":"f5fa08c5-9f224e081e67698ad03997d1","date":"2019-11-01T03:32:18.747267Z","version":"5.3"}
response: {"msg_id":"1b2c12f606154858a3f03acfba0eb5a1","username":"username","session":"7ce7e7acf63f4b9f9b1e6720baf128dc","msg_type":"execute_request","version":"5.2","date":"2019-11-01T03:32:18.737756Z"}
response: {}
response: {"data":{"text/plain":"'/Users/qianweicheng/work'"},"metadata":{},"execution_count":5}

response: kernel.74f0fb4d-8413-43dd-8f83-7eda729fd9c4.status
response: <IDS|MSG>
response: ad0018b273e2be8958083c854ede0f2eb7961937bc4a694f3dc5915e8e5d32ab
response: {"msg_id":"e19db7e4-d4cc6808106d7c192b939c86","msg_type":"status","username":"qianweicheng","session":"f5fa08c5-9f224e081e67698ad03997d1","date":"2019-11-01T03:32:18.768805Z","version":"5.3"}
response: {"msg_id":"1b2c12f606154858a3f03acfba0eb5a1","username":"username","session":"7ce7e7acf63f4b9f9b1e6720baf128dc","msg_type":"execute_request","version":"5.2","date":"2019-11-01T03:32:18.737756Z"}
response: {}
response: {"execution_state":"idle"}