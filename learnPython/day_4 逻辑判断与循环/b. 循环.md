# 循环
- for 循环
- while 循环

## for 循环
&emsp; for 的写法是for...in...,可以理解成，对列表里的每一个对象进行处理
```python
fruit_list = ["apple", "banana", "cherry"]
for fruit in fruit_list:  # 对fruit_list里面的fruit做以下操作
    print(fruit)
```

## while 循环
&emsp; while循环的写法是 while 条件， 意思是 当条件成立时，做以下操作
```python
i = 0
while i<=10: # 当i小于等于10的时候 我们做以下操作
    print(i)
    i += 1   # i 等于 i+1
```
- while True 循环就是死循环， 程序会一直运行下去，除非手动关闭 （ctrl+c）
```python
while True:
    print("I am not going to stop!!!")
```

## break 和 continue
- break 打断
- continue 跳过
&for循环和while循环都可以break或者continue
- break语句可以打断循环，配合逻辑判断可以实现在某种情况下打断循环
```python
i = 0
while: # 当i小于等于10的时候 我们做以下操作
    print(i)
    i += 1   # i 等于 i+1
    if i <=10:
        break
```

- continue可以跳过当前循环，配合逻辑判断可以实现某种情况下的跳过
```python
fruit_list = ["apple", "banana", "cherry"]
for fruit in fruit_list:  # 对fruit_list里面的fruit做以下操作
    if fruit == "apple":
        continue
    print(fruit)
```