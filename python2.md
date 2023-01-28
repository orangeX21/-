# **Python**运算符与判断

## 数据类型转换

**数据类型转换函数**

| **函数**                 | **说明**                                            |
| ------------------------ | --------------------------------------------------- |
| int(x [,base ])          | 将x转换为一个整数                                   |
| float(x)                 | 将x转换为一个浮点数                                 |
| complex(real  [,imag  ]) | 创建一个复数，real为实部，imag为虚部                |
| str(x)                   | 将对象 x  转换为字符串                              |
| repr(x)                  | 将对象  x  转换为表达式字符串                       |
| eval(str)                | 用来计算在字符串中的有效Python表达式,并返回一个对象 |
| tuple(s)                 | 将序列 s  转换为一个元组                            |
| list(s)                  | 将序列 s  转换为一个列表                            |
| chr(x)                   | 将一个整数转换为一个Unicode字符                     |
| ord(x)                   | 将一个字符转换为它的ASCII整数值                     |
| hex(x)                   | 将一个整数转换为一个十六进制字符串                  |
| oct(x)                   | 将一个整数转换为一个八进制字符串                    |
| bin(x)                   | 将一个整数转换为一个二进制字符串                    |

```python
# 案例1：input接收用户输入，用户输入“1”，将这个数据1转换成整型。
numbers1 = input("num:******")
print(f"你的数字是：{numbers1}")
print(type(numbers1))
#接收到的用户输入的数据类型 -- str类型
numbers1 = int(numbers1)
print(type(numbers1))
```

numbers : 123456789
你的数字是：123456789
`<class 'str'>`
`<class 'int'>`

3、将字符串中的数据转换成Python表达式==原本类型== => `eval()`



**超市收银系统案例升级**

```python

# name = input('请输入您购买商品名称：')
# id = int(input('请输入您购买商品编号：'))#int
# price = float(input('请输入您购买商品价格：')) #float
# print('您够买了%s，商品编号为%s，商品价格为%.2f，欢迎下次光临！' % (name, id, price)) #

```





## **运算符的使用**

### **运算符分类**

