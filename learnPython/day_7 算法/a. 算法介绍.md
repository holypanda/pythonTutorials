# 算法 algorithm
- 算法就是一种计算发的方法
- 从一个初始状态，经过一系列的逻辑运算，最后得出一个结果。
- 比如，我有一个1到10的列表，我要在里面找到一个5，用python写
```python
a_list = [1,2,3,4,5,6,7,8,9,10]
for number in a_list:
    if number == 5:
        print(number, " found!")
```
## 算法的时间复杂度
- 在我们做的小游戏里，最暴力的算法是从0一直迭代到100 （从0开始尝试，一直到100）
- 那么最坏的结果是我们尝试100次后得到答案
- 时间复杂度就为：f(n) = n （意思是有n种可能，我们最多需要n次尝试）
- 若复杂度为 f(n) = n^2 (有n种可能，我们最多需要尝试n^2次）
