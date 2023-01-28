# **函数递归**

递推算法：递推算法是一种简单的算法，即通过==已知条件==，利用==特定条件==得出中间推论，直至得到结果的算法。

递推又分为顺推和逆推。

* 顺推：通过最简单的条件，然后逐步推演结果

* 逆推：通过结果找到规律，然后推导已知条件

![image-20221113165851158](C:\Users\29248\AppData\Roaming\Typora\typora-user-images\image-20221113165851158.png)

**递归的概念**

程序调用自身的编程技巧称为递归（ recursion）。

递归做为一种算法在程序设计语言中广泛应用，它通常==把一个大型复杂的问题层层转化为一个与原问题相似的规模较小的问题来求解==，递归策略只需少量的程序就可描述出解题过程所需要的多次重复计算，大大地减少了程序的代码量。

① 简化问题：找到最优子问题（不能再小） 

② 函数自己调用自己

![image-20221113170049263](C:\Users\29248\AppData\Roaming\Typora\typora-user-images\image-20221113170049263.png)

<center>斐波那契数列</center>

需求：求指定位置的数据   找规律：第一个数是1，第二个数1，从第三个数开始：结果等于前两个数的和

递归有两个非常重要的概念：

*  递归点：找到解决当前问题的等价函数（先解决规模比当前问题小一些的函数，依次类推，最终实现对问题的解决） => 有递有归

*  递归出口：当问题解决的时候，已经到达（必须存在）最优问题，不能再次调用函数了

>  注：如果一个递归函数没有递归出口就变成了死循环

**递归三要素**

-  明确你这个函数想要干什么

  对于递归，很重要的一个事就是，**这个函数的功能是什么，他要完成什么样的一件事**，而这个，是完全由你自己来定义的。也就是说，我们先不管函数里面的代码什么，而是要先明白，你这个函数是要用来干什么。

  ```python
  // 算 n 的阶乘(假设n不为0)
  def f(n){
  }
  ```

* 寻找递归结束条件

  所谓递归，就是会在函数内部代码中，调用这个函数本身，所以，我们必须要找出**递归的结束条件**，不然的话，会一直调用自己，进入无底洞。也就是说，我们需要找出**当参数为啥时，递归结束，之后直接把结果返回**，请注意，这个时候我们必须能根据这个参数的值，能够**直接**知道函数的结果是什么。

  例如，上面那个例子，当 n = 1 时，那你应该能够直接知道 f(n) 是啥吧？此时，f(1) = 1。完善我们函数内部的代码，把第二要素加进代码里面，如下：

  ```python
  // 算 n 的阶乘(假设n不为0)
  def f(n){
      if(n == 1){
          return 1;
      }
  }
  ```

  > 只要你觉得参数是什么时，你能够直接知道函数的结果，那么你就可以把这个参数作为结束的条件

* 找出函数的等价关系式

第三要素就是，我们要**不断缩小参数的范围**，缩小之后，我们可以通过一些辅助的变量或者操作，使原函数的结果不变。

找到原函数的一个等价关系式,把这个等价式写进函数里.

```python
// 算 n 的阶乘(假设n不为0)
def f(n){
    if(n <= 2){
        return n;
    }
    // 把 f(n) 的等价操作写进去
    return f(n-1) * n;
}
```

<center>每次做递归的时候，你就强迫自己试着去寻找这三个要素。</center>

# lambda 表达式

**lambda**的应用场景

如果一个函数有一个返回值，并且只有一句代码，可以使用 lambda简化。

**lambda**语法

<center>lambda 参数列表 ： 表达式
> lambda表达式的参数可有可无，函数的参数在lambda表达式中完全适用。

> lambda表达式能接收任何数量的参数但只能返回一个表达式的值。

```python
# 函数
def fn1():
    return 100


print(fn1)
print(fn1())
//<function fn1 at 0x00000257D19D2050>
//100

# lambda表达式
fn2 = lambda: 100
print(fn2)
print(fn2())
//<function <lambda> at 0x00000242E6992E60>
//100
```

**带参数的**lambda

![image-20221113173952312](C:\Users\29248\AppData\Roaming\Typora\typora-user-images\image-20221113173952312.png)

![image-20221113175109757](C:\Users\29248\AppData\Roaming\Typora\typora-user-images\image-20221113175109757.png)



