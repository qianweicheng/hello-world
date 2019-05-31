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


Rasa问题
交互测试太差了
对英文支持不好

https://blog.csdn.net/u012526436/article/details/82911565
https://blog.csdn.net/u012526436/article/details/88061902
https://rasa.com
https://github.com/zqhZY/_rasa_chatbot.git