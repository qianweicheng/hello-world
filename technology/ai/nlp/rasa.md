# Rasa
## 概念
1. Stories:可以理解为对话的场景流程
    |符号|说明|
    |-|-|
    |##|story 标题|
    |*|	意图|
    |-|	动作|

2. Domain:可以理解为机器的知识库
    |标识|说明|备注|
    |-|-|-|
    |intents|意图|
    |actions|动作|
    |templates|回答模板|
    |entities|实体|
    |slots|词槽|词槽是机器人的记忆力
## Install(rasa & rasax)
- Mac(Linux 没有成功)
http://rasa.com/docs/rasa/user-guide/installation/
https://github.com/RasaHQ/rasa
```
pip install rasa-x --extra-index-url https://pypi.rasa.com/simple
rasa init --no-prompt

# Solution 1
pip install rasa
# Solution 2
pip install rasa[spacy]
python -m spacy download en_core_web_md
python -m spacy link en_core_web_md en
```
- Using Docker
  `docker run -v $(pwd):/app rasa/rasa init --no-prompt`
## 文档
```
brew install sphinx
pip3 install -r requirements-dev.txt
make livedocs
```
## 文件结构
data/nlu.md contains training examples for the NLU model
data/stories.md contains training stories for the Core model
actions.py contains some custom actions
config.yml contains the model configuration
domain.yml contains the domain of the assistant
endpoints.yml contains the webhook configuration for the custom action
policy.py contains a custom policy
run.py contains code to train a Rasa model and use it to parse some text
## 启动
`rasa run -m models --enable-api --endpoint endpoints.yml --credentials credentials.yml
`
## RESTful API
/webhooks/rest/webhook
{
    "message": "hi"
}
/model/parse 
{
    "text": "hello"
}