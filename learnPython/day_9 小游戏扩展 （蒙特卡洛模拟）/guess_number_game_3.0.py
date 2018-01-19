import random


# 初始化游戏
def initialize_game(range_u):  # 抽象出游戏的范围
    random_int = random.randint(0, range_u)
    round_count = 0
    return random_int, round_count, range_u


# 玩家行动
def player_move():
    player_guess_num = int(input("猜一个数字，范围是0-100"))  # 有可能出错的代码
    return player_guess_num


# 比较数字
def compare_number(player_guess_num, random_int):
    if player_guess_num < random_int:
        # print("你猜的数字太小了！")
        return 2, player_guess_num  # 返回signal和猜的数
    elif player_guess_num > random_int:
        # print("你猜的数字太大了！")
        return 1, player_guess_num  # 返回signal和猜的数
    elif player_guess_num == random_int:
        # print("你猜对了！")
        return True, True


# 自动判断
# 初始化上限为100， 下限为0
# 信号=1说明猜测太大， 信号=2说明猜测太小 （信号=signal）
# 信号=None说明为第一回合， 直接返回默认上限和下限
def update_upper_and_lower(range_u, player_guess_num=None, signal=None, upper_b=100, lower_b=0):
    if signal is not None:
        if signal == 1:
            upper_b = player_guess_num
        elif signal == 2:
            lower_b = player_guess_num
        return upper_b, lower_b
    elif signal is None:
        upper_b = range_u
        lower_b = 0
        return upper_b, lower_b


def guess_number(upper_b, lower_b):  # signal 为大小信号， player_guess_num为上一次我们猜的数

    return int((upper_b - lower_b) / 2) + lower_b

# 之前的主函数改为模拟游戏函数
def stimulate_game(range_u):
    # 初始化变量
    random_int, round_count, range_u = initialize_game(range_u)
    signal, player_guess_num = None, None
    while True:
        try:
            # 如果signal和player_guess_num 为None，则是第一回合，否则就不是第一回合
            if signal is None and player_guess_num is None:  # 不是第一回合
                upper_b, lower_b = update_upper_and_lower(range_u)  # 更新上下限
                player_guess_num = guess_number(upper_b, lower_b)  # 产生猜测数字

            elif upper_b - lower_b == 1:  # 增加一种新的可能 防止陷入死循环
                print(upper_b, lower_b)
                player_guess_num = upper_b
                print("upper! " + str(player_guess_num))

            else:  # 第一回合
                upper_b, lower_b = update_upper_and_lower(range_u, player_guess_num, signal, upper_b, lower_b)  # 更新上下限
                player_guess_num = guess_number(upper_b, lower_b)  # 产生猜测数字

            signal, player_guess_num = compare_number(player_guess_num, random_int)  # 输入游戏
            print(player_guess_num, signal, lower_b, upper_b, random_int)
            if signal is True and player_guess_num is True:  # 如果这个函数返回的为True，就打算这个循环，游戏结束。
                round_count += 1
                break
            else:
                round_count += 1
        except ValueError:
            print("请输入一个数字整数。")
    print("你猜了了" + str(round_count) + "次！")
    return range_u, round_count

# 新的主函数
# 模拟游戏的运行很多次
# 并记录每一次游戏的参数和结果
def main():
    game_result = []
    for i in range(2,1000):
        upper_range, round_count = stimulate_game(i)
        game_result.append((upper_range, round_count))
    for game in game_result:
        print("数字上限为%s, 所用回合数为%s" % (game[0], game[1]))
    
main()