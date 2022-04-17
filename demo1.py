from functools import reduce
# def f(x):
#     return x*x
# list_1=[1,2,3]
# result1=list(map(str,list_1))
# print(result1)


list_1=[1,2,3]
def demo_1(list_1):
    result1=list(map(str,list_1))
    print(result1)
# demo_1(list_1)

def demo_2():
    g=(x for x in range(5))
    for i in g:
        print(i)
# demo_2()

# 斐波拉契数列
def demo_3(max):
    n,a,b=0,0,1
    while n<max:
        # print(b)
        yield b
        a,b=b,a+b
        n=n+1
    return 'done'
# g1 = demo_3(5)
# n = 0
# while True:
#     try:
#         x = next(g)
#         print(x)
#     except StopIteration as e:
#         print('Generator return value:',e.value)
#         break

def triangles(max):
    L = [1]
    n=0
    while n<max:
        yield L
        L = [1] + [L[n] + L[n + 1] for n in range(len(L) - 1)] + [1]
        n=n+1
# g2=triangles(5)
# while True:
#     try:
#         x2 = next(g2)
#         print(x2)
#     except StopIteration as e:
#         print('Generator return value:',e.value)
#         break

def demo_4(n):
    return n*n
result=list(map(demo_4,[1,2,3]))
# print(result)

from functools import reduce
# def fn(x,y):
#     return x*10+y
# result_3 = reduce(fn,[1,3,5,7,9])
# # print(result_3)
# def char2int(s):
#     digits = {'0':0,'1':1,'2':2,'3':3,'4':4,'5':5,'6': 6, '7': 7, '8': 8, '9': 9}
#     return digits[s]
# result = reduce(fn,map(char2int,'135079'))

def str2int(s):
    digest = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}
    def fn(x,y):
        return x*10+y
    def char2int(s):
        return digest[s]
    return reduce(fn,map(char2int,s))
result = str2int('1355079')
# print(result)

# 利用map()函数，把用户输入的不规范的英文名字，
# 变为首字母大写，其他小写的规范名字。
# 输入：['adam', 'LISA', 'barT']，输出：['Adam', 'Lisa', 'Bart']
def normalize(s):
    def first2big(s):
        return s.capitalize()
    return list(map(first2big,s))
s = ['adam', 'LISA', 'barT']
# print(normalize(s))

def prod(s):
    def ji(x,y):
        return x*y
    return reduce(ji,s)
s = [3,5,7,9]
# print(prod(s))

def not_empty(s):
    return s and s.strip()
s=['A', '', 'B', None, 'C', '  ']
result = list(filter(not_empty,s))
# print(result)

n=range(1,1000)
def is_palindrome(n):
    return str(n) == str(n)[::-1] #数字是没有下标的，所以要将n转换为str类型
result = list(filter(is_palindrome,n))
# print(result)

s = ['bob', 'about', 'Zoo', 'Credit']
def func1(n):
    return n.lower()
# print(sorted(s,key=func1))

L = [('Bob', 75), ('Adam', 92), ('Bart', 66), ('Lisa', 88)]
def by_name(t):
    return t[0]
# print(sorted(L,key=by_name))

def by_sorced(t):
    return t[1]
# print(sorted(L,key=by_sorced))

#返回函数
def lazy_sum(n):
    def sum2(*args):
        ax = 0
        for n in args:
            ax = ax + n
        return ax
    def func2(*args):
        init = 1
        for n in args:
            init = init *n
        return init
    if n == '+':
        return sum2
    elif n == '*':
        return func2

a = lazy_sum('*')
# print(a(1,2,3,4,5))

def lazy_sum2(*args):
    def sum2():
        ax = 0
        for n in args:
            ax = ax + n
        return ax
    return sum2
a = lazy_sum2(1,2,3,4)
# print(a())

def createCounter():
    n=0
    def add():
        nonlocal n
        n=n+1
        return n
    return add
CounterA = createCounter()
# print(CounterA(),CounterA(),CounterA(),CounterA(),CounterA())

#匿名函数
def is_odd(n):
    return lambda n :n%2==1
result = is_odd(5)
# print(result(5))

L = list(filter(lambda n :n%2==1, (n for n in range(1, 20))))
# print(L)

#装饰器
def log1(text):
    def decorator(func):
        def wrapper(*args, **kw):
            print('%s %s():' % (text, func.__name__))
            return func(*args, **kw)
        return wrapper
    return decorator
@log1('execute')
def now():
    print('2015-3-25')
# print(now())
# print(now.__name__)


import functools
def log2(text):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kw):
            print('%s %s():' % (text, func.__name__))
            return func(*args, **kw)
        return wrapper
    return decorator
@log2('execute')
def now():
    print('2015-3-25')
# print(now())
# print(now.__name__)

#偏函数
a1 = '12345'
a2 = int(a1,base=8)
# print(a2)

import functools
result = functools.partial(int,base=2)
# print(result('1000000'))
result = functools.partial(int,base=16)
# print(result('12345',base=8))
max1 = functools.partial(max,10)
# print(max1(5,6,7))


#!use/bin/env python3
#coding:utf-8
'a test module'
__author__ = 'dyt'

import sys
# prefix = 'D:\\Anaconda'
# print(sys.argv)
# print(sys.path)
def _private_1(name):
    return 'Hello, %s' % name

def _private_2(name):
    return 'Hi, %s' % name

def greeting(name):
    if len(name) > 3:
        return _private_1(name)
    else:
        return _private_2(name)
# print(greeting('yyqx').upper())

#占位符
def func(i):
    # return ('{}*{}'.format(i,i))
    # return ('%d*%d'%(i,i))
    return (f'{i}*{i}')
# print(func(2))


#命名空间和作用域
Money = 2000
def AddMoney():
    # 想改正代码就取消以下注释:
    global Money
    Money = Money + 1
# print(Money)
AddMoney()
# print(Money)

import math
# dir() 函数一个排好序的字符串列表，内容是一个模块里定义过的名字,返回的列表容纳了在一个模块里定义的所有模块，变量和函数。
# print(dir(math))
# print(math.ceil(12.3))

# 文件读写
file = open('demo1.txt',mode='a+',encoding='utf-8')
# print(file.mode,file.name,file.encoding)
file.write('dyt\n')  #在要加入的字符后面添加\n换行
file.seek(0)  #a+模式下，文件指针默认在末尾，所以需要加一个seek（0），让指针指向开头
# print(file.readline())
# print(file.__next__())

#面相对象编程
# class Person(object):
# # 这里就是初始化你将要创建的实例的属性
#     def __init__(self,hight,weight,age):
#         self.hight = hight
#         self.weight = weight
#         self.age = age
#
# # 定义你将要创建的实例所有用的技能
#     def paoniu(self):
#         print('你拥有泡妞的技能')
#
#     def eat(self):
#         print('you can eat')
#
# # 开始创建实例
# zhangsan=Person(170,50,29)
# lisi = Person(175,100,30)
#
# # 你的实例开始使用它的技能
# zhangsan.paoniu()
# lisi.eat()

class Person(object):
    def __init__(self,name,height,weight,age):
        self.name = name
        self.height = height
        self.weight = weight
        self .age = age
    # def __init__(self):
    #     print('我没有属性')
    def paoniu(self):
        print('你会泡妞')
    def eat(self):
        print('{}会吃饭'.format(self.name))
zs = Person('zs',167,106,25)
ls = Person('ls',165,102,24)
ls.eat()