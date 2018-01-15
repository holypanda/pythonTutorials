
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