# 解析
```Option1
var param model.User
decoder := json.NewDecoder(c.Request.Body)
err := decoder.Decode(&param)
```
```Option2
var param model.User
bytes, err2 := c.GetRawData()
json.Unmarshal(bytes, &param)
```
