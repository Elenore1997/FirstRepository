#encoding:utf-8

# n = 2
# if n > 3:
#     print "bigger"
#     print "really big"
# else:
#     print "smaller"
# print "hahaha"

#
# aString = 'Hello World'
# bString = 'tomorrow'
# # listString = str(range(4))
# # print listString
# print aString[1:8]  #第X到X-1位切片
# print bString[-6:-1]    #负号从后面开始

# 成员操作符：in/not in
# if 'you' in 'i lov e you':
#     print 'yes'
# else:
#     print 'no'

# fDict = {}.fromkeys(('id', 'score'))    #创建具有相同值的字典，没有则为None
# print fDict
# # ffDict = {'name':'laji', 'age':233}
# # print ffDict
# # empty = {}
# # print empty
# formDict = {}.fromkeys(('x','y'), (1,2))
# print formDict
# for key in formDict.keys():
#     print key,
# for value in formDict.values():
#     print value,

#
# firstSet = set([1, 2, 3])
# secondSet = set([3, 4, 5])
# print firstSet & secondSet #交集
# print firstSet | secondSet  #并集
# print firstSet - secondSet  #作差

# print [x+2 for x in range(6) if x % 2]

# def cal(*num):#累加函数
#     sum = 0
#     for n in num:
#         sum += n
#     return sum
# print cal(1, 2, 3)

# def mycmp(a, b): #比较大小
#     if a > b:
#         return 1
#     if a == b:
#         return 0
#     if a < b:
#         return -1
# print mycmp(1, 2)
#
# def cifang(x, n=2):#默认为2次方
#     s = 1
#     while n > 0:
#         n -=1
#         s *=x
#     return s
# print cifang(5, 3)
#
# class Student():
#     def __init__(self, name, id):
#         self.name = name
#         self.id = id
#     def show(self):
#         print "student:", self.name, " id:", self.id
#     def money(self):
#         print 'no money'
#
# st = Student('Mike',23333)
# st.show()
#
# class ShabiStudent(Student):
#     def __init__(self, name, id, age):
#         self.name = name
#         self.id = id
#         self.age = age
#     def show(self):
#         print "shabi student:", self.name, " id:", self.id, " age:", self.age
# shabi = ShabiStudent('cqd', 123123, 19)
# shabi.show()
# shabi.money()

# alist = [1, 'majunteng', 233]
# alist.insert(1,666)
# print alist[1:]

# x = input('enter a number')
# print x + 233

# def division():
#     try:
#         x = input('enter the first number:')
#         y = input('enter the second number:')
#         print x/y
#     except Exception as e:
#         print e.message
#     finally:
#         print '这句话总会执行'
# division()

# file = open('/home/mark/Documents/树蛙/python讲解.txt', 'r')
# for line in file.readlines():
#     print line,
#/home/mark/PycharmProjects/untitled/hello.py
with open('/home/mark/Documents/树蛙/python讲解.txt')as file:
    for line in file.readlines():
        print line,