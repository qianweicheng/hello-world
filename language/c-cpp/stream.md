# Stream
打开文件夹集中模式truc会清除所有内容
istream
ostream
iostream

istringstream
ostringstream
stringstream

ifstream
ofstream
fstream

#include <iostream>
#include <sstream>
## 读取文件
in：打开文件时做读操作；
out：打开文件时做写操作；
app：在每次写之前找到文件尾；
ate：打开文件后立即将文件定位在文件尾；(与ios::app存在区别)
trunc：打开文件时清空已存在的文件流；
binary：以二进制模式进行IO操作；（默认时采用的是 文本文件模式）
// fstream pos(this->dbInfoPath, fstream::in | fstream::out);
// 使用string
// string bufstr;
// pos.seekg(0);
// getline(pos, bufstr);
// 使用 char
// char buf[10];
// pos.getline(buf, sizeof(buf))
