# 安装python3.5.2
操作系统：Windows 10

官网地址：https://www.python.org/

下载地址：https://www.python.org/downloads/

- 找到python3.5.2， -> download -> Windows x86-64 executable installer <br>
- 勾选 Add Python 3.5 to PATH
- Advanced Options 下勾选所有选项（除了最后两个 Download debugging symbols 和 Download debug binaries）
- 安装路径要记住，待会可能要配置环境变量
- 安装完成猴 用win+r， 输入cmd 打开命令行，命令行输入python，没有报错即安装成功
- 报错的话，把安装路径配置到环境变量里
- 至此你的python环境已经搭建好了！

## 配置python.exe 到环境变量
- 右键我的电脑->属性->高级系统设置->环境变量
- 在用户变量里面编辑Path，如果没有就新建
- 新建或浏览路径，把python的安装路径 "...\Python\Python35" 添加至Path,确认配置
- 用win+r， 输入cmd 打开命令行，命令行输入python，成功运行则配置环境变量成功