**lambda**参数形式



* 无参数

  ```python
  fn1 = lambda: 100
  print(fn1())
  //100
  ```

* 一个参数

  ```python
  fn1 = lambda a: a
  print(fn1('hello world'))
  //hello world
  ```

* 默认参数

  ```python
  fn1 = lambda a, b, c=100: a + b + c
  print(fn1(10, 20))
  //130
  ```


* 可变参数：``*args``

```python
fn1 = lambda *args: args
print(fn1(10, 20, 30))    =>   //注：这里的可变参数传入到lambda之后，返回值为元组。
//(10, 20, 30)
```

> 注：这里的可变参数传入到lambda之后，返回值为==元组==。

* 可变参数：``**kwargs``

  ```python
  fn1 = lambda **kwargs: kwargs
  print(fn1(name='python', age=20))
  //{'name': 'python', 'age': 20}
  //<class 'dict'>
  ```

> 注：这里的可变参数传入到lambda之后，返回值为==字典==。

* 带判断的lambda表达式

  ```python
  fn1 = lambda a, b: a if a > b else b
  print(fn1(1000, 500))
  //1000
  ```

* 列表数据排序

  ```python
  
  # 按name值升序排列
  students.sort(key=lambda x: x['name'])
  print(students)
  
  # 按name值降序排列
  students.sort(key=lambda x: x['name'], reverse=True)
  print(students)
  
  # 按age值升序排列
  students.sort(key=lambda x: x['age'])
  print(students)
  
  ```

  

```python
[{'name': 'Jack', 'age': 22}, {'name': 'ROSE', 'age': 19}, {'name': 'TOM', 'age': 20}]
[{'name': 'TOM', 'age': 20}, {'name': 'ROSE', 'age': 19}, {'name': 'Jack', 'age': 22}]
[{'name': 'ROSE', 'age': 19}, {'name': 'TOM', 'age': 20}, {'name': 'Jack', 'age': 22}]

```

# 高阶函数

**什么是高阶函数**

==把函数作为参数传入==，这样的函数称为高阶函数，高阶函数是函数式编程的体现。函数式编程就是指这种高度抽象的编程范式。

在Python中，`abs()`函数可以完成对数字求绝对值计算。

```python
abs(-9)
//9
```

`round()`函数可以完成对数字的四舍五入计算。

```python
round(1.09)
//1
```

<center>需求：任意两个数字，按照指定要求整理数字后再进行求和计算。</center>

方法一：

```python
def add_num(a,b):
    return abs(a)+abs(b)
print(add_num(a,b))//a+b
```

方法二：

```python
def sum_num(a, b, f):
    return f(a) + f(b)

result = sum_num(-1, 2, abs)
print(result)  # 3
```

> 方法2的代码会更加==简洁==，函数==灵活性更高==。函数式编程大量使用函数，==减少了==代码的重复，因此程序比较短，开发速度较快。

**内置高阶函数**map()

map(func, lst)，将传入的函数变量func作用到lst变量的每个元素中，并将结果组成新的列表(Python2)/迭代器(Python3)返回

需求：计算`list1`序列中各个数字的2次方。

list1 = [1, 2, 3, 4, 5]

```python
# 需求：计算`list1`序列中各个数字的2次方。
list1 = [1, 2, 3, 4, 5]
func = lambda x: x ** 2
print(map(func, list1), list(map(func, list1)))
// <map object at 0x000002A3A0DB8700> [1, 4, 9, 16, 25]
```

**内置高阶函数**reduce()

reduce(func，lst)，其中func必须有两个参数。每次func计算的结果继续和序列的下一个元素做累积计算。

>  注意：reduce()传入的参数==func必须接收2个参数。==

需求：计算`list1`序列中各个数字的累加和。

```python
import functools
list1 = [1, 2, 3, 4, 5]
func = lambda a,b:a+b
print(functools.reduce(func,list1))
```

**内置高阶函数**filter()

filter(func, lst)函数用于过滤序列, 过滤掉不符合条件的元素, 返回一个 filter 对象。如果要转换为列表, 可以使用 list() 来转换。

```python
list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
func = lambda x:x%2==0
print(list(filter(func,list1)))
//[2, 4, 6, 8, 10]
```

