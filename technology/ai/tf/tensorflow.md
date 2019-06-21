# Tensorflow
TensorFlow有一个极好的可视化工具TensorBoard
Keras

## Install 
`pip install tensorflow`
https://www.tensorflow.org/
## 使用
tensorflow-lite
tensorflow.js
Swift, R, etc.
## 资源
- https://github.com/ageron/tf2_course
- http://www.tensorfly.cn/tfdoc/tutorials/overview.html
- https://proandroiddev.com/using-tensorflow-in-android-step-by-step-code-explanation-fee36c281f32
- https://github.com/tensorflow/models
## 入门
#### 步法
- 构造网络模型 
- 编译模型 
- 训练模型 
- 评估模型 
- 使用模型进行预测  
#### 网络结构：由10种基本层结构和其他层结构组成 
- 激活函数：如relu，softmax等
    对于多分类的情况，最后一层是softmax。 
    其它深度学习层中多用relu。 
    二分类可以用sigmoid。 
    另外浅层神经网络也可以用tanh。
- 损失函数：
    categorical_crossentropy多分类对数损失
    binary_crossentropy对数损失
    mean_squared_error平均方差损失
    mean_absolute_error平均绝对值损失
- 优化器：
    SGD随机梯度下降
    RMSProp
    Adagrad 自适应梯度下降
    Adadelta 对于Adagrad的进一步改进
    Adam
#### 9种基本层模型：
- 3种主模型： 
    ‍全连接层Dense 
    卷积层：如conv1d, conv2d 
    循环层：如lstm, gru  
- 3种辅助层
    Activation层 
    Dropout层 
    池化层
- 3种异构网络互联层： 
    嵌入层：用于第一层，输入数据到其他网络的转换 
    Flatten层：用于卷积层到全连接层之间的过渡 
    Permute层：用于RNN与CNN之间的接口