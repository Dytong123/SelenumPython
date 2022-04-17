'''
1.定制类
2.使用枚举类
3.使用元类
'''
# 1.定制类
class Student():

    def __init__(self,name):
        self.name = name
    def __str__(self):
        return ('Student object (name:%s)'%self.name)
    def __repr__(self):
        return ('Student object (name:%s)'%self.name)

a = Student('yyqx')
# print(a)

class Fib():
    def __init__(self):
        self.a = 0
        self.b = 1
    def __iter__(self):
        return self      #实例本身就是迭代对象，故返回自己
    def __next__(self):
        self.a = self.b
        self.b = self.a+self.b
        if self.a>100:
            raise StopIteration()
        return self.a
# for n in Fib():
#     print(n)

class Fib():
    def __getitem__(self, item):
        a,b = 0,1
        for x in range(item):
            a,b = b, a+b
        return a
f = Fib()
# print(f[10])

# 2.使用枚举类
from enum import Enum
Month = Enum('month',('Jan','Feb','Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'))
# print(Month.__members__.items())
# for name,member in Month.__members__.items():
#     print(name,'=>',member,',',member.value)

from enum import Enum,unique
# @unique装饰器可以帮助我们检查保证没有重复值
@unique
class Weekday(Enum):
    Sun = 0  # Sun的value被设定为0
    Mon = 1
    Tue = 2
    Wed = 3
    Thu = 4
    Fri = 5
    Sat = 6

day1 = Weekday.Mon
# print(day1)
# print(Weekday['Mon'])
# print(Weekday(1))
# print(Weekday.Mon.value)
# print(day1.value)
@unique
class Gender(Enum):
    Male = 0
    Female = 1
# sex1 = Gender.Male
# print(sex1.value)

class Student(object):
    def __init__(self,name,gender):
        self.name = name
        self.gender = gender
bart = Student('Bart', Gender.Male)
# if bart.gender == Gender.Male:
#     print('测试通过!')
# else:
#     print('测试失败!')

# 3.使用元类
# class Hello(object):
#     def hello(self,name='world'):
#         print('Hello,%s'%name)
#
# h = Hello()
# print(h.hello())
# print(type(Hello))
# print(type(h))

# type()函数既可以返回一个对象的类型，又可以创建出新的类型
'''
要创建一个class对象，type()函数依次传入3个参数：
    1.class的名称；
    2.继承的父类集合，注意Python支持多重继承，如果只有一个父类，别忘了tuple的单元素写法；
    3.class的方法名称与函数绑定，这里我们把函数fn绑定到方法名hello上
'''
def fn (self,name='world'):#先定义函数
    print('Hello，%s'%name)
Hello = type('Hello',(object,),dict(hello=fn))#创建Hello class
h =Hello()
# print(h.hello())
# print(type(Hello))
# print(type(h))


'''
1.错误处理
2.调试
3.单元测试
4.文档测试
'''
# 1.错误处理
# try:
#     print('try...')
#     r = 10 / 2
#     print('result:', r)
# except ZeroDivisionError as e:
#     print('except:', e)
# finally:
#     print('finally...')
# print('END')


import logging
#
# def foo(s):
#     return 10 / int(s)
#
# def bar(s):
#     return foo(s) * 2
#
# def main():
#     try:
#         bar('0')
#     except Exception as e:
#         logging.exception(e)
# main()
# print('END')

class FooError(ValueError):
    pass

def foo(s):
    n = int(s)
    if n==0:
        raise FooError('invalid value: %s' % s)
    return 10 / n

# foo('0')


from functools import reduce

def str2num(s):
    return int(s)

def calc(exp):
    ss = exp.split('+')
    ns = map(str2num, ss)
    return reduce(lambda acc, x: acc + x, ns)

def main():
    r = calc('100 + 200 + 345')
    print('100 + 200 + 345 =', r)
    try:
        r = calc('99 + 88 + 7.6')
    except ValueError as e:
        logging.exception(e)
        print('ValueError:',e)
    print('99 + 88 + 7.6 =', r)

# main()

import logging
logging.basicConfig(level=logging.INFO)
s = '0'
n = int(s)
logging.info('n = %d' % n)
print(10 / n)
