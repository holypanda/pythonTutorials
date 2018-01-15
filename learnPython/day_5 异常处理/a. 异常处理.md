# 异常处理
&emsp;今天我们基于我们写的猜数字游戏来讲python里面的异常处理
- 猜数字游戏代码
```python
import random

random_int = random.randint(0, 100)
round_count = 0
while True:
    player_guess_num = int(input("猜一个数字，范围是0-100"))
    if player_guess_num < random_int:
        print("你猜的数字太小了！")
    elif player_guess_num > random_int:
        print("你猜的数字太大了！")
    elif player_guess_num == random_int:
        print("你猜对了！")
        break
    round_count += 1
print("你猜了了" + str(round_count) + "次！")
```

&emsp;昨天有折腾这个游戏的小伙伴，应该会发现，这个游戏很容易崩溃，比如我在输入我要猜的数字的时候，输入了中文(五十)
```
猜一个数字，范围是0-100五十
Traceback (most recent call last):
  File "C:/Users/38086/PycharmProjects/PythonTutorial/pythonTutorials/learnPython/day_4 逻辑判断与循环/实战1 猜数字游戏/guess_number_game.py", line 6, in <module>
    player_guess_num = int(input("猜一个数字，范围是0-100"))
ValueError: invalid literal for int() with base 10: '五十'
```
&emsp;这是因为 在第六行代码，python期待我们输入的是一个int，或者可以转化为int的字符串
```python
player_guess_num = int(input("猜一个数字，范围是0-100")) #这里只能输入int，或者可以转换成int的字符串
```
&emsp;而我输入了“五十”，python转换不了，所以报了 ValueError 这个错误

## 异常处理
&emsp;异常处理的代码很好理解，就是尝试运行你的代码，如果发生了某种异常，就运行别的代码（默认为任何异常）
```python
try:
    代码
except 异常:
    就做什么
```
&emsp;我们只要用异常处理把有可能出错的代码包裹起来，并提供解决方案或者提示，一般就可以解决问题。
以我们的游戏为例子
```python
import random

random_int = random.randint(0, 100)
round_count = 0
while True:
    try:
        player_guess_num = int(input("猜一个数字，范围是0-100"))  # 有可能出错的代码
        if player_guess_num < random_int:
            print("你猜的数字太小了！")
        elif player_guess_num > random_int:
            print("你猜的数字太大了！")
        elif player_guess_num == random_int:
            print("你猜对了！")
            break
        round_count += 1
    except ValueError:  # ValueError 为我们捕捉的异常
        print("请用数字输入一个整数。")  # 提供合理的解决方案，或者提示。
print("你猜了了" + str(round_count) + "次！")
```
&emsp;虽然捕捉的异常我们不填写，这个程序也能顺畅的运行（默认捕捉所有异常）。
但是一般来说，为了方便解决问题，我们希望精准的捕捉我们的异常，然后精准的给出提示或者解决方法。
但是，在某些特殊的情况，我们也可以捕捉所有异常，然后直接跳过这个异常，运行下一个循环。