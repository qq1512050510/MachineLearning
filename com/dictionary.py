#-*- coding:utf-8 -*-
'''
Created on Dec 11, 2019
@content: 字典使用
@author: jyp
'''
people = {'Alice':{'phone':'2341', 'addr':'Foo drive 23'}, 'Beth':{'phone':'9102', 'addr':'Bar street 42'}}
labels = {'phone':'phone number', 'addr':'address'}
name = raw_input('Name:')
# 查找电话号码还是地址
request = raw_input('Phone number (p) or address (a)?')

# 使用正确的键：
key = request  # 如果既不是‘p’也不是‘a’
if request == 'p':key = 'phone'
if request == 'a':key = 'addr'
person = people.get(name, {})
label = labels.get(key, key)
result = person.get(key, 'not available')
print"%s,%s is %s" % (name, label, result)
