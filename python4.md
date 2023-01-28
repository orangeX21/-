<center>study day 4</center>

# FOR循环结构

## **基本语法**

```
for 临时变量 in 序列:
    重复执行的代码1
    重复执行的代码2
    ......

```

案例演示

```python
str1 = "atheism"
for i in str1:
    print (i, end="")
```

执行结果：

```
atheism
```

## **range****函数基础用法**

Python 2 `range()` 函数返回的是<u>列表</u>，而在Python 3中 `range()` 函数返回的是一个<u>可迭代对象（类型是对象）</u>，而不是列表类型， 所以打印的时候不会打印列表。（由于我们还未学习面向对象，为了方便大家理解，你可以简单的将其理解为一个==序列结构==）

基本语法：

```python
range(stop)
range(start, stop[, step])
```

`start`: 计数从 start 开始。默认是从 0 开始。例如range（5）等价于range（0， 5）;
`stop`: 计数到 stop 结束，但不包括 stop。例如：range（0，5） 是 [0, 1, 2, 3, 4] 没有 5
`step`：步长，默认为1。例如：range（0，5） 等价于 range(0, 5, 1)



案例演示：

```python
for i in range(9):
    print(i,end=" ")

for i in range(1,7):
    print(i,end=" ")

for i in range(12,36,6):
    print(i,end="*")
```

```
0 1 2 3 4 5 6 7 8 1 2 3 4 5 6 12*18*24*30*
```

案例1：求1-100的和

```python
result = 0
for i in range(101):
    result+=i
print(f'1-100的和为：{result}')
```

```
1-100的和为：5050
```



求1-100之间所有偶数的和

```python
result = 0
for i in range(101):
    if i % 2 == 0:
        result += i
print(f'1-100的所有偶数的和为：{result}')
```

```
1-100的所有偶数的和为：2550
```

**循环中的两大关键词**

案例：打印`itheima`字符串中的每个字符，遇'e'终止循环

```python
result ="itheima"
for i in result:
    if i == "e":
        print('遇到e不打印')
        break
    print(i)
```



打印`itheima`字符串中的每个字符，遇'e'跳过循环

```python
result ="itheima"
for i in result:
    if i == "e":
        print('遇到e不打印')
        continue
    print(i)
```



**for** **循环案例**

案例：用for循环实现用户登录

① 输入用户名和密码

② 判断用户名和密码是否正确（``username`=`admin`，`password`=`admin888`） 

③ 登录仅有三次机会，超过3次会报错 

```python
for i in range(3):
    username = input("username:")
    print(f"username:{username}")
    password = input("password:")
    print(f"password:{password}")
    if username == "admin":
        if password == "admin888":
            print(f"用户名:{username}正确 密码正确 --登陆成功")
        else:
            print("用户名正确 密码错误 --登陆失败 ")
            continue
    else:
        print("用户名错误  -- 登陆失败 ")
        continue

```

for循环嵌套

所谓for循环嵌套，就是一个for循环里面嵌套另外一个for循环的写法。

当循环结构相互嵌套时，位于外层的循环结构常简称为外层循环或外循环，位于内层的循环结构常简称为内层循环或内循环。

```
# 外层循环
for i in 序列1:
    普通程序...
    # 内层循环
    for j in 序列2:
        普通程序...
```

① 循环嵌套结构的代码，Python 解释器执行的流程为：<u>当外层循环条件为 True 时，则执行外层循环结构中的循环体</u>

② 外层循环体中包含了普通程序和内循环，<u>当内层循环的循环条件为 True 时会执行此循环中的循环体，直到内层循环条件为 False，跳出内循环</u>

③ <u>如果此时外层循环的条件仍为 True，则返回第 2 步，继续执行外层循环体，直到外层循环的循环条件为 False</u>

④ <u>当内层循环的循环条件为 False，且外层循环的循环条件也为 False，则整个嵌套循环才算执行完毕</u>

使用for循环嵌套编写 9 x 9 乘法表

```python
for i in range(1, 10):
    for j in range(1, i+1):
        print(f'{j}*{i}={j*i}', end='\t')
    print('')

```

## while循环else结构

循环可以和else配合使用，else下方缩进的代码指的是当循环==正常结束==之后要执行的代码。

需求：女朋友生气了，要惩罚：连续说5遍“老婆大人，我错了”，如果道歉正常完毕后女朋友就原谅我了，这个程序怎么写？