算术运算符[1](混合运算优先级顺序：( ) 高于 ** 高于 * / // % 高于 + - )

| **运算符** | **描述**     | **实例**                                                 |
| ---------- | ------------ | -------------------------------------------------------- |
| +          | 加           | 1 +  1 输出结果为  2                                     |
| -          | 减           | 1 -  1 输出结果为  0                                     |
| *          | 乘           | 2 *  2 输出结果为  4                                     |
| /          | 除           | 10  / 2 输出结果为  5                                    |
| //         | 整除         | 9  // 4 输出结果为2                                      |
| %          | 取余（取模） | 9 %  4 输出结果为  1                                     |
| **         | 指数         | 2  ** 4 输出结果为  16，即  2  * 2 * 2 * 2               |
| ()         | 小括号       | 小括号用来提高运算优先级，即  (1  + 2) * 3 输出结果为  9 |

**使用**Python **求梯形的面积**



![image-20220909114301945](C:\Users\29248\AppData\Roaming\Typora\typora-user-images\image-20220909114301945.png)
$$
S=(a+b)*h/2
$$

```python
# 使用Python求梯形的面积
# a=上底 b=下底 h=高
a = float(input("上底是:"))
b = float(input("下底:"))
h = float(input("高:"))
# 公式 s=(a+b)*h/2 s是答案
s = (a + b) * h / 2
print(f"梯形的面积:{s}")
```



**算术运算符**

| **运算符** | **描述**     | **实例**                                                 |
| ---------- | ------------ | -------------------------------------------------------- |
| +          | 加           | 1 +  1 输出结果为  2                                     |
| -          | 减           | 1 -  1 输出结果为  0                                     |
| *          | 乘           | 2 *  2 输出结果为  4                                     |
| /          | 除           | 10  / 2 输出结果为  5                                    |
| //         | 整除         | 9  // 4 输出结果为2                                      |
| %          | 取余（取模） | 9 %  4 输出结果为  1                                     |
| **         | 指数         | 2  ** 4 输出结果为  16，即  2  * 2 * 2 * 2               |
| ()         | 小括号       | 小括号用来提高运算优先级，即  (1  + 2) * 3 输出结果为  9 |

注意事项:<u>混合运算优先级顺序：`( )` 高于`` **`` 高于 ``*`` ``/`` ``//`` `% `高于 ``+`` ` -`</u>``



### 赋值运算符

单个变量赋值

```python
num = 1
print(num)
```

多个变量赋值

```python
num1,num2,num3,num888 = 10,3,9,"hallo word"
print(num1)
```

多变量赋相同值

```python
a=b=c=d=999
print(c)
```

### 复合赋值运算符

![image-20220909145250275](C:\Users\29248\AppData\Roaming\Typora\typora-user-images\image-20220909145250275.png)

例子： 

```text
a = 100
a += 1
# 输出101  a = a + 1,最终a = 100 + 1
print(a)

b = 2
b *= 3
# 输出6  b = b * 3,最终b = 2 * 3
print(b)

c = 10
c += 1 + 2
# 输出13, 先算运算符右侧1 + 2 = 3， c += 3 , 推导出c = 10 + 3
print(c)
```





### 比较运算符

![image-20220909150152472](C:\Users\29248\AppData\Roaming\Typora\typora-user-images\image-20220909150152472.png)



### 逻辑运算符



![image-20220909150345670](C:\Users\29248\AppData\Roaming\Typora\typora-user-images\image-20220909150345670.png)

`and`  和 ` `or` `  not`

```python
a = 1
b = 2
c = 3

print((a < b) and (b < c))  # True
print((a > b) and (b < c))  # False
print((a > b) or (b < c))     # True
print(not (a > b))               # True
```



## Python运算符练习题

圆的面积 $S = πr^2$ 

```python
# Python运算符练习题
# 圆的面积输入圆的半径
r = float(input("输入圆的半径:"))
T = 3.14
S = T * r ** 2
print(S)
```

```python 
输入圆的半径:2
12.56
```



练习题3：逻辑运算 => 输入三角形的3边，如果两边的长度大于第三条边，则代表是一个合法三角形

```python
# 输入三角形的3边 a,b,c

a = float(input("a:"))
b = float(input("b:"))
c = float(input("c:"))
a, b, c = float(a + 1 - 1), float(b + 1 - 1), float(c + 1 - 1)
print((a + b > c) and (b + c > a) and (a + c > b))

```

# **if**选择结构

**if**条件语句的基本语法

```text
if 条件:
    条件成立执行的代码1
    条件成立执行的代码2
    ......

```

```python
# 如果用户年龄大于等于18岁，即成年，输出"已经成年，可以上网"。
# 接受用户输入>判断
name = input("你的名字：")
print(f"你的名字：{name}")
age = int(input("你的年龄："))
print(f"你的年龄：{age}")
```

**if…elif …else多重判断语句**

```
if 条件1:
    条件1成立执行的代码1
    条件1成立执行的代码2
    ......
elif 条件2：
    条件2成立执行的代码1
    条件2成立执行的代码2
    ......
......
else:
    以上条件都不成立执行的代码

```



思考题：

① 中国合法工作年龄为18-60岁，即如果年龄小于18的情况为童工，不合法；

② 如果年龄在18-60岁之间为合法工龄；

③ 大于60岁为法定退休年龄。

```python
age = int(input("你的年龄："))
print(f"你的年龄：{age}")
if age < 18:
    print(f"年龄{age}情况为童工，不合法")
elif (age >= 18) or (age <= 60):
    print("年龄在18-60岁之间为合法工龄")
else:
    print("法定退休年龄")
```

**if**嵌套结构

```
if 条件1：
    条件1成立执行的代码
    条件1成立执行的代码
    
    if 条件2：
        条件2成立执行的代码
        条件2成立执行的代码
```

**猜拳案例**

需求：参与游戏的角色有两个（玩家 与 电脑），玩家手工出拳，电脑随机出拳，根据石头剪刀布判断输赢。大致有三种情况：

![image-20220909163208977](C:\Users\29248\AppData\Roaming\Typora\typora-user-images\image-20220909163208977.png)

```python
#需求：参与游戏的角色有两个（玩家 与 电脑），玩家手工出拳，电脑随机出拳，根据石头剪刀布判断输赢。大致有三种情况
import random
computer = random.randint(0,2)
player = int(input("请出拳：0-石头，1-剪刀，2-布："))
# 玩家胜利 p0:c1 或 p1:c2 或 p2:c0
if (player == 0 and computer == 1) or (player == 1 and computer == 2) or (player == 2 and computer == 0):
    print('玩家获胜')

# 平局：玩家 == 电脑
elif player == computer:
    print('平局')
else:
    print('电脑获胜')
    
```



## 三目运算符

三目运算符也叫三元运算符。

语法如下：

值1 if 条件 else 值2

求两个数的最大值：

```python
a = 1
b = 2

c = a if a > b else b
print(c)

```

