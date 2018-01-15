import random


# 初始化游戏
def initialize_game():
    random_int = random.randint(0, 100)
    round_count = 0
    return random_int, round_count


# 玩家行动
def player_move():
    player_guess_num = int(input("猜一个数字，范围是0-100"))  # 有可能出错的代码
    return player_guess_num


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


def main():
    random_int, round_count = initialize_game()
    while True:
        try:
            player_guess_num = player_move()
            if compare_number(player_guess_num, random_int):  # 如果这个函数返回的为True，就打算这个循环，游戏结束。
                round_count += 1
                break
            else:
                round_count += 1
        except ValueError:
            print("请输入一个数字整数。")
    print("你猜了了" + str(round_count) + "次！")


main()
