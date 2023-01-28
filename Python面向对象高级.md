<center><b>Python</b>面向对象高级</center>

# 面向对象三大特性

**封装、继承、多态**

① 封装

将属性和方法书写到类的里面的操作即为封装，封装可以为属性和方法添加私有权限。

② 继承

子类默认继承父类的所有属性和方法，与此同时子类也可以重写父类属性和方法。

③ 多态

多态是同一类事物具有的多种形态。不同的对象调用同一个接口（方法），表现出不同的状态，称为多态。

# Python中的继承

生活中的继承，一般指的是子女继承父辈的财产。

![image-20221218135202336](E:\Administrator\Desktop\学习\image-20221218135202336.png) 我们接下来来聊聊Python代码中的“继承”：类是用来描述现实世界中同一组事务的共有特性的抽象模型，但是类也有上下级和范围之分，比如：**生物 => 动物 => 哺乳动物 => 灵长型动物 => 人类 => 黄种人**

从哲学上说，就是共性与个性之间的关系，比如：白马和马！所以，我们在OOP代码中，也一样要体现出类与类之间的共性与个性关系，这里就需要通过类的继承来体现。简单来说，如果一个类A使用了另一个类B的成员（属性和方法），我们就可以说A类继承了B类，同时这也体现了OOP中代码重用的特性！

**继承的基本语法**

```python
# 父类B
class B(object):
	pass

# 子类A
class A(B):
    pass

```

> 在Python中，所有类默认继承object类，object类是顶级类或基类；其他子类叫做派生类。

**与继承相关的几个概念**

**继承**：一个类从另一个已有的类获得其成员的相关特性，就叫作继承！

**派生**：从一个已有的类产生一个新的类，称为派生！

很显然，继承和派生其实就是从不同的方向来描述的相同的概念而已，本质上是一样的！

**父类**：叫作基类，就是指已有被继承的类！

**子类**：叫作派生类或扩展类

**扩展**：在子类中增加一些自己特有的特性，就叫作扩展，没有扩展，继承也就没有意义了！

**单继承**：一个类只能继承自一个其他的类，不能继承多个类，单继承也是大多数面向对象语言的特性！

**多继承**：一个类同时继承了多个父类， （C++、Python等语言都支持多继承）

**Python** **中的单继承**

单继承：一个类只能继承自一个其他的类，不能继承多个类。这个类会有具有父类的属性和方法。

```python
# 父类B
class B(object):
	pass

# 子类A
class A(B):
    pass
```

案例：猫，狗 都属于动物，它们行为相似性高。都会吃、会睡、会叫

```python
class Animal(object):
    def eat(self):
        print('吃...')

    def sleep(self):
        print('睡...')

    def call(self):
        print('叫...')


class Dog(Animal):
    pass


class Cat(Animal):
    pass

Cat().sleep()
# 睡...
class Dog(Animal):
    def mac(self):
        print("999")
        
    pass


class Cat(Dog):
    pass

Cat().mac()
# 999
```

**重写父类属性和方法**

**重写也叫作覆盖，就是当子类成员与父类成员名字相同的时候，从父类继承下来的成员会重新定义！**



此时，通过子类实例化出来的对象访问相关成员的时候，真正其作用的是子类中定义的成员！



上面单继承例子中 Animal 的子类 Cat和Dog 继承了父类的属性和方法，但是我们狗类Dog 有自己的叫声'汪汪叫'，猫类 Cat 有自己的叫声 '喵喵叫' .

这时我们需要对父类的 call() 方法进行重构。如下：

​	![image-20221218142200917](E:\Administrator\Desktop\学习\image-20221218142200917.png)

```
吃...
汪汪叫...
w
吃...
喵喵叫...
```

思考一个问题：此时父类中的call方法还在不在？

> 答：还在，只不过是在其子类中找不到了。类方法的调用顺序，当我们在子类中重构父类的方法后，Cat子类的实例先会在自己的类 Cat 中查找该方法，当找不到该方法时才会去父类 Animal 中查找对应的方法。

**调用父类属性和方法**

==super()：调用父类属性或方法，完整写法：super(当前类名, self).属性或方法()==

```python
class Animal():
    def __init__(self, name, age):
        self.name = name
        self.age = age


    def eat(self):
        print('吃...')


    def sleep(self):
        print('睡...')


    def call(self):
        print('叫...')

class Dog(Animal):
    def __init__(self, name, age, sex):
        super().__init__(name, age)
        self.sex = sex


    def __str__(self):
        return f'{self.name}，今年{self.age}岁了，我会汪汪叫...'


class Cat(Animal):
    def __init__(self, name, age, sex):
        super().__init__(name, age)
        self.sex = sex

    def __str__(self):
        return (f'{self.name}，今年{self.age}岁了，我会喵喵叫...')

a = Cat("name", 333, 87).__str__()
print(a)
```

**Python** **中的多继承实现**

多继承：一个类同时继承了多个父类，并且同时具有所有父类的属性和方法例如：孩子会继承父亲 和 母亲的方法。

```python
class Father(object):
    pass


class Mother(object):
    pass


class Child(Father, Mother):
    pass

```

注：MRO(Method Resolution Order)：方法解析顺序，我们可以通过类名.__mro__或类名.mro()获得“类的层次结构”，方法解析顺序也是按照这个“类的层次结构”寻找到。

# Python中的多态

多态指的是一类事物有多种形态。

定义：**多态是一种使用对象的方式，子类重写父类方法，调用不同子类对象的相同父类方法，可以产生不同的执行结果**

① **多态依赖继承**

② **子类方法必须要重写父类方法**

> 好处：调用灵活，有了多态，更容易编写出通用的代码，做出通用的编程，以适应需求的不断变化！

**多态的实现步骤**

* 定义父类，并提供公共方法

* 定义子类，并重写父类方法

* 传递子类对象给调用者，可以看到不同子类执行效果不同

类具有继承关系，并且子类类型可以向上转型看做父类类型，如果我们从 Animal 派生出 Cat和 Dog，并都写了一个 call() 方法，如下示例：

```python
class Animal(object):  
   def __init__(self, name, age):
       self.name = name
       self.age = age
   def call(self):
       print(self.name, '会叫')
```

<center>¦¦¦¦¦¦ - - - ¦¦¦¦¦¦¦

```python
class Cat(Animal):
   def __init__(self, name, age, sex):
       super(Cat, self).__init__(name, age)
       self.sex = sex

   def call(self):
       print(self.name, '会“喵喵”叫')

class Dog(Animal):
   def __init__(self, name, age, sex):
       super(Dog, self).__init__(name, age)
       self.sex = sex
   def call(self):
       print(self.name, '会“汪汪”叫')
```

**这种行为称为多态。也就是说，方法调用将作用在 all 的实际类型上。**C 是 Cat 类型，它实际上拥有自己的 call() 方法以及从 Animal 继承的 call 方法，但调用 C .call() 总是先查找它自身的定义，如果没有定义，则顺着继承链向上查找，直到在某个父类中找到为止。传递给函数 do(all) 的参数 all 不一定是 Animal 或 Animal 的子类型。任何数据类型的实例都可以，只要它有一个 call() 的方法即可。其他类不继承于 Animal，具备 call 方法也可以使用 do 函数。这就是动态语言，动态语言调用实例方法，不检查类型，只要方法存在，参数正确，就可以调用。