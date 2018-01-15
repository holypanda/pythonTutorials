# 函数
&emsp;函数就像是预先定义的一个工具，或者一套命令，当你调用这个函数的时候，
会自动运行你自定义的工具，或者你你自定义的命令。函数可以预先输入一下参数，
也可以返回一些数据。

## 定义函数 def
- def 你的函数名(参数1，参数2，参数3，...):
- return 关键字定义要返回那些变量
```python
def say_hello(name):
    print("hello " + str(name) + "!")
    return name
```

## 调用函数
- 调用我们刚才定义的函数
- hello_name 接受函数返回的数据
```python
hello_name = say_hello("小明")
print(hello_name) # --> 小明
```