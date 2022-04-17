# 普通类和实例
class Student(object):
    def __init__(self,name,score):
        self.name = name
        self.score = score
    def get_grade(self):
        if self.score>=80:
            print('{}的成绩是{}'.format(self.name,self.score))
        elif self.score>=60 and self.score<80:
            print('{}的成绩是{}'.format(self.name,self.score))
        else:
            print('{}的成绩是{}'.format(self.name,self.score))
# yyqx = Student('yyqx',98)
# wjk  = Student('wjk',99)
'''
和静态语言不同，Python允许对实例变量绑定任何数据，
也就是说，对于两个实例变量，虽然它们都是同一个类的不同实例，但拥有的变量名称都可能不同：
'''
# yyqx.age=25     #给yyqx这个实力动态绑定了age属性
# yyqx.get_grade()
# print(dir(yyqx))   #查看yyqx wjk这两个实例都有哪些属性
# print(dir(wjk))

# 带有访问限制的类和实例
'''
如果要让内部属性不被外部访问，可以把属性的名称前加上两个下划线__
在Python中，实例的变量名如果以__开头，就变成了一个私有变量（private），只有内部可以访问，外部不能访问
'''
class Student(object):
    def __init__(self,name,score):
        self.__name = name
        self.__score = score
    def print_score(self):
        print(f'{self.__name}:{self.__score}')
    #给Student类增加get_name和get_score方法,使得外部代码获取name和score属性
    def get_name(self):
        return self.__name
    def get_score(self):
        return self.__score
    #给Student类增加set_score方法，使得外部代码可以修改score
    def set_score(self,score):
        self.__score = score
        if 0<=score<=100:
            self.__score = score
        else:
            raise ValueError('bad score')

# yyqx = Student('yyxq',98)
# yyqx.__score = 50
# print(yyqx.get_score())
# print(dir(yyqx))
# print(yyqx.get_name())
# print(yyqx.get_score())
# yyqx.set_score(56)
# print(yyqx.get_score())

class Student(object):
    def __init__(self,name,gender):
        self.__name = name
        self.__gender = gender
    def get_gender(self):
        return self.__gender
    def set_gender(self,gender):
        self.__gender = gender

wjk = Student('wjk','男')
wjk.set_gender('我不是女生')
print(wjk.get_gender())
# print(dir(wjk))
# print(isinstance(wjk,Student))

class Animal(object):   #编写Animal类
    def run(self):
        print("Animal is running...")

class Dog(Animal):  #Dog类继承Amimal类，没有run方法
    pass

class Cat(Animal):  #Cat类继承Animal类，有自己的run方法
    def run(self):
        print('Cat is running...')
    pass

class Car(object):  #Car类不继承，有自己的run方法
    def run(self):
        print('Car is running...')

class Stone(object):  #Stone类不继承，也没有run方法
    pass

def run_twice(animal):
    animal.run()
    animal.run()

# run_twice(Animal())
# run_twice(Dog())
# run_twice(Cat())
# run_twice(Car())
# run_twice(Stone())

#type()
# print(type(123))
# print(type('123'))
# print(type(12.3))

import types
def func():
    pass
# print(type(func) == types.FunctionType)
# print(type(abs) == types.BuiltinFunctionType)
# print(type(lambda x : x)==types.LambdaType)
# print(type((x for x in range(3))) == types.GeneratorType)
# print(isinstance(123,int))
# print(isinstance('dyt',str))
# print(type((x for x in range(5))))

class Myobject(object):
    def __init__(self):
        self.x =9
    def power(self):
        return self.x * self.x
obj1 = Myobject()
# print(obj1.x)
# print(hasattr(obj1,'x'))
# print(getattr(obj1,'x'))
# setattr(obj1,'x',12)
# print(getattr(obj1,'x'))

class TFBOYS(object):
    # 在class中定义属性，这种属性是类属性
    team = 'TFBOYS'
    def __init__(self,name):
        # 给实例绑定属性的方法是通过实例变量，或者通过self变量
        # 实例属性优先级比类属性高
        self.name = name

member1 = TFBOYS('王俊凯')
member2 = TFBOYS('易烊千玺')
member3 = TFBOYS('王源')
# print(f'大家好，我是来自{TFBOYS.team}的{member1.name}')
# print(f'大家好，我是来自{member1.team}的{member1.name}')
# print(f'大家好，我是来自{member2.team}的{member2.name}')
# print(f'大家好，我是来自{member3.team}的{member3.name}')
member1.team = 'tfboys'
TFBOYS.team = 'tfboy'
# print(member1.team)
# print(TFBOYS.team)
# del member1.team   #删除实例属性team
# print(member1.team)

class Student(object):
    count = 0
    # __init__方法会在创建实例时自动被执行一次，其他的方法不会
    def __init__(self,name):
        self.name = name
        Student.count =Student.count+1
        self.count = Student.count

    def test(self):
        pass
yyqx = Student('yyqx')
wjk = Student('wjk')
wy = Student('wy')
# print(Student.count)
# print(yyqx.count)


class School(object):
    # __slots__变量，用于限制该class实例能添加的属性。
    # __slots__定义的属性仅对当前类实例起作用，对继承的子类是不起作用的
    __slots__ = ('name','built_year')
    def __init__(self):
        pass
class Student(School):
    __slots__ = ('name','age')
    def __init__(self):
        pass
sch = School()
sch.name = '重庆一中'
# print(hasattr(sch,'name'))
# sch.address = '重庆'
stu = Student()
# 子类实例允许定义的属性就是自身的__slots__加上父类的__slots__。
stu.built_year = '1998'
# print(sch.name)
# print(stu.built_year)


'''
@property装饰器就是负责把一个方法变成属性调用
'''
class Screen(object):
    @property
    def resolution(self):
        return self._width*self._height
    @property
    def width(self):
        return self._width
    @width.setter
    def width(self,w):
        self._width = w
    @property
    def height(self):
        return self._height
    @height.setter
    def height(self,h):
        self._height = h

result = Screen()
result.width = 1024
result.height = 768
# print(result.width)
# print(result.height)
# print(result.resolution)

'''
多重继承:通过多重继承，一个子类就可以同时获得多个父类的所有功能。
'''
# class Animal(object):
#     def func(self):
#         print('我是Animal')
class Mammal(Animal):
    def func(self):
        return ('我是Mammal')
class Bird(Animal):
    pass
class Dog(Mammal):
    pass
class Bat(Mammal):
    pass
class Parrot(Bird):
    pass
class Ostrich(Bird):
    pass
class Runnable(object):
    def func2(self):
        return ('我是Runnable')
class Flyable(object):
    pass
# 通过多重继承，一个子类就可以同时获得多个父类的所有功能。
# class Dog(Mammal,Runnable):
#     print ('我是dog')

# dog = Dog()
# print(dog.func2())