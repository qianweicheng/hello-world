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
## 其他
Rasa
https://www.jianshu.com/p/7f8ca4ac16e7
https://blog.csdn.net/qfire/article/details/78964212
https://github.com/zqhZY/_rasa_chatbot
http://www.crownpku.com/2017/07/27/用Rasa_NLU构建自己的中文NLU系统.html
python多版本管理
https://blog.csdn.net/coding_dong/article/details/80343756
https://www.leiphone.com/news/201801/vACDb4p98FqcmJVA.html
https://www.cnblogs.com/qcloud1001/p/8391212.html
https://blog.csdn.net/starzhou/article/details/71304843
http://www.shareditor.com/blogshow/?blogId=121
http://www.shareditor.com/blogshow?blogId=63

书籍
Make Your Own Neural Network

matlab替代品
octave

https://github.com/rasahq


Jupyter

https://rasa.com/docs/get_started_step3/


sudo pip install -r requirements.txt --user
sudo pip install -e . --user
pip install --upgrade pip

doc
https://rasa.com/docs/get_started_step2/

python 2，3兼容
https://blog.csdn.net/u014259820/article/details/81023224

https://blog.rasa.com/level-3-contextual-assistants-beyond-answering-simple-questions/?_ga=2.182158433.754151901.1550471106-1744593422.1550471106

语料库
https://github.com/crownpku/awesome-chinese-nlp
https://blog.csdn.net/hfutdog/article/details/78155467

具体实战例子
https://www.leiphone.com/news/201801/vACDb4p98FqcmJVA.html

Botbit
https://github.com/howdyai/botkit

训练集
https://blog.csdn.net/u010505246/article/details/83276354

北邮代码
https://github.com/zqhZY/_rasa_chatbot.git

阅读进度

https://rasa.com/docs/nlu/choosing_pipeline/
https://github.com/terrifyzhao/rasa-tutorial


照这个来
https://blog.csdn.net/u012526436/article/details/82911565
https://blog.csdn.net/u012526436/article/details/88061902


模型训练

https://www.jianshu.com/p/4ecd09be4419


python -m rasa_core.train -d domain.yml -s stories.md -o models/dialogue

python -m rasa_core.train -d domain_1.yml -s stories_1.md -o models_1/dialogue


python -m rasa_core.run -d models/dialogue

python -m rasa_core.run -d models_1/dialogue

python -m rasa_nlu.train -c nlu_config.yml --data data/nlu.md -o models_1 --fixed_model_name nlu --project current --verbose

python -m rasa_nlu.train -c nlu_config.yml --data nlu.md -o models --fixed_model_name nlu --project current --verbose

python -m rasa_core.run -d models_1/dialogue -u models_1/current/nlu

python -m rasa_core.run -d models/dialogue -u models/current/nlu

中文 nlp

https://github.com/crownpku/Rasa_NLU_Chi



sudo pip install -U rasa_core —user
sudo pip install rasa_nlu[tensorflow] —user



https://github.com/fendouai/Awesome-Chatbot.git


聊天机器人

http://www.shareditor.com/bloglistbytag/?tagname=自己动手做聊天机器人

入门好材料
http://www.shareditor.com/blogshow/?blogId=73


https://www.jianshu.com/p/3c6f1e32e128

从头开始讲
https://yq.aliyun.com/articles/277285#1


https://blog.csdn.net/u012526436/article/details/82911565
https://blog.csdn.net/u012526436/article/details/88061902
https://rasa.com
https://github.com/zqhZY/_rasa_chatbot.git