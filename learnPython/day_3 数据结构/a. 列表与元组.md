# 数据结构
在python里面，常用的数据结构分别是
- 列表 [ ]
- 元组 ( )
- 字典 { }

## 列表 list [ ]
&emsp; 列表是一种有序的集合,可以容易的对列表的进行增加，删除，或者排序。在
python里用 [ ] 创建列表。
```python
fruit = ["apple", "banana", "cherry"]
print(fruit) # --> ["apple", "banana", "cherry"]
```
- 用 [index]来表示列表的下标，取出列表的元素。 注意程序员从0开始数数，所以苹果的下标为0,超出下标会报错。
```python
print(fruit[0])  # --> "apple"
print(fruit[1])  # --> "banana"
print(fruit[2])  # --> "cherry"
print(fruit[3]) # -->error
```
- 下标也可以到过来数，倒过来从-1开始
```python
print(fruit[-3])  # --> "apple"
print(fruit[-2])  # --> "banana"
print(fruit[-1])  # --> "cherry"
```
- 也可以一次取几个下标 用:表示
```python
print(fruit[0:3])  # --> ["apple", "banana", "cherry"]
```
### 列表的几种常用方法
- len(), 计算出列表的长度
```python
print(len(fruit)) # --> 3
```

- append() 在列表的最后面增加一个元素
```python
fruit.append("grape")
print(fruit) # --> ["apple", "banana", "cherry", "grape"]
print(len(fruit)) # --> 4
```

- insert(index, things_to_insert) 把元素插入到列表指定位置
```python
fruit.insert(1,"grape")
print(fruit) # -->["apple", "grape", "banana", "cherry"]
```

- pop() 删除并取出列表的末尾元素
```python
fruit = ["apple", "banana", "cherry", "grape"]
fruit.pop() # --> "grape"
print(fruit) # --> ["apple", "banana", "cherry"]
```

- 替换列表中的某个元素
```python
fruit[0] = "orange"
print(fruit) # --> ["orange", "banana", "cherry", "grape"]
```

## 元组
&emsp;元组和列表几乎一样，但是元组初始化后不能更改，所以元组没有insert(),append()
等方法。取出元组中的元素的方法和列表一样。
- 初始化一个元组() 并取出下标0
```python
fruit = ("apple", "banana", "cherry")
print(fruit[0]) # "apple"
```

- 如果初始化的元组只有一个元素，需要在后面加逗号
```python
fruit = (1,)
```
