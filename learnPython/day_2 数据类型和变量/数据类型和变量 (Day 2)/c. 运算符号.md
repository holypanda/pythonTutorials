# 运算符号
&emsp;python支持各类的运算符号，运算规则也是从左到右，从括号内都括号外。
- 加 +
- 减 -
- 乘 *
- 除 /
- 地板除 //
- 模 %

&emsp; 加减乘除很简单,和一般运算规则一样. 下面主要说需要注意的地方.

## 字符串相加
- 字符串可以和字符串相加
```python
a = "你追我如果你追到我,"
b = "我就让你"
c = "嘿嘿嘿!"
d = a+b+c
print(d)   #你追我如果你追到我,我就让你嘿嘿嘿!
```
- 字符串不能与整数或者浮点数相加，需要先转换成同类型
```python
a = "1"
b = 1
c = int(a) + b
d = a + str(b)
print(c) # 2
print(d) # "11"
```
- 浮点与整数
- + 浮点+整数=浮点
- + 浮点+浮点=浮点
- + 整数+整数=整数

## 除法 /
- 两个数相除为浮点数 (即使两个都是整数)

## 地板除 //
- 两个数相地板除为整数
- 相当于两个数相处,再把小数点切掉
```python
a = 10//3
b = int(10/3)
print(a) # 3
print(b) # 3
```

## 模 %
- 相当于求余数,得到的结果为整数
```python
a = 10 % 3
print(a) # 1
```
- 一些小规则
- + 如果左边的数比右边的数小，模的结果为左边的数
- + 如果左边的数等于右边的数，模的结果为0
- + 如果左边的数大于右边的数，模的结果为余数
```python
a = 1 % 3
b = 2 % 3
c = 3 % 3
d = 4 & 3
print(a, b, c, d) # 1 2 0 1
```
