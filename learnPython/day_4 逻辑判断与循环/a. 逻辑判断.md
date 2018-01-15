# 逻辑判断
- if 如果
- elif 如果不满足上一个if或者elif
- else 否则

&emsp; 逻辑判断能帮助你写出比较智能的程序。
## if和elif的区别
- if 一定会判断，而elif只有在上一层判断失败的时候，才会判断。
- 下面这个小程序会说明一个简单的逻辑判断。
```python
your_age = int(input("What's your age?")) # 输入年龄

if type(your_age) is int: # 如果年龄是个整数，那就进入下一层逻辑判断

    if 0 < your_age < 10: # 如果年龄在0到10之间
        print("Your are a baby!")
    elif 10 <= your_age < 20: #如果年龄在10到20之间
        print("Your are a teenager!")
    elif your_age >= 20: # 如果年龄大于20
        print("Your are an adult!")
    else: # 否则
        print("Plesae input a valid age.")
else:
    print("Please input a valid age.")
```

## 常用运算符号
- ">" 大于, ">=" 大于等于
- "<" 小于, "<=" 小于等于
- "==" 等于 （注意等于要用两个等号，一个等号是变量的赋值）
