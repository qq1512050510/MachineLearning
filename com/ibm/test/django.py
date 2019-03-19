#!/usr/bin/python
#encoding:utf-8
'''
Created on Nov 14, 2017

@author: jyp
'''
import requests 
print "你好"
res = requests.get("http://www.baidu.com");
savefile = open("test.html","w");
savefile.write(res.content);
savefile.close();
