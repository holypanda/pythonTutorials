import random

random_int = random.randint(0, 100)
round_count = 0
while True:
    player_guess_num = int(input("猜一个数字，范围是0-100"))  # 有可能出错的代码
    if player_guess_num < random_int:
        print("你猜的数字太小了！")
    elif player_guess_num > random_int:
        print("你猜的数字太大了！")
    elif player_guess_num == random_int:
        print("你猜对了！")
        break
    round_count += 1
print("你猜了了" + str(round_count) + "次！")
