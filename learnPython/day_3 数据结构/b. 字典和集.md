## 字典
- 字典是一种无序的数据结构，是有键-值（key-val）的储存，拥有很快的查找速度
- 初始化一个字典 { }
```python
article = {

    "id" = 89757,
    "title" = "Python"
    "content" = "Life is short, I use python."
}
```
- 以上等号左边为键， 等号右边为值， 当我们需要查找相对应的值的时候，只要输入
等号左边的键即可.注意 每一个键只能对应一个值
```python
print(article["id"]) # --> 89757
print(article["title"]) # --> "Python"
print(article["content"]) # --> "Life is short, I use python."
```
- 替换调字典中的内容
```python
article["id"] = 123456
print(article["id"]) # --> 123456
```
- 常用的字典方法
- xxx.keys() 找到字典中所有的键，储存为列表
- xxx.values() 找到字典中所有的值，储存为列表
```python
article_keys = article.keys()
article_values = article.values()
print(article_keys)
print(article_values)
```

## 集 set()
&emsp; python里集合中的元素不可以重复，所以set可以用来去重
- 初始化一个set
```python
my_set = set(["a","a","b","b"])
print(my_set) # --> {"a","b"}
```
- set常用的方法
- xxx.add 添加一个元素 添加相同元素无效果
- xxx.remove 删除一个元素
```python
my_set.add("c")
print(my_set) # -->　{"a", "b", "c"}
my_set.remove("a") --> {"b", "c"}
```

- set与set之间的操作
- & 选出set与set之间重复的元素
- | 合并set，并且不会出现重复元素
```python
set_a = set([1,2,3])
set_b = set([2,3,4])
set_same = set_a & set_b
set_combine = set_a | set_b
print(set_same) # --> {2,3}
print(set_combine) # --> {1,2,3,4}
```

