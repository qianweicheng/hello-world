# Swagger
官网: https://swagger.io/ 
GitHub地址: https://github.com/swagger-api
- 编辑Swagger
    - 在线收费版: https://app.swaggerhub.com/
    - 在线免费版: http://editor.swagger.io/
    - 自己DIY: https://github.com/swagger-api/swagger-editor
- 查看Swagger
    https://github.com/swagger-api/swagger-ui
- 代码生成
    https://github.com/swagger-api/swagger-codegen
    `brew install swagger-codegen`
## Go-Swagger
一个Golang版本的swagger，可以从文档生成代码，也可以从代码生成文档
https://github.com/go-swagger/go-swagger
https://goswagger.io/
- 查看:`swagger serve -p 8888 --no-open the-swagger-file-or-url`
- 代码生成:`swagger generate spec -o ./swagger.json`
## Generate spec form source
- swagger:meta  总文档
- swagger:route `swagger:operation`的简化版本，直接使用的是`swagger:response`
- swagger:params  用来做请求参数的实体
- swagger:operation 可以用来做复杂的API定义，可以通过yaml自定义
- swagger:response 定义相应类，包括了Body，Header等。必须有description
- swagger:model 定义实体类
## Tips
建议直接使用`swagger:operation`, 这样可以直接使用model定义response，简化实体定义类型
## 本人遇到的坑
在使用swagger:operation的时候，定义response出错了，注意一下对比(schema)
- response vs definitions
```
      responses:
        "200":
          description: success
          schema:
            $ref: '#/definitions/GroupListResponse'
      responses:
        "200":
          $ref: '#/responses/GroupListResponse'
```