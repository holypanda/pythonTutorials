# 封装

&emsp;封装的意思就是把一条一条命令，封装成一个一个的函数。（初步封装）
使我们的代码看起来更加简介，并且重用性更高。

&emsp;让我们来分析我们的小游戏，然后吧我们的小游戏封装的更加简洁吧。

## 猜数字游戏的结构
- 初始化游戏
```python
# 初始化游戏
def initialize_game():
    random_int = random.randint(0, 100)
    round_count = 0
    return random_int, round_count
```
- 玩家行动
```python
# 玩家行动
def player_move():
    player_guess_num = int(input("猜一个数字，范围是0-100"))  # 有可能出错的代码
    return player_guess_num
```

- 比较判断
```python
# 比较数字
def compare_number(player_guess_num, random_int):
    if player_guess_num < random_int:
        print("你猜的数字太小了！")
        return False
    elif player_guess_num > random_int:
        print("你猜的数字太大了！")
        return False
    elif player_guess_num == random_int:
        print("你猜对了！")
        return True
```
- 我们把我们的小游戏分成三个函数，然后再设置一个主函数包裹我们这三个函数
```python
def main():
    random_int, round_count = initialize_game()
    while True:
        try:
            player_guess_num = player_move()
            if compare_number(player_guess_num, random_int): # 如果这个函数返回的为True，就打算这个循环，游戏结束。
                round_count += 1
                break
            else:
                round_count += 1
        except ValueError:
            print("请输入一个数字整数。")
    print("你猜了了" + str(round_count) + "次！")
```
- 调用我们的主函数
```python
main()
```

- 虽然这么写，我们代码的行数增加了，但是整个游戏的结构更加清晰，易于以后维护或者扩展这个游戏。
- 如果只看主函数的话 (main()),主函数的逻辑更加的清晰了。