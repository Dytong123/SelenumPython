# with open('demo1.txt','r') as f:
#     # list = f.readlines()
#     # print(list[0:2])
#     for line in f:
#         print(line.strip())   #删除掉文件末尾的\n\

# with open(path = '清晰图片.jpg',mode='rb',encoding='utf-8',errors='ignore') as f:
#     print(f.read())

import os
#如果是posix，说明系统是Linux、Unix或Mac OS X，如果是nt，就是Windows系统
# print(os.name)
# print(os.environ)
# print(os.environ.get('PATH'))
#查看当前目录的绝对路径
# print(os.path.abspath('.'))
# os.path.join(r'\python\python_practice\package','demo5.py')
# 创建一个目录
# os.makedirs(r'\python\python_practice\package2')
# 删除一个目录
# os.rmdir(r'\python\python_practice\package2')
# print(os.path)

# print(__file__)

seq1 = ['hello','good','boy','doiido']
seq2 = 'hello good boy doiido'
seq3 = ('hello','good','boy','doiido')
seq4 = {'hello':1,'good':2,'boy':3,'doiidi':'4'}
print(','.join(seq4))